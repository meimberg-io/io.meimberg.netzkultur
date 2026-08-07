#!/usr/bin/env python3
"""Szenen aus manuscript/Index.md zu Prueftexten zusammensetzen.

Longform kompiliert immer den ganzen Draft. Die Kohaerenzpruefung braucht aber
kleinere und andere Zuschnitte, deshalb dieses Skript. Es liest die Reihenfolge
und die Verschachtelung aus `Index.md` (der einzigen Wahrheit darueber), setzt
die Ueberschriften aus Dateinamen und Einrueckungstiefe zusammen und schneidet
Ordnungspraefixe wie "2.03 - " genauso weg wie der Compile-Step.

Die drei Zuschnitte entsprechen den drei Pruefebenen:

    --kapitel N     ein Kapitel vollstaendig       -> kohaerenz, plausibilitaet
    --naht N        Ende von Kapitel N + Anfang N+1 -> Anschluss ueber Kapitelgrenzen
    --abriss        Ueberschriftenbaum, je zwei Saetze -> Dopplungen ueber Distanz

Ohne Argument kommt das ganze Buch. Ausgabe nach stdout oder --out.

Beispiele:
    scripts/kompilieren.py --kapitel 1
    scripts/kompilieren.py --naht 1 --out /tmp/naht-1-2.md
    scripts/kompilieren.py --abriss
"""

import argparse
import pathlib
import re
import sys

PREFIX = re.compile(r"^\d+(?:\.\d+)*\s*[-–—]\s*")
FRONTMATTER = re.compile(r"^---\n.*?\n---\n+", re.S)


def read_index(project):
    text = (project / "Index.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        sys.exit(f"{project / 'Index.md'}: kein Frontmatter gefunden.")
    try:
        import yaml
    except ImportError:
        sys.exit("Braucht pyyaml: pip3 install pyyaml")
    data = yaml.safe_load(match.group(1))
    return data["longform"]["scenes"]


def flatten(items, level=1):
    """Liefert [(ebene, szenenname), ...] in Dokumentreihenfolge."""
    out = []
    for item in items:
        if isinstance(item, list):
            out += flatten(item, level + 1)
        else:
            out.append((level, str(item)))
    return out


def body_of(project, name):
    path = project / f"{name}.md"
    if not path.exists():
        return None
    return FRONTMATTER.sub("", path.read_text(encoding="utf-8")).strip("\n")


def heading(level, name):
    return "#" * level + " " + PREFIX.sub("", name)


def chapters(scenes):
    """Gruppiert zu [(elternname, [kindnamen]), ...] anhand der Ebene 1."""
    groups = []
    for level, name in scenes:
        if level == 1:
            groups.append((name, []))
        elif groups:
            groups[-1][1].append(name)
    return groups


def render(project, pairs, missing):
    parts = []
    for level, name in pairs:
        body = body_of(project, name)
        if body is None:
            missing.append(name)
            continue
        parts.append(heading(level, name) + "\n\n" + body)
    return "\n\n".join(parts) + "\n"


def pick_chapter(groups, wanted):
    """Kapitel per Nummer (1-basiert, ohne die Einleitung zu zaehlen) oder per Namensteil."""
    if wanted.isdigit():
        n = int(wanted)
        for name, kids in groups:
            # Numerisch vergleichen, damit 1, 01 und 001 dasselbe Kapitel treffen.
            fuehrend = re.match(r"^\s*(\d+)", name)
            if fuehrend and int(fuehrend.group(1)) == n:
                return name, kids
            if re.match(rf"^(Kapitel\s*)?{n}\b", PREFIX.sub("", name)):
                return name, kids
        sys.exit(f"Kapitel {n} nicht gefunden. Vorhanden:\n  "
                 + "\n  ".join(name for name, _ in groups))
    for name, kids in groups:
        if wanted.lower() in name.lower():
            return name, kids
    sys.exit(f"Kein Kapitel passt auf '{wanted}'.")


def first_sentences(text, count=2):
    plain = [l for l in text.split("\n") if l.strip() and not l.startswith(("!", ">", "|"))]
    if not plain:
        return "(kein Text)"
    sentences = re.split(r"(?<=[.!?])\s+", " ".join(plain))
    return " ".join(sentences[:count]).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--projekt", type=pathlib.Path, default=pathlib.Path("manuscript"))
    ap.add_argument("--kapitel", metavar="N|TEIL", help="ein Kapitel vollstaendig")
    ap.add_argument("--naht", type=int, metavar="N",
                    help="letzte Szene von Kapitel N plus erste von N+1")
    ap.add_argument("--abriss", action="store_true",
                    help="Ueberschriftenbaum mit je zwei Saetzen pro Szene")
    ap.add_argument("--out", type=pathlib.Path)
    args = ap.parse_args()

    scenes = flatten(read_index(args.projekt))
    groups = chapters(scenes)
    level_of = dict((name, level) for level, name in scenes)
    missing = []

    if args.abriss:
        lines = ["# Struktur-Abriss", ""]
        for level, name in scenes:
            body = body_of(args.projekt, name)
            if body is None:
                missing.append(name)
                continue
            lines.append(heading(level, name))
            lines.append("")
            lines.append(first_sentences(body))
            lines.append("")
        text = "\n".join(lines)

    elif args.naht is not None:
        a = pick_chapter(groups, str(args.naht))
        b = pick_chapter(groups, str(args.naht + 1))
        if not a[1] or not b[1]:
            sys.exit("Mindestens eines der beiden Kapitel hat keine Szenen.")
        tail, head = a[1][-1], b[1][0]
        text = (f"# Naht: Ende von „{PREFIX.sub('', a[0])}" + "“"
                f" zu Anfang von „{PREFIX.sub('', b[0])}" + "“\n\n"
                + render(args.projekt, [(level_of[tail], tail), (level_of[head], head)], missing))

    elif args.kapitel:
        name, kids = pick_chapter(groups, args.kapitel)
        pairs = [(level_of[name], name)] + [(level_of[k], k) for k in kids]
        text = render(args.projekt, pairs, missing)

    else:
        text = render(args.projekt, scenes, missing)

    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print(f"{args.out}: {len(text.split())} Woerter", file=sys.stderr)
    else:
        sys.stdout.write(text)

    if missing:
        print("Fehlende Szenendateien (in Index.md gelistet, nicht auf der Platte):\n  "
              + "\n  ".join(missing), file=sys.stderr)


if __name__ == "__main__":
    main()
