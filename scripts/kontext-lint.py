#!/usr/bin/env python3
"""Prueft die Kontext-Architektur des Repos.

Jede Datei unter rules/, memory/, research/ und notes/ ist ein Kontext-Objekt und traegt
einen Vertrag im Frontmatter: wer sie laedt, wann, ganz oder per Abfrage, und ob blinde
Pruef-Agenten sie sehen duerfen. Dieses Skript haelt den Vertrag ein.

Geprueft wird:

1. Vertrag vorhanden und vollstaendig (rolle, liest, wann, modus, agentensichtbar).
2. Kein verwaistes Objekt: jeder genannte Leser existiert als Skill oder Agent,
   und die Datei wird dort auch tatsaechlich referenziert. Genau so ist digest.md
   neun Monate lang unbemerkt tot gewesen.
3. Kein toter Verweis: jeder Pfad, den ein Skill, Agent oder Command nennt, existiert.
4. Regeln bleiben lesbar: rolle=regel heisst modus=ganz und hoechstens MAX_REGEL Zeilen.
   Eine Regeldatei, die man nicht am Stueck liest, wird ueberflogen.

Exit 1, wenn etwas nicht stimmt.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KONTEXT_DIRS = ["rules", "memory", "research", "notes"]
LADER_DIRS = [".claude/skills", ".claude/agents", ".claude/commands"]
PFLICHTFELDER = ["rolle", "liest", "wann", "modus", "agentensichtbar"]
ROLLEN = {"regel", "wissen", "material", "stand"}
MODI = {"ganz", "abfrage"}
MAX_REGEL = 150

# "claude" und "oli" sind Leser ohne eigene Datei: die Hauptsession und der Mensch.
LESER_OHNE_DATEI = {"claude", "oli"}


def frontmatter(pfad):
    """Gibt das Frontmatter als dict zurueck, oder None wenn keins da ist."""
    text = pfad.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    ende = text.find("\n---\n", 4)
    if ende == -1:
        return None
    felder = {}
    for zeile in text[4:ende].splitlines():
        if ":" not in zeile:
            continue
        schluessel, wert = zeile.split(":", 1)
        felder[schluessel.strip()] = wert.strip()
    return felder


def lader():
    """Alle Skills, Agenten und Commands mit ihrem Volltext."""
    gefunden = {}
    for verzeichnis in LADER_DIRS:
        for pfad in (REPO / verzeichnis).rglob("*.md"):
            name = pfad.parent.name if pfad.name == "SKILL.md" else pfad.stem
            gefunden.setdefault(name, []).append(pfad)
    return gefunden


def main():
    fehler = []
    warnungen = []
    alle_lader = lader()
    ladertexte = {
        name: "\n".join(p.read_text(encoding="utf-8") for p in pfade)
        for name, pfade in alle_lader.items()
    }

    kontextdateien = []
    for verzeichnis in KONTEXT_DIRS:
        kontextdateien.extend(sorted((REPO / verzeichnis).glob("*.md")))

    for pfad in kontextdateien:
        rel = pfad.relative_to(REPO)
        fm = frontmatter(pfad)

        if fm is None:
            fehler.append(f"{rel}: kein Vertrag im Frontmatter. Verdrahten oder loeschen.")
            continue

        fehlend = [f for f in PFLICHTFELDER if f not in fm]
        if fehlend:
            fehler.append(f"{rel}: Vertrag unvollstaendig, fehlt: {', '.join(fehlend)}")
            continue

        if fm["rolle"] not in ROLLEN:
            fehler.append(f"{rel}: rolle '{fm['rolle']}' unbekannt, erlaubt: {sorted(ROLLEN)}")
        if fm["modus"] not in MODI:
            fehler.append(f"{rel}: modus '{fm['modus']}' unbekannt, erlaubt: {sorted(MODI)}")

        if fm["rolle"] == "regel":
            if fm["modus"] != "ganz":
                fehler.append(f"{rel}: rolle=regel verlangt modus=ganz")
            zeilen = len(pfad.read_text(encoding="utf-8").splitlines())
            if zeilen > MAX_REGEL:
                fehler.append(
                    f"{rel}: {zeilen} Zeilen, erlaubt sind {MAX_REGEL}. "
                    "Was nicht hineinpasst, ist keine Regel, sondern Wissen."
                )

        leser = [n.strip() for n in fm["liest"].split(",") if n.strip()]
        for name in leser:
            if name in LESER_OHNE_DATEI:
                continue
            # Kapitel-Dossiers werden in den Skills als Muster referenziert, nicht einzeln.
            varianten = [str(rel)]
            if rel.parent.name == "research" and rel.stem.isdigit():
                varianten.append("research/<NN>.md")

            if name not in alle_lader:
                fehler.append(f"{rel}: Leser '{name}' existiert nicht in .claude/")
            elif not any(v in ladertexte[name] for v in varianten):
                fehler.append(
                    f"{rel}: '{name}' ist als Leser eingetragen, laedt die Datei aber nicht. "
                    "Entweder dort referenzieren oder hier austragen."
                )

    # Tote Verweise aus den Ladern heraus.
    verweis = re.compile(r"(?:rules|memory|research|notes|sources|scripts)/[\w./-]+\.(?:md|py|js)")
    for name, text in ladertexte.items():
        for treffer in sorted(set(verweis.findall(text))):
            if not (REPO / treffer).exists():
                fehler.append(f".claude/…/{name}: verweist auf '{treffer}', das es nicht gibt")

    # Kontextdateien, die niemand als Leser nennt, sind tot; nur ein Hinweis, kein Fehler,
    # weil manches bewusst nur von Oli gelesen wird.
    for pfad in kontextdateien:
        fm = frontmatter(pfad)
        if fm and fm.get("liest", "").strip() in LESER_OHNE_DATEI:
            warnungen.append(
                f"{pfad.relative_to(REPO)}: wird nur von der Hauptsession gelesen, "
                "kein Skill laedt sie deterministisch."
            )

    for zeile in warnungen:
        print(f"hinweis  {zeile}")
    for zeile in fehler:
        print(f"FEHLER   {zeile}")

    if fehler:
        print(f"\n{len(fehler)} Fehler.")
        return 1
    print(f"\nKontext-Architektur in Ordnung ({len(kontextdateien)} Objekte).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
