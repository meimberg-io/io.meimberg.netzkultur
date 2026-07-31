#!/usr/bin/env python3
"""Redaktions-Lint: mechanischer Stil-Check für Hub-Drafts.

Prüft einen Markdown-Draft auf das eine Zeichen, das sich mechanisch
zuverlässig ahnden lässt: den langen Gedankenstrich (Em-Dash).

Alles Weitere (Floskeln, Ausrufezeichen, rhetorische Überschriften) lässt
sich nicht per Wort- oder Musterliste erschlagen. Ob ein Wort wie "disruptiv"
oder ein Ausrufezeichen an einer Stelle stört, hängt vom Kontext ab und
gehört ins redaktionelle Urteil, nicht in ein Skript. Diese Checks lagen
früher hier und sind bewusst entfernt worden: eine Wortverbotsliste greift
zu kurz.

Zwei Modi:
  Hook-Modus (kein Argument): liest PostToolUse-JSON von stdin, zieht
    tool_input.file_path. Greift nur für *.md unter drafts/. Findet er einen
    Em-Dash, schreibt er die Fundstellen nach stderr und beendet mit Exit 2
    (Claude bekommt die Fundstellen als Feedback und bessert nach).
    Sauber: Exit 0, still.
  CLI-Modus: redaktion-lint.py <datei.md>: Report nach stdout, Exit 1 bei
    Funden, sonst 0.
"""

import json
import sys


def lint_text(text):
    """Liefert (zeile, kategorie, fund, hinweis) für jeden Em-Dash."""
    findings = []
    for i, line in enumerate(text.splitlines(), start=1):
        if "—" in line:  # em-dash —
            findings.append((i, "langer Gedankenstrich", "—",
                             "auflösen (Komma, Punkt oder Klammer)"))
    return findings


def format_report(path, findings):
    out = [f"REDAKTIONS-LINT: {path}",
           f"{len(findings)} Gedankenstrich(e) gefunden:", ""]
    for line_no, cat, hit, hint in findings:
        out.append(f"  [Z. {line_no}] {cat}: »{hit}« → {hint}")
    out.append("")
    out.append("Bitte auflösen.")
    return "\n".join(out)


def is_draft(path):
    """Greift auf redaktionelle Texte, egal wo sie liegen.

    In diesem Repo liegen die geschnittenen Kapitel-Szenen unter chapters/,
    die noch nicht geschnittenen Kapitel und kuerzere Sachen unter drafts/.
    Beides muss greifen, sonst laeuft der Check stillschweigend ins Leere.
    """
    if not path.endswith(".md"):
        return False
    parts = path.split("/")
    return bool({"chapters", "drafts", "draft"} & set(parts))


def main():
    # CLI-Modus
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            print(f"redaktion-lint: kann {path} nicht lesen: {exc}", file=sys.stderr)
            return 0
        findings = lint_text(text)
        if findings:
            print(format_report(path, findings))
            return 1
        print(f"redaktion-lint: {path} ist sauber.")
        return 0

    # Hook-Modus: PostToolUse-JSON von stdin
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    path = (payload.get("tool_input") or {}).get("file_path", "")
    if not path or not is_draft(path):
        return 0
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return 0
    findings = lint_text(text)
    if not findings:
        return 0
    print(format_report(path, findings), file=sys.stderr)
    return 2  # stderr wird Claude als Feedback gezeigt; Aufgabe: nachbessern


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # Lint darf die Session nie killen
        sys.exit(0)
