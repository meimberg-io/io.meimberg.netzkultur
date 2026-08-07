#!/usr/bin/env python3
"""Prueft die Kontext-Architektur des Repos.

Jede Datei unter rules/, knowledge/, material/ und state/ ist ein Kontext-Objekt und traegt
einen Vertrag im Frontmatter: welche Rolle sie hat, wer sie laedt, wann, ganz oder per
Abfrage, und ob blinde Pruef-Agenten sie sehen duerfen. Dieses Skript haelt den Vertrag ein.

Geprueft wird:

1. Vertrag vorhanden und vollstaendig (role, readers, when, mode, agent-visible).
2. Rolle passt zum Verzeichnis. Das Verzeichnis IST die Rolle; eine Regel in knowledge/
   wird nicht gelesen, wenn sie gelesen werden muesste.
3. Ladeverhalten passt zur Rolle: Regeln werden ganz gelesen und bleiben unter MAX_RULE
   Zeichen. Wissen, Material und Stand wachsen unbegrenzt und werden nur abgefragt.
4. Leserliste stimmt in BEIDE Richtungen:
   - jeder eingetragene Leser existiert und referenziert die Datei auch,
   - und jeder Skill/Agent, der die Datei referenziert, steht als Leser drin ("!name",
     wenn die Nennung ein Verbot ist).
   Ohne die zweite Richtung waechst die Verdrahtung still an der Deklaration vorbei.
5. Kein toter Verweis, weder aus einem Lader noch aus einer Kontextdatei heraus.
6. Hinweise: nicht ersetzte {{PLATZHALTER}} (nur dort, wo beim Aufsetzen etwas einzutragen
   ist) und dieselbe Ueberschrift in zwei Regeldateien oder in CLAUDE.md.

Exit 1, wenn etwas nicht stimmt.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Verzeichnis -> erlaubte Rolle. Das Verzeichnis ist die Rolle, nicht nur ihr Aufbewahrungsort.
DIR_ROLE = {
    "rules": "rule",           # normativ, wird ganz gelesen, bevor gehandelt wird
    "knowledge": "knowledge",  # gepruefte Fakten, schlaegt Modellwissen, wird durchsucht
    "material": "material",    # Rohstoff und Belege, wird durchsucht
    "state": "state",          # Beschlusslage und offene Punkte, punktuell gelesen
}
LOADER_DIRS = [".claude/skills", ".claude/agents", ".claude/commands"]
REQUIRED = ["role", "readers", "when", "mode", "agent-visible"]
MODES = {"full", "lookup"}
VISIBILITY = {"yes", "no"}
MAX_RULE = 4000  # Zeichen, nicht Zeilen: gemessen wird der Kontext, den eine Regel kostet

# Leser ohne eigene Datei: die Hauptsession und der Mensch.
READERS_WITHOUT_FILE = {"claude", "oli"}

# Dateien, die es pro Kapitel gibt und die in den Ladern als Muster stehen.
NUMBERED = [
    (re.compile(r"^material/dossier-\d+\.md$"), "material/dossier-<NN>.md"),
    (re.compile(r"^state/issues-\d+\.md$"), "state/issues-<NN>.md"),
]

# Nur hier ist ein offener Platzhalter ein Befund: Diese Dateien muessen beim Aufsetzen
# ausgefuellt werden. In den wachsenden Ablagen sind {{...}} Musterzeilen und bleiben stehen,
# bis der erste echte Eintrag sie ersetzt.
PLACEHOLDER_DIRS = {"rules"}

PATH_IN_TEXT = re.compile(
    r"(?<![\w/-])(?:\.\./)?(?:rules|knowledge|material|state|manuscript|assets|scripts|beispiel)/[\w./<>-]+"
    r"\.(?:md|py|js|json)"
)


def frontmatter(path):
    """Gibt das Frontmatter als dict zurueck, oder None wenn keins da ist."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def loaders():
    """Alle Skills, Agenten und Commands mit ihrem Volltext."""
    found = defaultdict(list)
    for directory in LOADER_DIRS:
        for path in (REPO / directory).rglob("*.md"):
            name = path.parent.name if path.name == "SKILL.md" else path.stem
            found[name].append(path)
    return found


def context_files():
    files = []
    for directory in DIR_ROLE:
        files.extend(sorted((REPO / directory).glob("*.md")))
    return files


def name_variants(rel):
    """Wie eine Datei in einem Lader stehen darf: konkret oder als <NN>-Muster."""
    variants = [str(rel)]
    for pattern, generic in NUMBERED:
        if pattern.match(str(rel)):
            variants.append(generic)
    return variants


def check_contract(path, rel, fm, errors):
    missing = [f for f in REQUIRED if f not in fm]
    if missing:
        errors.append(f"{rel}: Vertrag unvollstaendig, fehlt: {', '.join(missing)}")
        return False

    expected = DIR_ROLE[rel.parts[0]]
    if fm["role"] != expected:
        errors.append(
            f"{rel}: role '{fm['role']}' passt nicht zu {rel.parts[0]}/, erwartet '{expected}'. "
            "Entweder die Rolle korrigieren oder die Datei verschieben."
        )
    if fm["mode"] not in MODES:
        errors.append(f"{rel}: mode '{fm['mode']}' unbekannt, erlaubt: {sorted(MODES)}")
    if fm["agent-visible"] not in VISIBILITY:
        errors.append(f"{rel}: agent-visible '{fm['agent-visible']}' unbekannt, erlaubt: yes, no")
    if not fm["readers"].strip():
        errors.append(
            f"{rel}: kein Leser eingetragen. Eine Kontextdatei, die niemand laedt, wirkt nicht."
        )

    if fm["role"] == "rule":
        if fm["mode"] != "full":
            errors.append(f"{rel}: role=rule verlangt mode=full")
        # Zitierte Klangproben zaehlen nicht mit. Die Grenze schuetzt vor Anweisungs-
        # Wucher; eine Probe ist keine Anweisung, und zu wenige Proben erzeugen
        # gleichfoermige Texte. Wer sie mitzaehlt, optimiert in die falsche Richtung.
        anweisung = "\n".join(
            l for l in path.read_text(encoding="utf-8").splitlines()
            if not l.lstrip().startswith(">")
        )
        if len(anweisung) > MAX_RULE:
            errors.append(
                f"{rel}: {len(anweisung)} Zeichen Anweisung, erlaubt sind {MAX_RULE} "
                "(Zitate zaehlen nicht). Was nicht hineinpasst, ist keine Regel, sondern Wissen."
            )
    elif fm["mode"] != "lookup":
        errors.append(
            f"{rel}: role={fm['role']} verlangt mode=lookup. Diese Ablagen wachsen; "
            "wer sie ganz laedt, sprengt frueher oder spaeter den Kontext."
        )
    return True


def parse_readers(value):
    """readers: a, b, !c  ->  ({a, b}, {c}).

    Ein '!' davor heisst: Dieser Lader nennt die Datei ausdruecklich, um sie zu verbieten
    ("sieh da nicht hinein"). Das ist Verdrahtung wie jede andere und gehoert deklariert,
    sonst meldet der Rueckwaerts-Check sie ewig als Luecke.
    """
    plain, forbidden = set(), set()
    for entry in (n.strip() for n in value.split(",")):
        if not entry:
            continue
        (forbidden if entry.startswith("!") else plain).add(entry.lstrip("!"))
    return plain, forbidden


def check_readers(rel, fm, all_loaders, reader_texts, errors, hints):
    """Beide Richtungen: deklarierte Leser laden wirklich, ladende Leser sind deklariert."""
    variants = name_variants(rel)
    plain, forbidden = parse_readers(fm["readers"])

    for name in plain | forbidden:
        if name in READERS_WITHOUT_FILE:
            continue
        if name not in all_loaders:
            errors.append(f"{rel}: Leser '{name}' existiert nicht in .claude/")
        elif name in plain and not any(v in reader_texts.get(name, "") for v in variants):
            errors.append(
                f"{rel}: '{name}' ist als Leser eingetragen, laedt die Datei aber nicht. "
                "Entweder dort referenzieren oder hier austragen."
            )

    for name, text in reader_texts.items():
        if name in plain or name in forbidden or not any(v in text for v in variants):
            continue
        meldung = (
            f"{rel}: '{name}' referenziert die Datei, steht aber nicht in readers. "
            "Eintragen, oder als '!{name}' fuehren, wenn die Nennung ein Verbot ist."
        ).replace("{name}", name)
        # Bei agent-visible: no kann die Nennung ein Verbot sein, das ist ein Urteil.
        (hints if fm["agent-visible"] == "no" else errors).append(meldung)


def check_dead_links(loader_texts, context, errors):
    """Tote Pfade, aus Ladern und aus Kontextdateien heraus."""
    sources = [(f".claude/…/{name}", REPO, text) for name, text in loader_texts.items()]
    sources += [
        (str(p.relative_to(REPO)), p.parent, p.read_text(encoding="utf-8")) for p in context
    ]
    for label, base, text in sources:
        for hit in sorted(set(PATH_IN_TEXT.findall(text))):
            if "<" in hit:  # Muster wie dossier-<NN>.md
                continue
            target = (base / hit).resolve() if hit.startswith("../") else (REPO / hit)
            if not target.exists():
                errors.append(f"{label}: verweist auf '{hit}', das es nicht gibt")


def check_duplicate_headings(context, hints):
    """Dieselbe H2 in zwei Regeldateien heisst: ein Thema, zwei Heimaten.

    CLAUDE.md zaehlt mit. Sie wird immer geladen und zieht deshalb Inhalt an, der
    laengst in rules/ steht; die zweite Fassung ist die, die zuerst veraltet.
    """
    seen = defaultdict(list)
    candidates = [p for p in context if p.parent.name == "rules"]
    if (REPO / "CLAUDE.md").exists():
        candidates.append(REPO / "CLAUDE.md")
    for path in candidates:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                seen[line[3:].strip().lower()].append(path.name)
    for heading, where in sorted(seen.items()):
        if len(where) > 1:
            hints.append(
                f"Ueberschrift '{heading}' steht in {', '.join(where)}. "
                "Eine Sache, eine Heimat, sonst laufen die Fassungen auseinander."
            )


def main():
    errors, hints = [], []
    all_loaders = loaders()
    loader_texts = {
        name: "\n".join(p.read_text(encoding="utf-8") for p in paths)
        for name, paths in all_loaders.items()
    }
    # Commands sind Aufrufe, keine Lader. Sie duerfen Pfade nennen, ohne Leser zu sein,
    # und werden deshalb nur auf tote Verweise geprueft.
    commands = REPO / ".claude" / "commands"
    reader_texts = {
        name: "\n".join(
            p.read_text(encoding="utf-8") for p in paths if commands not in p.parents
        )
        for name, paths in all_loaders.items()
    }

    context = context_files()
    for path in context:
        rel = path.relative_to(REPO)
        fm = frontmatter(path)

        if fm is None:
            errors.append(f"{rel}: kein Vertrag im Frontmatter. Verdrahten oder loeschen.")
            continue
        if not check_contract(path, rel, fm, errors):
            continue
        check_readers(rel, fm, all_loaders, reader_texts, errors, hints)

    for path in list(context) + [REPO / "CLAUDE.md"]:
        if path.exists() and "{{" in path.read_text(encoding="utf-8"):
            rel = path.relative_to(REPO)
            if rel.parts[0] in PLACEHOLDER_DIRS or rel.name == "CLAUDE.md":
                hints.append(f"{rel}: noch nicht ausgefuellt, enthaelt {{{{PLATZHALTER}}}}.")

    check_dead_links(loader_texts, context, errors)
    check_duplicate_headings(context, hints)

    for line in hints:
        print(f"hinweis  {line}")
    for line in errors:
        print(f"FEHLER   {line}")

    if errors:
        print(f"\n{len(errors)} Fehler.")
        return 1
    print(f"\nKontext-Architektur in Ordnung ({len(context)} Objekte, {len(hints)} Hinweise).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
