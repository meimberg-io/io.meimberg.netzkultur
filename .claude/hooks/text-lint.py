#!/usr/bin/env python3
"""Mechanischer Stil-Check fuer redaktionelle Texte.

Prueft Markdown unter manuscript/ auf das eine Zeichen, das sich mechanisch zuverlaessig
ahnden laesst: den langen Gedankenstrich (Em-Dash). Er ist das deutlichste Merkmal
maschinengeschriebener Prosa und laesst sich immer aufloesen, in Komma, Punkt,
Doppelpunkt oder Klammer.

Alles Weitere gehoert nicht hierher. Ob eine Floskel, ein Ausrufezeichen oder ein
Wort wie "disruptiv" an einer Stelle stoert, haengt vom Kontext ab; das ist
redaktionelles Urteil und Sache der Pruef-Linsen. Eine Wortverbotsliste greift zu
kurz und erzeugt genau die Vermeidungsprosa, die dieses Repo verhindern soll.

Zwei Modi:
  Hook (kein Argument): liest PostToolUse-JSON von stdin, zieht tool_input.file_path.
    Bei Funden gehen die Fundstellen nach stderr, Exit 2 -- Claude bekommt sie als
    Feedback und bessert nach. Sauber: Exit 0, still.
  CLI (text-lint.py <datei.md>): Report nach stdout, Exit 1 bei Funden.
"""

import json
import sys

# Verzeichnisse mit redaktionellem Text. Wer die Textablage umbenennt, aendert das hier.
TEXT_DIRS = {"manuscript"}


def findings(text):
    """Zeilennummer und Spalte jedes Em-Dashs."""
    hits = []
    for number, line in enumerate(text.splitlines(), start=1):
        start = 0
        while (index := line.find("—", start)) != -1:
            hits.append((number, index + 1, line.strip()))
            start = index + 1
    return hits


def report(path, hits):
    wort = "langer Gedankenstrich" if len(hits) == 1 else "lange Gedankenstriche"
    out = [f"TEXT-LINT: {path}", f"{len(hits)} {wort} gefunden:", ""]
    for number, column, line in hits:
        snippet = line if len(line) <= 90 else line[:87] + "..."
        out.append(f"  Z. {number}, Sp. {column}: {snippet}")
    out.append("")
    out.append("Aufloesen: Komma, Punkt, Doppelpunkt oder Klammer.")
    return "\n".join(out)


def is_text_file(path):
    return path.endswith(".md") and bool(TEXT_DIRS & set(path.split("/")))


def read(path):
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except OSError:
        return None


def main():
    if len(sys.argv) > 1:  # CLI
        path = sys.argv[1]
        text = read(path)
        if text is None:
            print(f"text-lint: kann {path} nicht lesen.", file=sys.stderr)
            return 0
        hits = findings(text)
        if hits:
            print(report(path, hits))
            return 1
        print(f"text-lint: {path} ist sauber.")
        return 0

    try:  # Hook
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    path = (payload.get("tool_input") or {}).get("file_path", "")
    if not path or not is_text_file(path):
        return 0
    text = read(path)
    if text is None:
        return 0
    hits = findings(text)
    if not hits:
        return 0
    print(report(path, hits), file=sys.stderr)
    return 2  # stderr geht als Feedback an Claude


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # Ein Lint darf die Session nie killen.
        sys.exit(0)
