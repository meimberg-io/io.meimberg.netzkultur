#!/usr/bin/env python3
"""Bild aus einer externen Quelle holen und Lightroom-taugliche Metadaten schreiben.

Der Schreibteil ist quellenunabhängig und schreibt die Felder, die Lightroom
im Metadatenpanel anzeigt:

    Titel                  -> XMP-dc:Title       (+ IPTC:ObjectName)
    Beschreibung           -> XMP-dc:Description (+ IPTC:Caption-Abstract)
    Alt-Text               -> XMP-iptcCore:AltTextAccessibility
    Copyright              -> XMP-dc:Rights      (+ IPTC:CopyrightNotice, EXIF)
    Bed. f. Rechtenutzung  -> XMP-xmpRights:UsageTerms
    Copyright-Info-URL     -> XMP-xmpRights:WebStatement (+ Photoshop:URL)
    Quelle                 -> XMP-photoshop:Source
    Credit                 -> XMP-photoshop:Credit

Quelle und Credit werden immer geschrieben, damit die Herkunft in der Datei
steht und nicht nur im Kopf. Sichtbar werden sie im Panel über "Anpassen..."
-> "IPTC-Status" -> "Quelle" bzw. "Credit".

Bewusst NICHT beschrieben wird xmp:Label. Das ist Lightrooms Farb-Label
("Beschriftung festlegen" -> Rot/Gelb/...), kein Textfeld für Bildunterschriften.
Damit die Beschreibung im Panel sichtbar ist, muss dort die Sektion
"IPTC-Inhalt" -> "Beschreibung" eingeschaltet sein.

Was sich pro Quelle unterscheidet, ist allein die Recherche:

  commons   Wikimedia Commons. Urheber, Lizenz und Lizenz-URL kommen
            maschinenlesbar aus der API.
  demozoo   Demozoo (Demoszene-Datenbank). Liefert Gruppe, Titel und
            Erscheinungsdatum, aber KEINE Lizenz -- die Screenshots sind
            Einzelbilder geschützter Werke. "Bed. f. Rechtenutzung" bleibt
            dann leer; wer das Werk gemacht hat und wo es herkommt, steht in
            Copyright, Quelle und Copyright-Info-URL. Mit --zitat wird die
            Nutzung stattdessen als Bildzitat ausgewiesen.
  manual    Beliebige URL. Es wird nichts recherchiert, alle Rechtefelder
            kommen per Flag.

Titel, Beschreibung und Alt-Text sind immer redaktionell, nie recherchiert.

Beispiele:
    scripts/bild-einziehen.py https://commons.wikimedia.org/wiki/File:Amiexpress.png \\
      --out assets/01 --name amiexpress.png \\
      --titel "AmiExpress" --beschreibung "AmiExpress Hauptmenü"

    scripts/bild-einziehen.py https://demozoo.org/productions/142/ \\
      --out assets/01 --screenshots 1-4 \\
      --prefix demo_kefrens_desertdream

    scripts/bild-einziehen.py https://example.org/bild.jpg --manual \\
      --out assets/01 --name foo.jpg \\
      --copyright "Foto: Jemand" --lizenz "Presse-Freigabe per Mail 2026-07-30"

Mehrere Bilder auf einmal: --batch <datei.json> mit einer Liste von Objekten,
deren Keys den Langoptionen entsprechen (url, name, titel, beschreibung, ...).
"""

import argparse
import html
import json
import re
import shutil
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

COMMONS_API = "https://commons.wikimedia.org/w/api.php"
DEMOZOO_API = "https://demozoo.org/api/v1/productions"
UA = "meimberg-contenthub/1.0 (https://meimberg.io; oli@meimberg.io) python-urllib"

# Formate mit IPTC-Block und Photoshop-IRB. Bei PNG/WEBP/SVG bleibt es bei XMP,
# so macht es Lightroom auch.
IPTC_CAPABLE = {".jpg", ".jpeg", ".tif", ".tiff"}

# Navigations-Links, die Commons in das Artist-Feld rendert und die in einer
# Copyright-Zeile nichts zu suchen haben ("Coderman (talk) (Uploads)").
ARTIST_NOISE = {"uploads", "contribs", "beiträge", "gallery", "galerie"}

# Räumt die Quelle keine Lizenz ein, bleibt das Feld LEER. Es trägt die
# Bedingungen der Rechtenutzung, also eine Zusage des Rechteinhabers -- eine
# Notiz an uns selbst gehört dort nicht hinein und liest sich beim Empfänger
# wie ein Eingeständnis. Was in dem Fall trägt, steht in den anderen Feldern:
# Copyright nennt den Urheber, Quelle und Copyright-Info-URL verweisen dorthin,
# wo er zu finden ist. Der Hinweis auf die fehlende Zusage erscheint beim Lauf
# auf der Konsole, nicht in der Datei.

# Wortlaut für --zitat: Nutzung als Bildzitat, wenn die Quelle keine Lizenz
# einräumt. Bewusst kein Default, sondern eine bewusste Entscheidung pro Lauf,
# denn es ist eine rechtliche Einschätzung und keine recherchierte Tatsache.
BILDZITAT = "Bildzitat § 51 UrhG"

# Lizenzangaben, die keine Freigabe sind. "Fair use" ist US-Doktrin und gilt in
# Deutschland nicht -- wer den Wert unverändert in die Datei schreibt, hält
# später eine Erlaubnis in der Hand, die es hier nie gab.
UNFREI = re.compile(r"fair\s*use|non-?free|unfree|all rights reserved|"
                    r"copyrighted free use|screenshot of copyrighted", re.I)


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def strip_html(value):
    text = re.sub(r"<[^>]+>", "", value or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


# --------------------------------------------------------------- Quelle: Commons

def clean_artist(value):
    """Artist-Zeile entrümpeln: geklammerte Navigations-Links entfernen."""
    text = strip_html(value)
    text = re.sub(r"\(([^()]*)\)",
                  lambda m: "" if m.group(1).strip().lower() in ARTIST_NOISE
                  else m.group(0), text)
    return re.sub(r"\s+", " ", text).strip(" ,")


def license_hints(categories):
    """Weitere Lizenzen, die die Kategorien verraten. Commons erlaubt Mehrfach-
    Lizenzierung, die API liefert aber nur *eine* LicenseShortName."""
    return [c.strip() for c in (categories or "").split("|")
            if re.search(r"creative commons|GFDL|CC[- ]BY|public domain", c, re.I)]


def commons_query(source):
    base = {"action": "query", "prop": "imageinfo", "format": "json",
            "iiprop": "url|extmetadata", "redirects": "1"}
    parsed = urllib.parse.urlparse(source)
    query = urllib.parse.parse_qs(parsed.query)

    # MediaViewer-Links tragen die Datei im Fragment, nicht im Pfad:
    # .../wiki/Multi-user_dungeon#/media/File:Actsmudgnome.png
    # Der Namensraum ist sprachabhängig (Datei:, Fichier:, Archivo: ...), die
    # Commons-API kennt nur File: -- daher alles vor dem Doppelpunkt ersetzen.
    treffer = re.search(r"/media/(.+)$", parsed.fragment or "")
    if treffer:
        titel = urllib.parse.unquote(treffer.group(1))
        _, _, name = titel.partition(":")
        return {**base, "titles": f"File:{name or titel}"}

    if "curid" in query:
        return {**base, "pageids": query["curid"][0]}
    if "title" in query:
        return {**base, "titles": query["title"][0]}
    if parsed.netloc.startswith("upload."):
        parts = [p for p in parsed.path.split("/") if p]
        name = parts[-2] if "/thumb/" in parsed.path else parts[-1]
        return {**base, "titles": f"File:{urllib.parse.unquote(name)}"}
    if parsed.path.startswith("/wiki/"):
        return {**base, "titles": urllib.parse.unquote(parsed.path[len("/wiki/"):])}

    name = source if source.lower().startswith("file:") else f"File:{source}"
    return {**base, "titles": name}


def wiki_name(host):
    """'de.wikipedia.org' -> 'Wikipedia (de)', für die Credit-Zeile."""
    treffer = re.match(r"([a-z-]+)\.wikipedia\.org$", host or "")
    return f"Wikipedia ({treffer.group(1)})" if treffer else host


def normiere_lizenz(kurz):
    """'CC-BY-SA-3.0' -> 'CC BY-SA 3.0'. Rein typografisch, damit die Angaben
    aus verschiedenen Wikis in einem Ordner gleich aussehen."""
    treffer = re.fullmatch(r"CC-([A-Z]+(?:-[A-Z]+)*)-([\d.]+)", kurz or "")
    return f"CC {treffer.group(1)} {treffer.group(2)}" if treffer else kurz


def wiki_seite(host, params):
    """Holt die Dateiseite von einem MediaWiki-Host, oder None.

    Nicht jede Wikipedia-Datei liegt auf Commons: lokale Uploads bleiben im
    jeweiligen Sprach-Wiki, und ein Sprach-Wiki löst umgekehrt fremde
    Commons-Dateien nicht auf. Deshalb wird beides der Reihe nach gefragt.
    Die API-Antwort hat überall dieselbe Form, der Rest des Adapters muss
    also nicht wissen, woher die Datei kam."""
    try:
        data = fetch_json(f"https://{host}/w/api.php?"
                          + urllib.parse.urlencode(params))
    except Exception:
        return None
    page = next(iter(data.get("query", {}).get("pages", {}).values()), {})
    if "missing" in page or "invalid" in page or not page.get("imageinfo"):
        return None
    return page


def from_commons(source, opts):
    params = commons_query(source)
    quell_host = urllib.parse.urlparse(source).netloc

    page = wiki_seite("commons.wikimedia.org", params)
    heimat = "Wikimedia Commons"
    if page is None and quell_host and "wikimedia.org" not in quell_host:
        page = wiki_seite(quell_host, params)
        heimat = wiki_name(quell_host)
    if page is None:
        raise SystemExit(
            f"FEHLER: {params.get('titles', source)!r} weder auf Commons noch "
            + (f"auf {quell_host} gefunden." if quell_host else "gefunden.")
            + "\nIst das eine Datei-Seite? Sonst mit --manual laden und die "
              "Rechtefelder selbst setzen.")

    info = page["imageinfo"][0]
    meta = info.get("extmetadata", {})

    def field(key):
        return strip_html(meta.get(key, {}).get("value", ""))

    artist = clean_artist(meta.get("Artist", {}).get("value", ""))
    license_short = normiere_lizenz(field("LicenseShortName"))
    hints = license_hints(field("Categories"))

    warnungen = []
    if hints and not opts.get("lizenz"):
        warnungen.append(f"mehrfach lizenziert, API nahm {license_short!r}; "
                         f"Kategorien nennen: {', '.join(hints)}")
    # Lizenz verlangt Namensnennung, aber es gibt niemanden zu nennen. Häufig
    # steckt der Urheber dann im Upload-Kommentar oder im Wikitext der
    # Dateiseite und muss von Hand nachgetragen werden.
    if UNFREI.search(license_short) or UNFREI.search(field("UsageTerms")):
        warnungen.append(
            f"{license_short!r} ist KEINE freie Lizenz. Fair Use ist US-Doktrin und "
            "gilt in Deutschland nicht. Entweder freie Alternative suchen oder "
            "bewusst als Bildzitat verwenden (--zitat)")
    if not artist and field("AttributionRequired").lower() == "true":
        warnungen.append(
            "Lizenz verlangt Namensnennung, die API kennt aber keinen Urheber. "
            f"Dateiseite und Upload-Historie prüfen: {info['descriptionurl']} "
            "-- dann --copyright setzen")

    return [{
        "adapter": "commons" if heimat == "Wikimedia Commons" else heimat,
        "herkunft": f"{page['title']} ({heimat})",
        "download_url": info["url"],
        # Overrides gelten hier genauso wie bei den anderen Adaptern: die
        # Recherche liefert den Vorschlag, das Flag gewinnt.
        "copyright": opts.get("copyright") or (
            f"{artist} via {heimat}" if artist else heimat),
        "lizenz": opts.get("lizenz") or license_short,
        # MediaWiki liefert LicenseUrl teils protokollrelativ ("//host/...").
        "infourl": opts.get("infourl") or (
            re.sub(r"^//", "https://",
                   meta.get("LicenseUrl", {}).get("value", "").strip())
            if opts.get("url_mode", "license") == "license"
            else info["descriptionurl"]),
        "quellseite": info["descriptionurl"],
        "quelle": opts.get("quelle") or info["descriptionurl"],
        "credit": opts.get("credit") or (
            f"{artist} via {heimat}" if artist else heimat),
        "fremdbeschreibung": field("ImageDescription"),
        "vorschlagsname": urllib.parse.unquote(
            info["url"].rsplit("/", 1)[-1]).lower(),
        "warnungen": warnungen,
    }]


# --------------------------------------------------------------- Quelle: Demozoo

def parse_picks(spec, maximum):
    """'1-4', '1,3,7' oder '2' -> Liste von 1-basierten Indizes."""
    picks = []
    for part in str(spec).split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            picks.extend(range(int(a), int(b) + 1))
        elif part:
            picks.append(int(part))
    for i in picks:
        if not 1 <= i <= maximum:
            raise SystemExit(f"FEHLER: Screenshot {i} gibt es nicht "
                             f"(Production hat {maximum})")
    return picks


def from_demozoo(source, opts):
    match = re.search(r"/productions/(\d+)", source)
    if not match:
        raise SystemExit(f"FEHLER: keine Demozoo-Production-ID in {source!r}")

    prod = fetch_json(f"{DEMOZOO_API}/{match.group(1)}/?format=json")
    shots = prod.get("screenshots", [])
    if not shots:
        raise SystemExit(f"FEHLER: Production {prod.get('title')!r} hat keine Screenshots")

    gruppe = ", ".join(a["name"] for a in prod.get("author_nicks", [])) or "unbekannt"
    jahr = (prod.get("release_date") or "")[:4]
    plattform = ", ".join(p["name"] for p in prod.get("platforms", []))
    picks = parse_picks(opts.get("screenshots", 1), len(shots))

    # Demozoo räumt an den Screenshots keine Rechte ein und nennt keinen
    # Uploader -- es sind Einzelbilder eines geschützten Werks. Ohne explizite
    # --lizenz bleibt das offen und wird auch so in die Datei geschrieben.
    lizenz = opts.get("lizenz") or (BILDZITAT if opts.get("zitat") else "")
    warnung = None if (opts.get("lizenz") or opts.get("zitat")) else (
        f"Demozoo nennt keine Lizenz. Rechte am Werk liegen bei {gruppe}. "
        f"Feld 'Bed. f. Rechtenutzung' bleibt leer, Herkunft steht in "
        f"Copyright, Quelle und Copyright-Info-URL. Für die Nutzung als "
        f"Bildzitat: --zitat")

    kandidaten = []
    for nr in picks:
        shot = shots[nr - 1]
        kandidaten.append({
            "adapter": "demozoo",
            "herkunft": f"{prod['title']} ({gruppe}"
                        f"{', ' + jahr if jahr else ''}), Screenshot {nr}",
            "download_url": shot["original_url"],
            "copyright": opts.get("copyright") or gruppe,
            "lizenz": lizenz,
            "infourl": opts.get("infourl") or prod["demozoo_url"],
            "quellseite": prod["demozoo_url"],
            "quelle": f"Demozoo, {prod['demozoo_url']}",
            "credit": f"{gruppe} via Demozoo",
            "fremdbeschreibung": f"{prod['title']} von {gruppe}"
                                 f"{', ' + jahr if jahr else ''}"
                                 f"{', ' + plattform if plattform else ''}",
            "vorschlagsname": f"{nr:02d}" + Path(
                urllib.parse.urlparse(shot["original_url"]).path).suffix,
            "index": nr,
            "warnungen": [warnung] if warnung else [],
        })
    return kandidaten


# ---------------------------------------------------------------- Quelle: manuell

def from_manual(source, opts):
    """Direkte URL, nichts wird recherchiert."""
    name = Path(urllib.parse.urlparse(source).path).name or "bild"
    return [{
        "adapter": "manual",
        "herkunft": source,
        "download_url": source,
        "copyright": opts.get("copyright") or "",
        "lizenz": opts.get("lizenz") or (BILDZITAT if opts.get("zitat")
                                         else ""),
        "infourl": opts.get("infourl") or "",
        "quellseite": source,
        "quelle": opts.get("quelle") or source,
        "credit": opts.get("credit") or "",
        "fremdbeschreibung": "",
        "vorschlagsname": urllib.parse.unquote(name).lower(),
        "warnungen": [] if (opts.get("lizenz") or opts.get("zitat")) else
                     ["keine Recherche möglich, Feld 'Bed. f. Rechtenutzung' "
                      "bleibt leer"],
    }]


def resolve(source, opts):
    if opts.get("manual"):
        return from_manual(source, opts)
    host = urllib.parse.urlparse(source).netloc.lower()
    if "demozoo.org" in host:
        return from_demozoo(source, opts)
    if "wikimedia.org" in host or "wikipedia.org" in host \
            or not host:  # nackter 'File:Name.png'
        return from_commons(source, opts)
    raise SystemExit(f"FEHLER: für {host!r} gibt es keine Recherche. "
                     "Mit --manual laden und Rechtefelder selbst setzen.")


# ------------------------------------------------------------------- Schreibteil

def download(url, target):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as resp, target.open("wb") as out:
        shutil.copyfileobj(resp, out)
    return target


def write_metadata(path, titel, beschreibung, alt, copyright_, usage_terms, url,
                   quelle, credit):
    args = ["exiftool", "-charset", "iptc=UTF8", "-overwrite_original"]

    def add(tag, value):
        if value:
            args.append(f"-{tag}={value}")

    add("XMP-dc:Title", titel)
    add("XMP-dc:Description", beschreibung)
    add("XMP-iptcCore:AltTextAccessibility", alt or beschreibung)
    add("XMP-dc:Rights", copyright_)
    add("XMP-xmpRights:UsageTerms", usage_terms)
    add("XMP-xmpRights:WebStatement", url)
    add("XMP-photoshop:Source", quelle)
    add("XMP-photoshop:Credit", credit)

    if path.suffix.lower() in IPTC_CAPABLE:
        args.append("-IPTC:CodedCharacterSet=UTF8")
        add("IPTC:ObjectName", titel)
        add("IPTC:Caption-Abstract", beschreibung)
        add("IPTC:CopyrightNotice", copyright_)
        add("EXIF:Copyright", copyright_)
        add("Photoshop:URL", url)
        # IPTC:Source und IPTC:Credit bewusst NICHT: der alte IIM-Block begrenzt
        # beide auf 32 Zeichen, jede Quell-URL wird darin stillschweigend
        # abgeschnitten ("https://commons.wikimedia.org/w/"). Eine kaputte URL
        # ist schlechter als keine, und XMP trägt die Werte unbegrenzt.

    args.append(str(path))
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"FEHLER exiftool: {result.stderr.strip()}")
    # exiftool meldet ignorierte Tags per Warning und Exit 0 -- nicht schlucken,
    # sonst fehlt ein Feld und niemand merkt es.
    if result.stderr.strip():
        print(f"  exiftool: {result.stderr.strip()}")


def target_name(item, kandidat, mehrere):
    if item.get("name"):
        return item["name"]
    if item.get("prefix"):
        prefix = item["prefix"]
        suffix = Path(kandidat["vorschlagsname"]).suffix
        stem = Path(kandidat["vorschlagsname"]).stem
        if mehrere:
            return f"{prefix.rstrip('_-')}_{stem}{suffix}"
        # Ein reiner Sammel-Prefix ("tracker_") ergibt als Einzelname nur einen
        # Torso -- dann den Namen aus der Quelle anhängen statt "tracker_.png".
        return f"{prefix}{stem}{suffix}" if prefix.endswith(("_", "-")) \
            else f"{prefix}{suffix}"
    return kandidat["vorschlagsname"]


def process(item, out_dir, dry_run):
    kandidaten = resolve(item["url"], item)
    mehrere = len(kandidaten) > 1

    for kandidat in kandidaten:
        target = out_dir / target_name(item, kandidat, mehrere)
        titel = item.get("titel")
        beschreibung = item.get("beschreibung")

        print(f"\n{kandidat['herkunft']}   [{kandidat['adapter']}]")
        print(f"  Ziel                  : {target}")
        print(f"  Titel                 : {titel or '(leer)'}")
        print(f"  Beschreibung          : {beschreibung or '(leer)'}")
        print(f"  Alt-Text              : {item.get('alt') or '(= Beschreibung)'}")
        print(f"  Copyright             : {kandidat['copyright'] or '(leer)'}")
        print(f"  Bed. f. Rechtenutzung : {kandidat['lizenz'] or '(leer)'}")
        print(f"  Copyright-Info-URL    : {kandidat['infourl'] or '(leer)'}")
        print(f"  Quelle                : {kandidat['quelle'] or '(leer)'}")
        print(f"  Credit                : {kandidat['credit'] or '(leer)'}")
        if kandidat["fremdbeschreibung"]:
            print(f"  Quellen-Beschreibung  : {kandidat['fremdbeschreibung'][:160]}")
        for w in kandidat["warnungen"]:
            print(f"  ACHTUNG {w}")

        if dry_run:
            print("  -> dry-run, nichts geschrieben")
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        download(kandidat["download_url"], target)
        write_metadata(target, titel, beschreibung, item.get("alt"),
                       kandidat["copyright"], kandidat["lizenz"],
                       kandidat["infourl"], kandidat["quelle"],
                       kandidat["credit"])
        print(f"  -> geschrieben ({target.stat().st_size // 1024} kB)")


def main():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("url", nargs="?", help="Commons-URL, Demozoo-Production-URL "
                                         "oder direkte URL mit --manual")
    p.add_argument("--out", required=True, type=Path, help="Zielverzeichnis")
    p.add_argument("--name", help="Dateiname im Ziel")
    p.add_argument("--prefix", help="Dateiname-Prefix, Rest kommt aus der Quelle "
                                    "(z. B. demo_kefrens_desertdream)")
    p.add_argument("--titel", help="Lightroom-Feld 'Titel'")
    p.add_argument("--beschreibung", help="Bildunterschrift (IPTC-Inhalt)")
    p.add_argument("--alt", help="Alt-Text (default: gleich der Beschreibung)")
    p.add_argument("--copyright", help="überschreibt die recherchierte Autor-Zeile")
    p.add_argument("--lizenz", help="überschreibt 'Bed. f. Rechtenutzung'")
    p.add_argument("--zitat", action="store_true",
                   help=f"Nutzung als Bildzitat: setzt die Rechtenutzung auf "
                        f"{BILDZITAT!r} statt auf den Ungeklärt-Marker")
    p.add_argument("--infourl", help="überschreibt 'Copyright-Info-URL'")
    p.add_argument("--quelle", help="überschreibt das Feld 'Quelle'")
    p.add_argument("--credit", help="überschreibt das Feld 'Credit'")
    p.add_argument("--screenshots", default="1",
                   help="Demozoo: welche Screenshots, z. B. '1-4' oder '1,3,7'")
    p.add_argument("--manual", action="store_true",
                   help="nichts recherchieren, Rechtefelder kommen per Flag")
    p.add_argument("--url-mode", choices=["license", "commons"], default="license",
                   help="Commons: Lizenz-URL oder Dateiseite als Copyright-Info-URL")
    p.add_argument("--batch", type=Path, help="JSON-Liste statt Einzel-URL")
    p.add_argument("--dry-run", action="store_true",
                   help="nur zeigen, was geschrieben würde")
    args = p.parse_args()

    if not shutil.which("exiftool"):
        raise SystemExit("FEHLER: exiftool nicht gefunden (brew install exiftool)")

    if args.batch:
        items = json.loads(args.batch.read_text(encoding="utf-8"))
    elif args.url:
        items = [{"url": args.url, "name": args.name, "prefix": args.prefix,
                  "titel": args.titel, "beschreibung": args.beschreibung,
                  "alt": args.alt, "copyright": args.copyright,
                  "lizenz": args.lizenz, "zitat": args.zitat,
                  "infourl": args.infourl, "quelle": args.quelle,
                  "credit": args.credit, "screenshots": args.screenshots,
                  "manual": args.manual, "url_mode": args.url_mode}]
    else:
        p.error("entweder eine URL oder --batch angeben")

    for item in items:
        process({k: v for k, v in item.items() if v}, args.out, args.dry_run)


if __name__ == "__main__":
    main()
