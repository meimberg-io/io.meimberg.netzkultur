# Export des Manuskripts nach Storyblok

*Datum: 2026-09-27 · Status: abgestimmt, bereit für den Umsetzungsplan*

## Ausgangslage und Ziel

Das Buch erscheint auf meimberg.io als Special unter `/s/netzkultur`. Das Frontend dafür steht in `io.meimberg.www` (Konzept: `docs/superpowers/specs/2026-07-27-special-longread-design.md` dort). In Storyblok (Space 330326, Ordner `s/netzkultur`) liegen eine `special`-Story und sieben `specialchapter`-Stories, alle unveröffentlicht, IDs in `state/publikation.md`.

Deren Inhalt stammt aus einer einmaligen Handübertragung der Gemini-Entwürfe vom 2026-07-30 und hat mit dem heutigen Manuskript wenig zu tun. Einen wiederholbaren Weg vom Manuskript nach Storyblok gibt es nicht.

Ziel ist ein Skript, das den Stand von `manuscript/` jederzeit und immer gleich nach Storyblok überträgt, einschließlich der Bilder und ihrer Nachweise.

## Entscheidungen

| Frage | Entscheidung |
|---|---|
| Was gilt, wenn Storyblok und Manuskript sich unterscheiden | Das Manuskript gewinnt. `body` wird bei jedem Lauf vollständig neu erzeugt, von Hand in Storyblok eingefügte Blöcke gehen verloren. |
| Welche Felder das Skript schreibt | `body`, Story-Name, `pagetitle`. Sonst nichts. Die Reihenfolge im Ordner prüft es nur. |
| Welche Felder es nie anfasst | Slug bestehender Stories, `headerpicture`, `teasertitle`, `teaserimage`, `abstract`, `readmoretext`, `pageintro`, `date`. Die werden in Storyblok gepflegt. |
| Veröffentlichen | Standard ist Entwurf. Mit `--publish` veröffentlicht das Skript die Stories, die es geschrieben hat. |
| Bilder | Werden als Assets hochgeladen, mit Alt-Text, Bildunterschrift und Nachweis aus dem XMP der Datei. |
| Nachweis auf der Website | `Picture.tsx` in `io.meimberg.www` zeigt Bildunterschrift und Quelle an und setzt den Alt-Text. |
| Ort und Sprache | Python-Skript `scripts/storyblok-export.py` in diesem Repo, neben `kompilieren.py`. Direkt gegen die Storyblok Management API, kein Umweg über den Content Manager oder einen Agenten. |

## Aufruf

```bash
python3 scripts/storyblok-export.py [--kapitel N] [--trocken] [--publish] [--bilder-ersetzen]
```

| Schalter | Wirkung |
|---|---|
| ohne | alle Teile aus `manuscript/Index.md` als Entwurf schreiben |
| `--kapitel N` | nur Teil N (`0` ist der Vorspann, `1` bis `7` die Kapitel); Zählung wie bei `kompilieren.py` |
| `--trocken` | vollständig prüfen und ausgeben, was angelegt, geändert oder hochgeladen würde; keine schreibende Anfrage |
| `--publish` | die geschriebenen Stories zusätzlich veröffentlichen |
| `--bilder-ersetzen` | Dateien bereits vorhandener Assets neu hochladen statt nur ihre Metadaten abzugleichen |

**Zugang.** Der Token kommt aus der Umgebungsvariable `STORYBLOK_MANAGEMENT_TOKEN`, ersatzweise aus einer `.env` im Repo-Wurzelverzeichnis. `.env` kommt in `.gitignore`. Space-ID `330326` und der Ordner `s/netzkultur` stehen als Konstanten im Skript. Die API liegt unter `https://mapi.storyblok.com/v1/`.

Abhängigkeiten: `pyyaml` (braucht `kompilieren.py` schon) und `exiftool` (braucht `bild-einziehen.py` schon). HTTP über die Standardbibliothek.

## Quelle: das Manuskript

`manuscript/Index.md` ist die einzige Wahrheit für Zugehörigkeit und Reihenfolge. Das Skript liest ihn genauso wie `kompilieren.py` (`read_index`, `flatten`, `chapters`, `PREFIX`, `FRONTMATTER`). Diese Funktionen wandern dafür in ein gemeinsames Modul `scripts/manuscript_index.py`, das beide Skripte importieren. Doppelter Parser-Code würde bei der nächsten Änderung an Longform auseinanderlaufen.

Ein Teil besteht aus der Datei des Hauptkapitels (Ebene 1, z. B. `01 - Bevor das Internet ein öffentlicher Ort war.md`) und seinen Szenen (Ebene 2). Das Frontmatter (`status`, `comment`) wird entfernt. Der Szenenstatus spielt für den Export keine Rolle, es wird übertragen, was im Index steht.

Im Manuskript vorkommende Markdown-Elemente, und nur diese muss der Konverter können:

| Markdown | Storyblok-Richtext |
|---|---|
| Absatz | `paragraph` |
| `###`, `####` | `heading` mit `level` 3 bzw. 4 |
| `**fett**` | Mark `bold` |
| `*kursiv*`, `_kursiv_` | Mark `italic` |
| `` `code` `` | Mark `code` |
| `- ` / `* ` Aufzählung | `bullet_list` → `list_item` → `paragraph` |
| `1. ` Aufzählung | `ordered_list` → `list_item` → `paragraph` |
| `> ` Zitat | `blockquote` → `paragraph` |
| ```` ``` ```` Codeblock, optional mit Sprache | `code_block`, Zeilen unverändert, Sprache als `attrs.class` `language-…` |
| `> [!…]` Obsidian-Callout | wird übersprungen, Redaktionsnotiz |
| `> **[BILD-MARKER …]**` | wird übersprungen und als offener Bildplatz gemeldet |
| eine Zeile mit genau einem `![[bild]]` | `picture`-Block, siehe unten |
| eine Zeile mit genau einem `![[video.mp4]]` (auch `.webm`, `.ogv`) | `video`-Block |
| eine Zeile mit mehreren `![[bild]]` | `gallery`-Block (Bildreihe) |

Ein Größenzusatz wie `![[bild.png|300]]` wird ignoriert. Alles andere (Tabelle, Fußnote, Link, Wiki-Link ohne `!`, HTML, `#`/`##` innerhalb einer Szene, ein Bild mitten im Absatz, ein Video in einer Bildreihe) ist ein Fehler mit Datei und Zeile. Stillschweigend verschluckter Text wäre schlimmer als ein Abbruch.

## Ziel: Zuordnung zu Stories

Das Skript liest zuerst alle Stories unter `s/netzkultur/`.

- **Teil 0** (Vorspann) → die Story vom Typ `special`, Startpage des Ordners.
- **Teil N ≥ 1** → die `specialchapter`-Story, deren Slug mit der zweistelligen Nummer und Bindestrich beginnt (`01-`, `02-`, …). Die Nummer kommt aus dem Ordnungspräfix des Dateinamens.
- **Keine passende Story** → neu anlegen, Typ `specialchapter`, Slug aus dem Dateinamen: Nummer, Titel kleingeschrieben, Umlaute ausgeschrieben (`ä` → `ae`, `ß` → `ss`), alles andere außer `a-z0-9` zu Bindestrichen zusammengezogen. Ergibt für die bestehenden Kapitel exakt deren heutige Slugs.
- **Mehr als eine passende Story** → Abbruch vor jedem Schreiben.
- **Story ohne Gegenstück im Manuskript** → bleibt unangetastet, wird gemeldet.

Der Slug einer bestehenden Story wird nie geändert, auch wenn sich der Kapiteltitel ändert. Sonst brechen URLs.

**Name und `pagetitle`** werden bei jedem Lauf gesetzt: Teil 0 bekommt den Titel ohne Präfix, Teil N `Kapitel N: <Titel>`. Das entspricht der heutigen Benennung in Storyblok und der Nummerierung im Longform-Compile.

**Reihenfolge.** Das Frontend sortiert nach `position` (`sort_by: position:asc`). Die Management API dokumentiert keinen Endpunkt zum Umsortieren, deshalb setzt das Skript die Reihenfolge nicht selbst. Es prüft nach einem vollständigen Lauf, ob die Kapitel im Ordner in der Nummernfolge stehen, und meldet eine Abweichung zur Korrektur per Drag-and-Drop. Heute stimmt die Reihenfolge; neue Kapitel landen am Ende, was bei angehängten Kapiteln ohnehin richtig ist.

## Body-Aufbau

Aus einem Teil entsteht eine Liste von Blöcken:

1. Der Text der Kapiteldatei selbst, falls vorhanden, als erster `richtext`-Block.
2. Pro Szene ein neuer `richtext`-Block, beginnend mit dem Szenentitel als `heading` Level 2 (Dateiname ohne Ordnungspräfix, wie im Compile-Step).
3. Jedes `![[bild]]` beendet den laufenden `richtext`-Block, erzeugt einen `picture`-Block und eröffnet danach einen neuen `richtext`-Block für den restlichen Text der Szene.

Leere `richtext`-Blöcke entstehen nicht. Jeder Block bekommt eine neue `_uid`. Stabile UIDs über Läufe hinweg sind nicht nötig, weil der Body vollständig ersetzt wird.

`picture`-Block: `image` mit dem Asset-Feld, `style` `normal`, `spacing` `default`.

`video`-Block: `file` mit dem Asset-Feld.

`gallery`-Block: `images` mit den Asset-Feldern in Zeilenfolge, `columns` die Zahl der Bilder, höchstens `3`, `layout` `default`.

Das Asset-Feld im Block trägt `alt`, `title`, `copyright` und `source` als Kopie, weil das Frontend sie dort liest und nicht am Asset selbst.

## Bilder

**Datei finden.** `![[name.ext]]` wird unter `assets/` rekursiv gesucht. Keine Datei oder mehrere Dateien gleichen Namens → Fehler.

**Metadaten lesen** per `exiftool -j`:

| XMP-Feld | Storyblok-Asset-Feld |
|---|---|
| `XMP-iptcCore:AltTextAccessibility` | `alt` |
| `XMP-dc:Description` | `title` (dient als Bildunterschrift) |
| `XMP-dc:Rights`, `XMP-xmpRights:UsageTerms` | `copyright`, als `Rights · UsageTerms` |
| `XMP-photoshop:Source` | `source` |

**Prüfung vor jedem Upload.** Abbruch, wenn:
- `UsageTerms` leer ist oder „ungeklärt“ enthält. `bild-einziehen.py` lässt das Feld ohne `--zitat` bei Quellen ohne Lizenz leer, eine leere Rechtenutzung heißt also: nicht entschieden (siehe `rules/bilder.md`),
- Alt-Text oder `Rights` fehlen.

Das gilt für Videos genauso. Stand heute scheitern daran `c64.png` und `tracker.mp4`, beide ohne Rechteangaben im XMP.

Ein Bild ohne geklärte Rechte oder ohne Nachweis darf nicht nach Storyblok, auch nicht als Entwurf.

**Hochladen.** Die Assets liegen in einem Asset-Ordner `netzkultur`, den das Skript bei Bedarf anlegt. Ein Asset mit gleichem Dateinamen in diesem Ordner wird wiederverwendet. Seine Metadaten gleicht das Skript bei jedem Lauf mit dem XMP ab, die Datei selbst ersetzt es nur mit `--bilder-ersetzen`. Neue Dateien laufen über den signierten Upload der Management API (Anfrage, Upload auf die zurückgegebene URL, Abschluss).

## Ablauf und Fehlerverhalten

1. **Einlesen und prüfen, ohne Netz:** Index, alle Szenendateien, Markdown-Konvertierung, alle Bilder samt Metadaten. Jeder Fehler wird gesammelt, am Ende gemeinsam ausgegeben, dann Abbruch.
2. **Storyblok lesen:** Stories im Ordner, Asset-Ordner, vorhandene Assets. Zuordnung prüfen.
3. Bei `--trocken`: Bericht ausgeben, Ende.
4. **Schreiben:** Assets hochladen bzw. abgleichen, dann Story für Story `body`, Name und `pagetitle` setzen, bei `--publish` mit Veröffentlichung. Eine Story, deren Inhalt sich nicht geändert hat, wird ohne `--publish` übersprungen.
5. **Bericht:** je Story angelegt, geändert oder unverändert, Zahl der Blöcke, Link in den Storyblok-Editor; bei vollständigem Lauf dazu verwaiste Stories und eine abweichende Reihenfolge.

Das Skript bleibt unter dem Rate-Limit der Management API (höchstens drei Anfragen pro Sekunde) und wiederholt bei HTTP 429 mit Pause. Jeder andere HTTP-Fehler bricht ab und nennt die Story oder das Asset, an dem es scheiterte, und die Antwort der API. Da jede Story für sich vollständig geschrieben wird, ist ein erneuter Lauf nach einem Abbruch unbedenklich.

## Änderung in `io.meimberg.www`

`src/components/elements/Picture.tsx` setzt heute `alt=""` und zeigt keinen Nachweis, `Gallery.tsx` und `Video.tsx` ebenso. Die Bildzitate der Demoszene stehen fast alle in Bildreihen, der Nachweis muss also auch dort erscheinen. Neu:

- `alt` aus `blok.image.alt`
- darunter eine `figcaption` mit `blok.image.title`, gefolgt vom Nachweis aus `blok.image.copyright`, verlinkt auf `blok.image.source`, falls vorhanden
- ohne `title` und `copyright` keine `figcaption`, damit bestehende Bilder im Blog sich nicht verändern
- `Gallery.tsx`: `alt` je Bild aus dem Asset, unter der Reihe die Nachweise aller Bilder, gleiche Nachweise zusammengefasst
- `Video.tsx`: Nachweis unter dem Player
- eine gemeinsame Komponente `AssetCredit` rendert den Nachweis für alle drei
- `Gallery.tsx` baut die Spaltenklassen heute per String-Verkettung (`'md:grid-cols-' + blok.columns`), die Tailwind nicht sicher erkennt; sie werden auf eine feste Zuordnung für 1 bis 4 Spalten umgestellt

Ein Schemawechsel in Storyblok ist nicht nötig, die Felder gehören zum Asset. Die Änderung ist ein eigener Commit im Website-Repo und muss live sein, bevor das Special mit `--publish` veröffentlicht wird.

## Pflege in diesem Repo

- `rules/werkzeuge.md`, Abschnitt Skripte: ein Absatz zu `storyblok-export.py` und dem Verweis auf diese Spec.
- `state/publikation.md`: Hinweis, dass die Stories ab jetzt aus dem Manuskript erzeugt werden und die Handübertragung vom Juli überholt ist.
- `.gitignore`: `.env`.

## Tests

Unittests ohne Netz in `scripts/test_storyblok_export.py`, lauffähig mit `python3 -m unittest`:

- Konverter: jedes Element der Tabelle oben einzeln, verschachtelte Marks, Liste mit fettem Eintrag, und je ein Fehlerfall (Tabelle, Link, `##` in einer Szene).
- Body-Aufbau: Kapitel mit Vorspann, zwei Szenen und einem Bild mitten in einer Szene ergibt die erwartete Blockfolge.
- Slug-Bildung: ergibt für alle acht heutigen Kapitelnamen exakt die heutigen Slugs.
- Zuordnung: passende Story, fehlende Story, doppelte Story.
- Bildprüfung: leere Rechtenutzung, „ungeklärt“ und fehlender Alt-Text führen zum Fehler.
- Bildreihe, Video, Callout, BILD-MARKER.

Danach von Hand:

1. `--trocken` über das ganze Buch. Erwartet zuerst: Abbruch mit `c64.png` und `tracker.mp4`. Sind deren Rechte eingetragen: keine Fehler, acht Stories „ändern", keine „anlegen", 18 offene Bildplätze als Hinweis.
2. `--kapitel 1` als Entwurf. In der Storyblok-Vorschau prüfen: Szenentitel als H2, Bilder an der richtigen Stelle mit Unterschrift und Nachweis, Kapitelleiste und Verzeichnis unverändert.
3. Zweiter Lauf `--kapitel 1` ohne Änderung am Manuskript: kein neues Asset, gleicher Inhalt.
4. Ganzes Buch als Entwurf.

## Bewusst nicht Teil davon

- Rücksync von Storyblok ins Manuskript
- Befüllen von `abstract`, `pageintro` oder Teaserfeldern aus dem Manuskript
- Löschen verwaister Stories oder Assets
- Bildgrößen oder Stile pro Bild aus dem Manuskript steuern
- Auslösen durch Hook oder CI; das Skript wird von Hand aufgerufen
