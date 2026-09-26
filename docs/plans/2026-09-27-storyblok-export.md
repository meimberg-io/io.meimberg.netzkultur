# Storyblok-Export Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ein Skript `scripts/storyblok-export.py`, das den Stand von `manuscript/` wiederholbar in das Storyblok-Special `s/netzkultur` überträgt, mit Bildern, Bildreihen, Video und Nachweisen; dazu die Anzeige der Nachweise auf meimberg.io.

**Architecture:** Vier Python-Module unter `scripts/`: `manuscript_index.py` liest den Longform-Index (gemeinsam mit `kompilieren.py`), `sb_content.py` übersetzt Markdown ohne Netz in Storyblok-Blöcke, `sb_api.py` ist ein schmaler Client für die Management API, `sb_export.py` verbindet beides und trägt die Kommandozeile; `storyblok-export.py` ist nur der Einstieg. Im Website-Repo zeigt eine neue Komponente `AssetCredit` Bildunterschrift und Nachweis unter `picture`, `gallery` und `video`.

**Tech Stack:** Python 3 (Standardbibliothek, `pyyaml`), `exiftool`, `unittest`; Storyblok Management API v1 (`https://mapi.storyblok.com/v1/spaces/330326`); Next.js 15 / React / Tailwind im Repo `io.meimberg.www`.

**Spec:** `docs/specs/2026-09-27-storyblok-export-design.md`

## Global Constraints

- Space `330326`, Story-Ordner `s/netzkultur/`, Asset-Ordner `netzkultur`.
- Token nur aus `STORYBLOK_MANAGEMENT_TOKEN` (Umgebung) oder `.env` im Repo-Wurzelverzeichnis; `.env` ist in `.gitignore`. Der Token erscheint nie in Ausgaben, Commits oder Plänen.
- Geschrieben werden nur `body`, Story-Name und `pagetitle`. Slug bestehender Stories, `headerpicture`, `teasertitle`, `teaserimage`, `abstract`, `readmoretext`, `pageintro`, `date` bleiben unangetastet.
- Standard ist Entwurf; veröffentlicht wird nur mit `--publish`.
- Kein Bild und kein Video ohne Alt-Text, ohne `Rights` oder mit leerer bzw. „ungeklärt“ enthaltender `UsageTerms` geht nach Storyblok, auch nicht als Entwurf.
- Alle Prüfungen laufen vor der ersten schreibenden Anfrage; ein Fehler bricht ab, bevor etwas geschrieben ist.
- Höchstens drei Anfragen pro Sekunde, bei HTTP 429 Wiederholung mit Pause.
- Keine neuen Python-Abhängigkeiten außer den vorhandenen (`pyyaml`, `exiftool`).
- Identifier englisch, Meldungen und Docstrings deutsch (Projekt-`CLAUDE.md`).
- Texte unter `manuscript/` werden nicht verändert. Skripte, Doku und Konfiguration werden committet, Commit-Message als kurze deutsche Zeile im Stil von `git log`, ohne KI-Attribution; gepusht wird nicht.
- Schreibende Läufe gegen Storyblok (Task 9) nur nach ausdrücklicher Zustimmung von Oli im Chat.

Tests laufen aus dem Repo-Wurzelverzeichnis mit:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

---

## Dateiübersicht

| Datei | Aufgabe |
|---|---|
| `scripts/manuscript_index.py` (neu) | Index lesen, Szenen gruppieren, Präfixe und Kapitelnummern; aus `kompilieren.py` herausgelöst |
| `scripts/kompilieren.py` (ändern) | importiert die Index-Funktionen statt sie selbst zu definieren |
| `scripts/sb_content.py` (neu) | Markdown → Richtext-Knoten, Blöcke, Slug, Titel, Story-Zuordnung, Bildmetadaten, Asset-Feld; kein Netz |
| `scripts/sb_api.py` (neu) | Management-API-Client: Stories, Assets, Upload, Drosselung |
| `scripts/sb_export.py` (neu) | Teile sammeln, Offline-Prüfung, Assets, Stories, Bericht, `main()` |
| `scripts/storyblok-export.py` (neu) | Einstieg für die Kommandozeile |
| `scripts/test_storyblok_export.py` (neu) | alle Unittests |
| `.gitignore`, `rules/werkzeuge.md`, `state/publikation.md` (ändern) | Pflege |
| `io.meimberg.www/src/components/elements/AssetCredit.tsx` (neu) | Nachweis-Komponente |
| `io.meimberg.www/src/components/elements/Picture.tsx`, `Gallery.tsx`, `Video.tsx` (ändern) | Alt-Text und Nachweis |

---

### Task 1: Index-Funktionen herauslösen

**Files:**
- Create: `scripts/manuscript_index.py`
- Modify: `scripts/kompilieren.py` (Definitionen von `PREFIX`, `FRONTMATTER`, `read_index`, `flatten`, `body_of`, `chapters` entfernen, Import ergänzen)
- Test: `scripts/test_storyblok_export.py`

**Interfaces:**
- Produces: `manuscript_index.PREFIX`, `FRONTMATTER`, `read_index(project: Path) -> list`, `flatten(items, level=1) -> list[tuple[int, str]]`, `body_of(project: Path, name: str) -> str | None`, `chapters(scenes) -> list[tuple[str, list[str]]]`, `strip_prefix(name: str) -> str`, `chapter_number(name: str) -> int | None`

- [ ] **Step 1: Referenzausgaben von `kompilieren.py` vor der Änderung sichern**

```bash
S=$(mktemp -d)
python3 scripts/kompilieren.py > $S/voll.md
python3 scripts/kompilieren.py --abriss > $S/abriss.md
python3 scripts/kompilieren.py --kapitel 1 > $S/k1.md
python3 scripts/kompilieren.py --naht 1 > $S/naht1.md
echo $S
```

Den ausgegebenen Pfad für Step 6 merken.

- [ ] **Step 2: Failing test schreiben**

`scripts/test_storyblok_export.py` anlegen:

```python
"""Tests für den Storyblok-Export. Aufruf aus dem Repo:

    python3 -m unittest discover -s scripts -p 'test_*.py' -v
"""

import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import manuscript_index as mi


def write_manuscript(root, scenes_yaml, files):
    """Legt ein Mini-Manuskript an: Index.md plus Szenendateien."""
    (root / "Index.md").write_text(
        "---\nlongform:\n  format: scenes\n  title: T\n  scenes:\n" + scenes_yaml + "---\n",
        encoding="utf-8")
    for name, body in files.items():
        (root / f"{name}.md").write_text(f"---\nstatus: draft\ncomment:\n---\n{body}", encoding="utf-8")


class ManuscriptIndexTest(unittest.TestCase):
    def test_chapter_number_and_strip_prefix(self):
        self.assertEqual(mi.chapter_number("01 - Bevor das Internet"), 1)
        self.assertEqual(mi.chapter_number("00.02 - Was dieses Buch erzählt"), 0)
        self.assertIsNone(mi.chapter_number("Ohne Nummer"))
        self.assertEqual(mi.strip_prefix("01.03 - Das Usenet"), "Das Usenet")
        self.assertEqual(mi.strip_prefix("02.04 - Die ersten Inhalte - Do It Yourself"),
                         "Die ersten Inhalte - Do It Yourself")

    def test_chapters_groups_scenes_under_level_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            write_manuscript(root,
                             "    - 01 - Eins\n    - - 01.01 - A\n      - 01.02 - B\n    - 02 - Zwei\n",
                             {"01 - Eins": "Vorspann", "01.01 - A": "a", "01.02 - B": "b", "02 - Zwei": ""})
            groups = mi.chapters(mi.flatten(mi.read_index(root)))
            self.assertEqual(groups, [("01 - Eins", ["01.01 - A", "01.02 - B"]), ("02 - Zwei", [])])
            self.assertEqual(mi.body_of(root, "01 - Eins"), "Vorspann")
            self.assertIsNone(mi.body_of(root, "fehlt"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Test laufen lassen, er muss scheitern**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: FAIL mit `ModuleNotFoundError: No module named 'manuscript_index'`

- [ ] **Step 4: `scripts/manuscript_index.py` anlegen**

```python
"""Liest manuscript/Index.md und die Szenendateien.

Gemeinsam genutzt von kompilieren.py und storyblok-export.py, damit beide
Reihenfolge, Verschachtelung und Ueberschriften identisch bestimmen.
Index.md ist die einzige Wahrheit ueber Zugehoerigkeit und Reihenfolge.
"""

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


def chapters(scenes):
    """Gruppiert zu [(elternname, [kindnamen]), ...] anhand der Ebene 1."""
    groups = []
    for level, name in scenes:
        if level == 1:
            groups.append((name, []))
        elif groups:
            groups[-1][1].append(name)
    return groups


def strip_prefix(name):
    """Ordnungspraefix wie '01.03 - ' abschneiden, wie der Compile-Step."""
    return PREFIX.sub("", name)


def chapter_number(name):
    """Fuehrende Zahl des Ordnungspraefixes, None ohne Praefix."""
    match = re.match(r"^\s*(\d+)", name)
    return int(match.group(1)) if match else None
```

- [ ] **Step 5: `kompilieren.py` umstellen**

In `scripts/kompilieren.py` die Zeilen von `PREFIX = re.compile(...)` bis einschließlich der Funktion `chapters(scenes)` löschen, mit Ausnahme von `heading()`, das bleibt. Konkret entfallen: `PREFIX`, `FRONTMATTER`, `read_index`, `flatten`, `body_of`, `chapters`. Direkt nach den bestehenden Imports (`import argparse`, `import pathlib`, `import re`, `import sys`) einfügen:

```python
from manuscript_index import PREFIX, body_of, chapters, flatten, read_index
```

`heading`, `render`, `pick_chapter`, `first_sentences` und `main` bleiben unverändert; sie nutzen `PREFIX`, `body_of`, `chapters`, `flatten`, `read_index` jetzt über den Import.

- [ ] **Step 6: Tests und Regressionsvergleich**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: 2 Tests PASS

- Run (mit dem Pfad aus Step 1 als `$S`):

```bash
python3 scripts/kompilieren.py | diff - $S/voll.md && \
python3 scripts/kompilieren.py --abriss | diff - $S/abriss.md && \
python3 scripts/kompilieren.py --kapitel 1 | diff - $S/k1.md && \
python3 scripts/kompilieren.py --naht 1 | diff - $S/naht1.md && echo IDENTISCH
```

- Expected: `IDENTISCH`

- [ ] **Step 7: Commit**

```bash
git add scripts/manuscript_index.py scripts/kompilieren.py scripts/test_storyblok_export.py
git commit -m "Index-Lesen aus kompilieren.py in ein gemeinsames Modul" -- scripts/manuscript_index.py scripts/kompilieren.py scripts/test_storyblok_export.py
```

---

### Task 2: Markdown in Richtext übersetzen

**Files:**
- Create: `scripts/sb_content.py`
- Test: `scripts/test_storyblok_export.py` (Klasse `MarkdownTest` ergänzen)

**Interfaces:**
- Consumes: nichts aus Task 1
- Produces:
  - `class ContentError(Exception)` mit Attribut `messages: list[str]`
  - `text_node(text: str, marks: tuple = ()) -> dict`
  - `inline(text: str, marks: tuple = ()) -> list[dict]`
  - `parse_markdown(text: str, source: str) -> tuple[list[tuple[str, list]], list[str]]` — Segmente `("rich", [knoten])` oder `("media", [dateinamen])`, dazu Hinweise; wirft `ContentError`
  - `is_video(name: str) -> bool`

- [ ] **Step 1: Failing tests schreiben**

Am Kopf von `scripts/test_storyblok_export.py` nach `import manuscript_index as mi` ergänzen:

```python
import sb_content as sc
```

Vor `if __name__ == "__main__":` einfügen:

```python
def t(text, *marks):
    return sc.text_node(text, marks)


def para(*nodes):
    return {"type": "paragraph", "content": list(nodes)}


class MarkdownTest(unittest.TestCase):
    def rich(self, text):
        segments, warnings = sc.parse_markdown(text, "x.md")
        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0][0], "rich")
        return segments[0][1]

    def test_inline_marks(self):
        self.assertEqual(sc.inline("a **fett** b"), [t("a "), t("fett", "bold"), t(" b")])
        self.assertEqual(sc.inline("*kursiv* und _auch_"), [t("kursiv", "italic"), t(" und "), t("auch", "italic")])
        self.assertEqual(sc.inline("Code `rec.arts.movies` hier"),
                         [t("Code "), t("rec.arts.movies", "code"), t(" hier")])
        self.assertEqual(sc.inline("**fett mit _kursiv_**"),
                         [t("fett mit ", "bold"), t("kursiv", "bold", "italic")])

    def test_inline_leaves_intraword_underscore_and_code_content(self):
        self.assertEqual(sc.inline("snake_case_name"), [t("snake_case_name")])
        self.assertEqual(sc.inline("Zucken `¯\\_(ツ)_/¯` und _„Keine Ahnung“_"),
                         [t("Zucken "), t("¯\\_(ツ)_/¯", "code"), t(" und "), t("„Keine Ahnung“", "italic")])

    def test_paragraphs_and_headings(self):
        nodes = self.rich("Erster Satz.\nGleicher Absatz.\n\n### Unter\n\nZweiter.\n\n#### Tiefer")
        self.assertEqual(nodes, [
            para(t("Erster Satz. Gleicher Absatz.")),
            {"type": "heading", "attrs": {"level": 3}, "content": [t("Unter")]},
            para(t("Zweiter.")),
            {"type": "heading", "attrs": {"level": 4}, "content": [t("Tiefer")]},
        ])

    def test_lists(self):
        nodes = self.rich("- eins\n- **zwei**\n\n1. erstens\n2. zweitens")
        item = lambda *n: {"type": "list_item", "content": [para(*n)]}
        self.assertEqual(nodes, [
            {"type": "bullet_list", "content": [item(t("eins")), item(t("zwei", "bold"))]},
            {"type": "ordered_list", "attrs": {"order": 1}, "content": [item(t("erstens")), item(t("zweitens"))]},
        ])

    def test_quote_callout_and_image_marker(self):
        text = ("> _„Zitat“_\n\n"
                "> [!NOTE] Issues\n> Contents\n\n"
                "> **[BILD-MARKER 1: KETTENBRIEFE]**\n> \n> _Vorschlag: ..._\n\n"
                "Text.")
        segments, warnings = sc.parse_markdown(text, "x.md")
        self.assertEqual(segments, [("rich", [
            {"type": "blockquote", "content": [para(t("„Zitat“", "italic"))]},
            para(t("Text.")),
        ])])
        self.assertEqual(warnings, ["x.md:6: offener Bildplatz übersprungen"])

    def test_media_lines(self):
        text = "Vorher.\n\n![[a.png|300]]\n\n![[b.png|100]] ![[c.png|100]]\n\n![[film.mp4]]\n\nNachher."
        segments, _ = sc.parse_markdown(text, "x.md")
        self.assertEqual(segments, [
            ("rich", [para(t("Vorher."))]),
            ("media", ["a.png"]),
            ("media", ["b.png", "c.png"]),
            ("media", ["film.mp4"]),
            ("rich", [para(t("Nachher."))]),
        ])

    def test_media_row_with_separator_punctuation(self):
        segments, _ = sc.parse_markdown("![[a.png|300]].  ![[b.png|300]]", "x.md")
        self.assertEqual(segments, [("media", ["a.png", "b.png"])])

    def test_errors_name_file_and_line(self):
        cases = {
            "| a | b |": "x.md:1: Tabelle",
            "Siehe [hier](http://x)": "x.md:1: Link",
            "Siehe [[Seite]]": "x.md:1: Link",
            "<b>x</b>": "x.md:1: HTML",
            "Text\n\n## Zu hoch": "x.md:3: Überschrift der Ebene 2",
            "Text ![[a.png]] mitten": "x.md:1: Bild mitten im Absatz",
            "![[a.png]] ![[b.mp4]]": "x.md:1: Video in einer Bildreihe",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                with self.assertRaises(sc.ContentError) as ctx:
                    sc.parse_markdown(text, "x.md")
                self.assertTrue(ctx.exception.messages[0].startswith(expected), ctx.exception.messages)

    def test_hashtag_is_not_a_heading(self):
        self.assertEqual(self.rich("#hashtag am Anfang"), [para(t("#hashtag am Anfang"))])

    def test_code_block_keeps_lines_verbatim(self):
        text = "Davor.\n\n```\n\n  +---+\n  | x |\n\n  > nicht zitiert\n```\n\nDanach."
        self.assertEqual(self.rich(text), [
            para(t("Davor.")),
            {"type": "code_block", "content": [t("\n  +---+\n  | x |\n\n  > nicht zitiert")]},
            para(t("Danach.")),
        ])
        segments, _ = sc.parse_markdown("```python\nprint(1)\n```", "x.md")
        self.assertEqual(segments[0][1][0]["attrs"], {"class": "language-python"})

    def test_unclosed_code_block_is_an_error(self):
        with self.assertRaises(sc.ContentError) as ctx:
            sc.parse_markdown("Text\n\n```\nhängt", "x.md")
        self.assertEqual(ctx.exception.messages, ["x.md:3: Codeblock wird nicht geschlossen"])
```

- [ ] **Step 2: Tests laufen lassen, sie müssen scheitern**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: FAIL mit `ModuleNotFoundError: No module named 'sb_content'`

- [ ] **Step 3: `scripts/sb_content.py` anlegen**

```python
"""Manuskript-Markdown in Storyblok-Bloecke uebersetzen. Ohne Netz, ohne Seiteneffekte.

Kennt nur die Elemente, die im Manuskript vorkommen
(docs/specs/2026-09-27-storyblok-export-design.md). Alles andere ist ein
Fehler mit Datei und Zeile, damit kein Text still verloren geht.
"""

import re


class ContentError(Exception):
    """Sammelt Fehlermeldungen; str() listet sie zeilenweise."""

    def __init__(self, messages):
        self.messages = list(messages)
        super().__init__("\n".join(self.messages))


INLINE = re.compile(
    r"`([^`]+)`"                                            # code
    r"|\*\*(.+?)\*\*"                                       # fett
    r"|(?<![\w*])\*(?![\s*])(.+?)(?<![\s*])\*(?![\w*])"     # kursiv mit *
    r"|(?<!\w)_(?![\s_])(.+?)(?<![\s_])_(?!\w)"             # kursiv mit _
)
EMBED = re.compile(r"!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
BULLET = re.compile(r"^[-*]\s+(.*)$")
ORDERED = re.compile(r"^(\d+)\.\s+(.*)$")
QUOTE = re.compile(r"^>\s?(.*)$")
LINK = re.compile(r"(?<!!)\[\[|\]\(")
VIDEO_EXTENSIONS = (".mp4", ".webm", ".ogv")
FENCE = "```"


def is_video(name):
    return name.lower().endswith(VIDEO_EXTENSIONS)


def text_node(text, marks=()):
    node = {"type": "text", "text": text}
    if marks:
        node["marks"] = [{"type": mark} for mark in marks]
    return node


def inline(text, marks=()):
    """Inline-Markdown (fett, kursiv, code) als Liste von Text-Knoten."""
    nodes, pos = [], 0
    for match in INLINE.finditer(text):
        if match.start() > pos:
            nodes.append(text_node(text[pos:match.start()], marks))
        code, bold, star, under = match.groups()
        if code is not None:
            nodes.append(text_node(code, marks + ("code",)))
        elif bold is not None:
            nodes += inline(bold, marks + ("bold",))
        else:
            nodes += inline(star if star is not None else under, marks + ("italic",))
        pos = match.end()
    if pos < len(text):
        nodes.append(text_node(text[pos:], marks))
    return nodes


def _paragraph(text):
    return {"type": "paragraph", "content": inline(text)}


def parse_markdown(text, source):
    """Liefert (segmente, hinweise).

    Segment: ("rich", [richtext-knoten]) oder ("media", [dateinamen]).
    Wirft ContentError mit allen Fehlern der Datei.
    """
    segments, warnings, errors = [], [], []
    nodes = []       # Knoten des laufenden richtext-Abschnitts
    para = []        # Zeilen des laufenden Absatzes
    lst = None       # {"type": ..., "items": [...], "start": n}
    quote = None     # {"line": n, "lines": [...]}
    code = None      # {"line": n, "lines": [...], "lang": str}

    def flush_para():
        nonlocal para
        if para:
            nodes.append(_paragraph(" ".join(para)))
            para = []

    def flush_list():
        nonlocal lst
        if lst:
            items = [{"type": "list_item", "content": [_paragraph(item)]} for item in lst["items"]]
            node = {"type": lst["type"], "content": items}
            if lst["type"] == "ordered_list":
                node["attrs"] = {"order": lst["start"]}
            nodes.append(node)
            lst = None

    def flush_quote():
        nonlocal quote
        if quote:
            first = quote["lines"][0].strip()
            if first.startswith("[!"):
                pass  # Obsidian-Callout: Redaktionsnotiz, gehoert nicht ins Buch
            elif "BILD-MARKER" in first:
                warnings.append(f"{source}:{quote['line']}: offener Bildplatz übersprungen")
            else:
                paragraphs, current = [], []
                for line in quote["lines"]:
                    if line.strip():
                        current.append(line.strip())
                    elif current:
                        paragraphs.append(current)
                        current = []
                if current:
                    paragraphs.append(current)
                nodes.append({"type": "blockquote",
                              "content": [_paragraph(" ".join(p)) for p in paragraphs]})
            quote = None

    def flush_all():
        flush_para()
        flush_list()
        flush_quote()

    for number, raw in enumerate(text.split("\n"), start=1):
        line = raw.strip()
        where = f"{source}:{number}"

        if code is not None:
            if line.startswith(FENCE):
                node = {"type": "code_block",
                        "content": [text_node("\n".join(code["lines"]))] if code["lines"] else []}
                if code["lang"]:
                    node["attrs"] = {"class": f"language-{code['lang']}"}
                nodes.append(node)
                code = None
            else:
                code["lines"].append(raw)
            continue

        if quote is not None and not raw.startswith(">"):
            flush_quote()
        if not line:
            flush_para()
            flush_list()
            continue

        if line.startswith(FENCE):
            flush_all()
            code = {"line": number, "lines": [], "lang": line[len(FENCE):].strip()}
            continue

        match = QUOTE.match(raw)
        if match:
            flush_para()
            flush_list()
            if quote is None:
                quote = {"line": number, "lines": []}
            quote["lines"].append(match.group(1))
            continue

        embeds = EMBED.findall(line)
        if embeds and not EMBED.sub("", line).strip(" .,;"):
            if len(embeds) > 1 and any(is_video(name) for name in embeds):
                errors.append(f"{where}: Video in einer Bildreihe")
                continue
            flush_all()
            if nodes:
                segments.append(("rich", nodes))
                nodes = []
            segments.append(("media", [name.strip() for name in embeds]))
            continue
        if embeds:
            errors.append(f"{where}: Bild mitten im Absatz")
            continue
        if LINK.search(line):
            errors.append(f"{where}: Link wird nicht unterstützt")
            continue
        if line.startswith("|"):
            errors.append(f"{where}: Tabelle wird nicht unterstützt")
            continue
        if line.startswith("<"):
            errors.append(f"{where}: HTML wird nicht unterstützt")
            continue

        match = HEADING.match(line)
        if match:
            level = len(match.group(1))
            if level not in (3, 4):
                errors.append(f"{where}: Überschrift der Ebene {level} gehört nicht in eine Szene")
                continue
            flush_all()
            nodes.append({"type": "heading", "attrs": {"level": level},
                          "content": inline(match.group(2).strip())})
            continue

        indented = raw[:1].isspace()
        bullet = BULLET.match(line)
        ordered = ORDERED.match(line)
        if (bullet or ordered) and not indented:
            flush_para()
            kind = "bullet_list" if bullet else "ordered_list"
            if lst is None or lst["type"] != kind:
                flush_list()
                lst = {"type": kind, "items": [],
                       "start": int(ordered.group(1)) if ordered else 1}
            lst["items"].append(bullet.group(1) if bullet else ordered.group(2))
            continue
        if lst is not None and indented:
            lst["items"][-1] += " " + line
            continue

        flush_list()
        para.append(line)

    if code is not None:
        errors.append(f"{source}:{code['line']}: Codeblock wird nicht geschlossen")
    flush_all()
    if nodes:
        segments.append(("rich", nodes))
    if errors:
        raise ContentError(errors)
    return segments, warnings
```

Hinweis zur Closure: `nodes = []` in der Schleife bindet die Variable der umschließenden Funktion neu; die inneren Funktionen sehen die neue Liste, weil sie die Variable und nicht den Wert referenzieren.

- [ ] **Step 4: Tests laufen lassen**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: alle Tests PASS

- [ ] **Step 5: Gegen das echte Manuskript laufen lassen**

```bash
cd scripts && python3 -c "
import pathlib, sb_content as sc, manuscript_index as mi
root = pathlib.Path('../manuscript'); errs = []; warns = []
for level, name in mi.flatten(mi.read_index(root)):
    body = mi.body_of(root, name)
    try:
        _, w = sc.parse_markdown(body or '', name + '.md'); warns += w
    except sc.ContentError as e:
        errs += e.messages
print(len(warns), 'Hinweise'); print('\n'.join(errs) or 'keine Fehler')
"; cd ..
```

- Expected: `18 Hinweise` und `keine Fehler` (Stand 2026-09-27; die Zahl der Hinweise ist die Zahl der BILD-MARKER-Blöcke in Szenen, die im Index stehen, und darf abweichen, wenn Oli das Manuskript inzwischen geändert hat). Meldet der Lauf Fehler, ist entweder der Konverter falsch (dann Test ergänzen und korrigieren) oder das Manuskript enthält ein nicht unterstütztes Element (dann Oli melden, nicht das Manuskript ändern).

- [ ] **Step 6: Commit**

```bash
git add scripts/sb_content.py scripts/test_storyblok_export.py
git commit -m "Storyblok-Export: Markdown des Manuskripts in Richtext übersetzen" -- scripts/sb_content.py scripts/test_storyblok_export.py
```

---

### Task 3: Blöcke, Slugs, Titel und Story-Zuordnung

**Files:**
- Modify: `scripts/sb_content.py` (Funktionen anhängen)
- Test: `scripts/test_storyblok_export.py` (Klasse `BodyTest` ergänzen)

**Interfaces:**
- Consumes: `parse_markdown`, `text_node`, `is_video`, `ContentError` (Task 2); `strip_prefix`, `chapter_number` (Task 1)
- Produces:
  - `build_body(intro: tuple[str, str] | None, scenes: list[tuple[str, str, str]], resolve: Callable[[str], dict]) -> tuple[list[dict], list[str]]` — `intro` ist `(text, quelle)`, `scenes` sind `(titel_ohne_praefix, text, quelle)`, `resolve(dateiname)` liefert das Asset-Feld
  - `strip_uids(value) -> value` ohne `_uid`-Schlüssel, rekursiv
  - `slugify(name: str) -> str`
  - `story_title(number: int, name: str) -> str`
  - `match_story(number: int, stories: list[dict]) -> dict | None`, wirft `ContentError` bei mehreren Treffern

- [ ] **Step 1: Failing tests schreiben**

Vor `if __name__ == "__main__":` einfügen:

```python
class BodyTest(unittest.TestCase):
    def resolve(self, name):
        return {"filename": name}

    def test_body_blocks(self):
        intro = ("Vorspann.", "01 - K.md")
        scenes = [
            ("Szene A", "Text A.\n\n![[bild.png]]\n\nRest A.", "01.01 - Szene A.md"),
            ("Szene B", "![[a.png]] ![[b.png]]\n\n![[film.mp4]]", "01.02 - Szene B.md"),
        ]
        blocks, warnings = sc.build_body(intro, scenes, self.resolve)
        h2 = lambda text: {"type": "heading", "attrs": {"level": 2}, "content": [t(text)]}
        doc = lambda *n: {"type": "doc", "content": list(n)}
        self.assertEqual(sc.strip_uids(blocks), [
            {"component": "richtext", "content": doc(para(t("Vorspann.")))},
            {"component": "richtext", "content": doc(h2("Szene A"), para(t("Text A.")))},
            {"component": "picture", "image": {"filename": "bild.png"}, "style": "normal", "spacing": "default"},
            {"component": "richtext", "content": doc(para(t("Rest A.")))},
            {"component": "richtext", "content": doc(h2("Szene B"))},
            {"component": "gallery", "images": [{"filename": "a.png"}, {"filename": "b.png"}],
             "columns": "2", "layout": "default", "title": ""},
            {"component": "video", "file": {"filename": "film.mp4"}},
        ])
        self.assertEqual(warnings, [])
        self.assertTrue(all(len(b["_uid"]) == 36 for b in blocks))

    def test_gallery_columns_capped_at_three(self):
        blocks, _ = sc.build_body(None, [("S", "![[a.png]] ![[b.png]] ![[c.png]] ![[d.png]]", "s.md")], self.resolve)
        self.assertEqual(blocks[1]["columns"], "3")

    def test_empty_intro_is_skipped_and_errors_are_collected(self):
        blocks, _ = sc.build_body(("", "k.md"), [("S", "Text.", "s.md")], self.resolve)
        self.assertEqual(len(blocks), 1)
        with self.assertRaises(sc.ContentError) as ctx:
            sc.build_body(None, [("A", "| x |", "a.md"), ("B", "## y", "b.md")], self.resolve)
        self.assertEqual(len(ctx.exception.messages), 2)

    def test_slugs_match_existing_stories(self):
        expected = {
            "01 - Bevor das Internet ein öffentlicher Ort war": "01-bevor-das-internet-ein-oeffentlicher-ort-war",
            "02 - Die ersten Jahre des öffentlichen Internets": "02-die-ersten-jahre-des-oeffentlichen-internets",
            "03 - Das Internet wird zum Lebensraum": "03-das-internet-wird-zum-lebensraum",
            "04 - Die Sprache des Netzes": "04-die-sprache-des-netzes",
            "05 - Memes und andere Phänomene": "05-memes-und-andere-phaenomene",
            "06 - Die große Plattformisierung": "06-die-grosse-plattformisierung",
            "07 - Was vom alten Netz geblieben ist": "07-was-vom-alten-netz-geblieben-ist",
        }
        for name, slug in expected.items():
            self.assertEqual(sc.slugify(name), slug)

    def test_story_title(self):
        self.assertEqual(sc.story_title(0, "00 - Netzkultur – Eine Retrospektive"), "Netzkultur – Eine Retrospektive")
        self.assertEqual(sc.story_title(3, "03 - Das Internet wird zum Lebensraum"),
                         "Kapitel 3: Das Internet wird zum Lebensraum")

    def test_match_story(self):
        stories = [
            {"id": 1, "slug": "index", "is_startpage": True},
            {"id": 2, "slug": "01-bevor", "is_startpage": False},
            {"id": 3, "slug": "10-spaeter", "is_startpage": False},
        ]
        self.assertEqual(sc.match_story(0, stories)["id"], 1)
        self.assertEqual(sc.match_story(1, stories)["id"], 2)
        self.assertIsNone(sc.match_story(2, stories))
        with self.assertRaises(sc.ContentError):
            sc.match_story(1, stories + [{"id": 4, "slug": "01-doppelt", "is_startpage": False}])
```

- [ ] **Step 2: Tests laufen lassen, sie müssen scheitern**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: FAIL mit `AttributeError: module 'sb_content' has no attribute 'build_body'`

- [ ] **Step 3: Funktionen in `scripts/sb_content.py` ergänzen**

Oben bei den Imports ergänzen:

```python
import uuid

from manuscript_index import chapter_number, strip_prefix
```

Am Dateiende anhängen:

```python
UMLAUTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
MAX_GALLERY_COLUMNS = 3


def new_uid():
    return str(uuid.uuid4())


def richtext_block(nodes):
    return {"_uid": new_uid(), "component": "richtext", "content": {"type": "doc", "content": nodes}}


def media_block(names, resolve):
    fields = [resolve(name) for name in names]
    if len(names) == 1 and is_video(names[0]):
        return {"_uid": new_uid(), "component": "video", "file": fields[0]}
    if len(names) == 1:
        return {"_uid": new_uid(), "component": "picture", "image": fields[0],
                "style": "normal", "spacing": "default"}
    return {"_uid": new_uid(), "component": "gallery", "images": fields,
            "columns": str(min(len(names), MAX_GALLERY_COLUMNS)), "layout": "default", "title": ""}


def build_body(intro, scenes, resolve):
    """Blockliste eines Teils.

    intro: (text, quelle) der Kapiteldatei oder None.
    scenes: [(titel ohne Praefix, text, quelle)].
    resolve(dateiname) -> Asset-Feld fuer picture, gallery und video.
    Liefert (bloecke, hinweise); wirft ContentError mit allen Fehlern.
    """
    blocks, warnings, errors = [], [], []

    def emit(text, source, lead):
        try:
            segments, found = parse_markdown(text, source)
        except ContentError as error:
            errors.extend(error.messages)
            return
        warnings.extend(found)
        current = [lead] if lead else []
        for kind, payload in segments:
            if kind == "rich":
                current += payload
                continue
            if current:
                blocks.append(richtext_block(current))
                current = []
            blocks.append(media_block(payload, resolve))
        if current:
            blocks.append(richtext_block(current))

    if intro and intro[0].strip():
        emit(intro[0], intro[1], None)
    for title, text, source in scenes:
        emit(text, source, {"type": "heading", "attrs": {"level": 2}, "content": [text_node(title)]})
    if errors:
        raise ContentError(errors)
    return blocks, warnings


def strip_uids(value):
    """Kopie ohne _uid, zum Vergleich zweier Bodies ueber Laeufe hinweg."""
    if isinstance(value, dict):
        return {k: strip_uids(v) for k, v in value.items() if k != "_uid"}
    if isinstance(value, list):
        return [strip_uids(v) for v in value]
    return value


def slugify(name):
    """'03 - Das Internet wird zum Lebensraum' -> '03-das-internet-wird-zum-lebensraum'."""
    title = strip_prefix(name).lower().translate(UMLAUTS)
    title = re.sub(r"[^a-z0-9]+", "-", title).strip("-")
    return f"{chapter_number(name):02d}-{title}"


def story_title(number, name):
    title = strip_prefix(name)
    return title if number == 0 else f"Kapitel {number}: {title}"


def match_story(number, stories):
    """Story zu Teil N: 0 ist die Startpage, sonst Slug mit 'NN-' am Anfang."""
    if number == 0:
        candidates = [s for s in stories if s.get("is_startpage")]
    else:
        candidates = [s for s in stories
                      if not s.get("is_startpage") and s["slug"].startswith(f"{number:02d}-")]
    if len(candidates) > 1:
        slugs = ", ".join(s["slug"] for s in candidates)
        raise ContentError([f"Teil {number}: mehrere passende Stories ({slugs})"])
    return candidates[0] if candidates else None
```

- [ ] **Step 4: Tests laufen lassen**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: alle Tests PASS

- [ ] **Step 5: Commit**

```bash
git commit -m "Storyblok-Export: Blöcke, Slugs und Zuordnung zu Stories" -- scripts/sb_content.py scripts/test_storyblok_export.py
```

---

### Task 4: Bilder finden, Rechte prüfen, Asset-Feld

**Files:**
- Modify: `scripts/sb_content.py`
- Test: `scripts/test_storyblok_export.py` (Klasse `MediaTest`)

**Interfaces:**
- Consumes: `ContentError` (Task 2)
- Produces:
  - `find_media(assets_dir: Path, name: str) -> Path`, wirft `ContentError` bei keinem oder mehreren Treffern
  - `media_meta(exif: dict, name: str) -> dict` mit Schlüsseln `alt`, `title`, `copyright`, `source`; wirft `ContentError`
  - `asset_field(asset_id: int | None, filename: str, meta: dict) -> dict`

- [ ] **Step 1: Failing tests schreiben**

```python
class MediaTest(unittest.TestCase):
    EXIF = {
        "Description": "Das ARPANET im September 1974",
        "AltTextAccessibility": "Karte der USA mit Knoten",
        "Rights": "Yngvar via Wikimedia Commons",
        "UsageTerms": "Public domain",
        "Source": "https://commons.wikimedia.org/wiki/File:Arpanet_1974.svg",
    }

    def test_media_meta(self):
        self.assertEqual(sc.media_meta(self.EXIF, "a.png"), {
            "alt": "Karte der USA mit Knoten",
            "title": "Das ARPANET im September 1974",
            "copyright": "Yngvar via Wikimedia Commons · Public domain",
            "source": "https://commons.wikimedia.org/wiki/File:Arpanet_1974.svg",
        })

    def test_media_meta_refuses_unclear_rights(self):
        for change, expected in [
            ({"UsageTerms": ""}, "Rechte ungeklärt"),
            ({"UsageTerms": "Rechte ungeklärt - vor Veröffentlichung klären"}, "Rechte ungeklärt"),
            ({"AltTextAccessibility": ""}, "Alt-Text fehlt"),
            ({"Rights": ""}, "Urheber"),
        ]:
            with self.subTest(change=change):
                exif = dict(self.EXIF, **change)
                with self.assertRaises(sc.ContentError) as ctx:
                    sc.media_meta(exif, "a.png")
                self.assertIn(expected, ctx.exception.messages[0])
                self.assertTrue(ctx.exception.messages[0].startswith("a.png: "))

    def test_media_meta_missing_everything_lists_all_problems(self):
        with self.assertRaises(sc.ContentError) as ctx:
            sc.media_meta({}, "c64.png")
        self.assertEqual(len(ctx.exception.messages), 3)

    def test_find_media(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "01").mkdir()
            (root / "02").mkdir()
            (root / "01" / "a.png").write_bytes(b"x")
            (root / "01" / "b.png").write_bytes(b"x")
            (root / "02" / "b.png").write_bytes(b"x")
            self.assertEqual(sc.find_media(root, "a.png"), root / "01" / "a.png")
            with self.assertRaises(sc.ContentError):
                sc.find_media(root, "b.png")
            with self.assertRaises(sc.ContentError):
                sc.find_media(root, "fehlt.png")

    def test_asset_field_carries_meta_as_copy(self):
        meta = sc.media_meta(self.EXIF, "a.png")
        field = sc.asset_field(42, "https://a.storyblok.com/f/330326/x/a.png", meta)
        self.assertEqual(field["id"], 42)
        self.assertEqual(field["fieldtype"], "asset")
        self.assertEqual(field["filename"], "https://a.storyblok.com/f/330326/x/a.png")
        for key in ("alt", "title", "copyright", "source"):
            self.assertEqual(field[key], meta[key])
        self.assertEqual(field["meta_data"], meta)
```

- [ ] **Step 2: Tests laufen lassen, sie müssen scheitern**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: FAIL mit `AttributeError: module 'sb_content' has no attribute 'media_meta'`

- [ ] **Step 3: Funktionen anhängen**

```python
UNCLEAR = "ungeklärt"


def find_media(assets_dir, name):
    hits = sorted(assets_dir.rglob(name))
    if not hits:
        raise ContentError([f"{name}: nicht unter assets/ gefunden"])
    if len(hits) > 1:
        raise ContentError([f"{name}: mehrfach unter assets/ ({', '.join(str(h) for h in hits)})"])
    return hits[0]


def media_meta(exif, name):
    """Asset-Metadaten aus dem XMP; verweigert Dateien ohne geklaerte Rechte.

    Leere 'Bed. f. Rechtenutzung' heisst: nicht entschieden. bild-einziehen.py
    laesst das Feld ohne --zitat bei Quellen ohne Lizenz leer (rules/bilder.md).
    """
    def field(key):
        value = exif.get(key, "")
        if isinstance(value, list):
            value = " ".join(str(v) for v in value)
        return str(value).strip()

    alt, rights, terms = field("AltTextAccessibility"), field("Rights"), field("UsageTerms")
    errors = []
    if not terms or UNCLEAR in terms.lower():
        errors.append(f"{name}: Rechte ungeklärt (Bed. f. Rechtenutzung), siehe rules/bilder.md")
    if not alt:
        errors.append(f"{name}: Alt-Text fehlt")
    if not rights:
        errors.append(f"{name}: Urheber (Copyright) fehlt")
    if errors:
        raise ContentError(errors)
    return {"alt": alt, "title": field("Description"),
            "copyright": f"{rights} · {terms}", "source": field("Source")}


def asset_field(asset_id, filename, meta):
    """Asset-Feld fuer einen Block. Die Metadaten stehen als Kopie darin, weil
    das Frontend sie am Feld liest und nicht am Asset."""
    return {"id": asset_id, "fieldtype": "asset", "filename": filename,
            "name": "", "focus": "", "is_external_url": False,
            "alt": meta["alt"], "title": meta["title"],
            "copyright": meta["copyright"], "source": meta["source"],
            "meta_data": dict(meta)}
```

- [ ] **Step 4: Tests laufen lassen**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: alle Tests PASS

- [ ] **Step 5: Commit**

```bash
git commit -m "Storyblok-Export: Bilder finden und Rechte vor dem Upload prüfen" -- scripts/sb_content.py scripts/test_storyblok_export.py
```

---

### Task 5: Client für die Management API

**Files:**
- Create: `scripts/sb_api.py`
- Test: `scripts/test_storyblok_export.py` (Klasse `ApiTest`)

**Interfaces:**
- Produces:
  - `class StoryblokError(Exception)`
  - `multipart(fields: dict, file_field: str, filename: str, data: bytes, content_type: str) -> tuple[bytes, str]`
  - `class Client(token: str, space: int, min_interval: float = 0.34, opener=urllib.request.urlopen, sleep=time.sleep)` mit
    - `request(method, path, body=None, query=None) -> dict`
    - `stories_in(prefix: str) -> list[dict]` (ohne `content`)
    - `story(story_id: int) -> dict` (mit `content`)
    - `create_story(story: dict, publish: bool) -> dict`
    - `update_story(story_id: int, story: dict, publish: bool) -> dict`
    - `asset_folders() -> list[dict]`
    - `create_asset_folder(name: str) -> dict`
    - `assets_in(folder_id: int) -> list[dict]`
    - `update_asset_meta(asset_id: int, meta: dict) -> None`
    - `upload_asset(path: Path, folder_id: int, replace_id: int | None = None) -> dict` mit `id` und `filename` (volle `https:`-URL)

API-Belege (Storyblok-Doku, geprüft am 2026-09-27):
- `GET /stories?starts_with=…&per_page=…&page=…` liefert Stories **ohne** `content`, mit `content_type`, `is_startpage`, `is_folder`, `parent_id`, `position`, `slug`, `full_slug`.
- `PUT /stories/:id` mit `{"story": {...}, "publish": bool}`; `publish: false` hebt eine bestehende Veröffentlichung nicht auf.
- `POST /assets` mit `filename`, `size`, `asset_folder_id`, optional `id` (Ersetzen), `validate_upload: 1` liefert `id`, `pretty_url`, `post_url`, `fields`. Upload per `multipart/form-data` an `post_url`, alle `fields` plus Datei im Feld `file`. Danach `GET /assets/:id/finish_upload`.
- `PUT /assets/:id` mit `{"asset": {"meta_data": {"alt", "title", "copyright", "source"}}}`.

- [ ] **Step 1: Failing tests schreiben**

Am Kopf ergänzen:

```python
import io
import json
import urllib.error

import sb_api
```

Vor `if __name__ == "__main__":` einfügen:

```python
class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def read(self):
        return self.payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class FakeOpener:
    """Nimmt Anfragen entgegen und beantwortet sie der Reihe nach."""

    def __init__(self, answers):
        self.answers = list(answers)
        self.requests = []

    def __call__(self, request):
        self.requests.append(request)
        answer = self.answers.pop(0)
        if isinstance(answer, Exception):
            raise answer
        return FakeResponse(json.dumps(answer).encode() if answer is not None else b"")


def http_error(code, body=b"nope"):
    return urllib.error.HTTPError("https://x", code, "err", {}, io.BytesIO(body))


class ApiTest(unittest.TestCase):
    def client(self, answers):
        opener = FakeOpener(answers)
        return sb_api.Client("TOKEN", 330326, min_interval=0, opener=opener, sleep=lambda s: None), opener

    def test_request_sends_token_and_json(self):
        client, opener = self.client([{"story": {"id": 7}}])
        self.assertEqual(client.update_story(7, {"name": "N"}, False), {"id": 7})
        req = opener.requests[0]
        self.assertEqual(req.get_method(), "PUT")
        self.assertEqual(req.full_url, "https://mapi.storyblok.com/v1/spaces/330326/stories/7")
        self.assertEqual(req.get_header("Authorization"), "TOKEN")
        self.assertEqual(json.loads(req.data), {"story": {"name": "N"}, "publish": False})

    def test_retry_on_429_then_error_on_other_codes(self):
        client, opener = self.client([http_error(429), {"story": {"id": 1}}])
        self.assertEqual(client.story(1), {"id": 1})
        self.assertEqual(len(opener.requests), 2)
        client, _ = self.client([http_error(422, b'{"error":"slug taken"}')])
        with self.assertRaises(sb_api.StoryblokError) as ctx:
            client.story(1)
        self.assertIn("HTTP 422", str(ctx.exception))
        self.assertIn("slug taken", str(ctx.exception))
        self.assertNotIn("TOKEN", str(ctx.exception))

    def test_paging(self):
        first = {"stories": [{"id": i} for i in range(100)]}
        second = {"stories": [{"id": 100}]}
        client, opener = self.client([first, second])
        self.assertEqual(len(client.stories_in("s/netzkultur/")), 101)
        self.assertIn("starts_with=s%2Fnetzkultur%2F", opener.requests[0].full_url)
        self.assertIn("page=2", opener.requests[1].full_url)

    def test_upload_asset_flow(self):
        signed = {"id": 55, "pretty_url": "//a.storyblok.com/f/330326/x/a.png",
                  "post_url": "https://s3.example/upload", "fields": {"key": "k", "policy": "p"}}
        client, opener = self.client([signed, None, {"id": 55}])
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "a.png"
            path.write_bytes(b"PNGDATA")
            result = client.upload_asset(path, 9)
        self.assertEqual(result, {"id": 55, "filename": "https://a.storyblok.com/f/330326/x/a.png"})
        create, upload, finish = opener.requests
        self.assertEqual(json.loads(create.data),
                         {"filename": "a.png", "size": 7, "asset_folder_id": 9, "validate_upload": 1})
        self.assertEqual(upload.full_url, "https://s3.example/upload")
        self.assertIsNone(upload.get_header("Authorization"))
        self.assertIn(b'name="key"\r\n\r\nk\r\n', upload.data)
        self.assertTrue(upload.data.index(b'name="policy"') < upload.data.index(b'name="file"'))
        self.assertIn(b"PNGDATA", upload.data)
        self.assertEqual(finish.full_url, "https://mapi.storyblok.com/v1/spaces/330326/assets/55/finish_upload")

    def test_update_asset_meta(self):
        client, opener = self.client([{}])
        client.update_asset_meta(5, {"alt": "a"})
        self.assertEqual(json.loads(opener.requests[0].data), {"asset": {"meta_data": {"alt": "a"}}})
```

- [ ] **Step 2: Tests laufen lassen, sie müssen scheitern**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: FAIL mit `ModuleNotFoundError: No module named 'sb_api'`

- [ ] **Step 3: `scripts/sb_api.py` anlegen**

```python
"""Schmaler Client fuer die Storyblok Management API. Nur Standardbibliothek.

Belege zu Endpunkten und Feldern: docs/plans/2026-09-27-storyblok-export.md, Task 5.
"""

import json
import mimetypes
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

API = "https://mapi.storyblok.com/v1/spaces/{space}"
PER_PAGE = 100
RETRIES = 5


class StoryblokError(Exception):
    pass


def multipart(fields, file_field, filename, data, content_type):
    """multipart/form-data mit den Feldern in Reihenfolge und der Datei zuletzt,
    wie S3 es fuer signierte POST-Uploads verlangt."""
    boundary = uuid.uuid4().hex
    parts = []
    for key, value in fields.items():
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n'.encode())
    parts.append(
        f'--{boundary}\r\nContent-Disposition: form-data; name="{file_field}"; filename="{filename}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n".encode() + data + b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode())
    return b"".join(parts), f"multipart/form-data; boundary={boundary}"


class Client:
    def __init__(self, token, space, min_interval=0.34, opener=urllib.request.urlopen, sleep=time.sleep):
        self.base = API.format(space=space)
        self.token = token
        self.min_interval = min_interval
        self.opener = opener
        self.sleep = sleep
        self._last = 0.0

    def _throttle(self):
        wait = self._last + self.min_interval - time.monotonic()
        if wait > 0:
            self.sleep(wait)
        self._last = time.monotonic()

    def request(self, method, path, body=None, query=None):
        url = self.base + path + ("?" + urllib.parse.urlencode(query) if query else "")
        data = json.dumps(body).encode() if body is not None else None
        for attempt in range(RETRIES + 1):
            self._throttle()
            request = urllib.request.Request(url, data=data, method=method, headers={
                "Authorization": self.token, "Content-Type": "application/json"})
            try:
                with self.opener(request) as response:
                    raw = response.read()
                    return json.loads(raw) if raw else {}
            except urllib.error.HTTPError as error:
                if error.code == 429 and attempt < RETRIES:
                    error.close()
                    self.sleep(2 ** attempt)
                    continue
                detail = error.read().decode("utf-8", "replace")[:500]
                error.close()
                raise StoryblokError(f"{method} {path}: HTTP {error.code}: {detail}") from None

    def _paged(self, path, key, query):
        items, page = [], 1
        while True:
            chunk = self.request("GET", path, query={**query, "per_page": PER_PAGE, "page": page})[key]
            items += chunk
            if len(chunk) < PER_PAGE:
                return items
            page += 1

    def stories_in(self, prefix):
        return self._paged("/stories", "stories", {"starts_with": prefix})

    def story(self, story_id):
        return self.request("GET", f"/stories/{story_id}")["story"]

    def create_story(self, story, publish):
        return self.request("POST", "/stories", {"story": story, "publish": publish})["story"]

    def update_story(self, story_id, story, publish):
        return self.request("PUT", f"/stories/{story_id}", {"story": story, "publish": publish})["story"]

    def asset_folders(self):
        return self.request("GET", "/asset_folders")["asset_folders"]

    def create_asset_folder(self, name):
        return self.request("POST", "/asset_folders", {"asset_folder": {"name": name}})["asset_folder"]

    def assets_in(self, folder_id):
        return self._paged("/assets", "assets", {"in_folder": folder_id})

    def update_asset_meta(self, asset_id, meta):
        self.request("PUT", f"/assets/{asset_id}", {"asset": {"meta_data": meta}})

    def upload_asset(self, path, folder_id, replace_id=None):
        data = path.read_bytes()
        body = {"filename": path.name, "size": len(data), "asset_folder_id": folder_id, "validate_upload": 1}
        if replace_id:
            body["id"] = replace_id
        signed = self.request("POST", "/assets", body)
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        payload, header = multipart(signed["fields"], "file", path.name, data, content_type)
        self._throttle()
        upload = urllib.request.Request(signed["post_url"], data=payload, method="POST",
                                        headers={"Content-Type": header})
        try:
            with self.opener(upload):
                pass
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", "replace")[:500]
            error.close()
            raise StoryblokError(f"Upload {path.name}: HTTP {error.code}: {detail}") from None
        self.request("GET", f"/assets/{signed['id']}/finish_upload")
        url = signed["pretty_url"]
        return {"id": signed["id"], "filename": "https:" + url if url.startswith("//") else url}
```

- [ ] **Step 4: Tests laufen lassen**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: alle Tests PASS

- [ ] **Step 5: Commit**

```bash
git add scripts/sb_api.py
git commit -m "Storyblok-Export: Client für die Management API" -- scripts/sb_api.py scripts/test_storyblok_export.py
```

---

### Task 6: Export-Ablauf und Kommandozeile

**Files:**
- Create: `scripts/sb_export.py`, `scripts/storyblok-export.py`
- Modify: `.gitignore`
- Test: `scripts/test_storyblok_export.py` (Klasse `ExportTest`)

**Interfaces:**
- Consumes: Task 1 (`read_index`, `flatten`, `chapters`, `body_of`, `strip_prefix`, `chapter_number`), Task 3/4 (`build_body`, `strip_uids`, `slugify`, `story_title`, `match_story`, `find_media`, `media_meta`, `asset_field`, `ContentError`), Task 5 (`Client`, `StoryblokError`)
- Produces:
  - `Part(number: int, name: str, intro: tuple | None, scenes: list)` (Dataclass)
  - `collect_parts(project: Path, only: int | None) -> list[Part]`
  - `read_exif(path: Path) -> dict`
  - `check_offline(parts, assets_dir) -> tuple[dict[str, tuple[Path, dict]], list[str]]`
  - `load_token(repo: Path) -> str`
  - `ensure_media(client, media, dry: bool, replace: bool) -> tuple[dict[str, dict], list[str]]`
  - `write_stories(client, pairs, fields, parent_id, dry: bool, publish: bool) -> list[str]`
  - `order_warning(stories) -> str | None`
  - `orphan_stories(stories, pairs) -> list[dict]`
  - `main(argv=None) -> int`

- [ ] **Step 1: Failing tests schreiben**

Am Kopf ergänzen:

```python
from unittest import mock

import sb_export
```

Vor `if __name__ == "__main__":` einfügen:

```python
class FakeClient:
    """Speichert Aufrufe statt sie an Storyblok zu schicken."""

    def __init__(self, stories=(), folders=(), assets=()):
        self.stories = {s["id"]: s for s in stories}
        self.folders = list(folders)
        self.assets = list(assets)
        self.calls = []

    def story(self, story_id):
        return self.stories[story_id]

    def create_story(self, story, publish):
        self.calls.append(("create_story", story, publish))
        return {"id": 999}

    def update_story(self, story_id, story, publish):
        self.calls.append(("update_story", story_id, story, publish))
        return {"id": story_id}

    def asset_folders(self):
        return self.folders

    def create_asset_folder(self, name):
        self.calls.append(("create_asset_folder", name))
        return {"id": 77, "name": name}

    def assets_in(self, folder_id):
        return self.assets

    def upload_asset(self, path, folder_id, replace_id=None):
        self.calls.append(("upload_asset", path.name, folder_id, replace_id))
        return {"id": 500, "filename": f"https://a.storyblok.com/f/330326/new/{path.name}"}

    def update_asset_meta(self, asset_id, meta):
        self.calls.append(("update_asset_meta", asset_id))


META = {"alt": "A", "title": "T", "copyright": "C · L", "source": "S"}


class ExportTest(unittest.TestCase):
    def manuscript(self, tmp):
        root = pathlib.Path(tmp)
        write_manuscript(root,
                         "    - 00 - Vorspann\n    - - 00.01 - Warum\n"
                         "    - 01 - Erstes Kapitel\n    - - 01.01 - Szene\n",
                         {"00 - Vorspann": "", "00.01 - Warum": "Darum.",
                          "01 - Erstes Kapitel": "Einleitung.", "01.01 - Szene": "Text.\n\n![[a.png]]"})
        return root

    def test_collect_parts(self):
        with tempfile.TemporaryDirectory() as tmp:
            parts = sb_export.collect_parts(self.manuscript(tmp), None)
            self.assertEqual([p.number for p in parts], [0, 1])
            self.assertIsNone(parts[0].intro)
            self.assertEqual(parts[1].intro, ("Einleitung.", "01 - Erstes Kapitel.md"))
            self.assertEqual(parts[1].scenes, [("Szene", "Text.\n\n![[a.png]]", "01.01 - Szene.md")])
            self.assertEqual([p.number for p in sb_export.collect_parts(pathlib.Path(tmp), 1)], [1])
            with self.assertRaises(sc.ContentError):
                sb_export.collect_parts(pathlib.Path(tmp), 5)

    def test_collect_parts_reports_missing_scene(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.manuscript(tmp)
            (root / "01.01 - Szene.md").unlink()
            with self.assertRaises(sc.ContentError) as ctx:
                sb_export.collect_parts(root, None)
            self.assertIn("01.01 - Szene.md fehlt", ctx.exception.messages)

    def test_check_offline_collects_media_and_refuses_bad_rights(self):
        with tempfile.TemporaryDirectory() as tmp:
            parts = sb_export.collect_parts(self.manuscript(tmp), None)
            assets = pathlib.Path(tmp) / "assets"
            (assets / "01").mkdir(parents=True)
            (assets / "01" / "a.png").write_bytes(b"x")
            with mock.patch.object(sb_export, "read_exif", return_value=MediaTest.EXIF):
                media, warnings = sb_export.check_offline(parts, assets)
            self.assertEqual(list(media), ["a.png"])
            self.assertEqual(media["a.png"][0], assets / "01" / "a.png")
            with mock.patch.object(sb_export, "read_exif", return_value={}):
                with self.assertRaises(sc.ContentError):
                    sb_export.check_offline(parts, assets)

    def test_load_token_from_env_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / ".env").write_text("OTHER=1\nSTORYBLOK_MANAGEMENT_TOKEN=\"abc\"\n", encoding="utf-8")
            with mock.patch.dict("os.environ", {}, clear=True):
                self.assertEqual(sb_export.load_token(root), "abc")
            with mock.patch.dict("os.environ", {"STORYBLOK_MANAGEMENT_TOKEN": "env"}):
                self.assertEqual(sb_export.load_token(root), "env")

    def test_ensure_media_reuses_uploads_and_creates_folder(self):
        media = {"a.png": (pathlib.Path("/x/a.png"), META), "b.png": (pathlib.Path("/x/b.png"), META)}
        existing = [{"id": 1, "filename": "https://a.storyblok.com/f/330326/old/a.png"}]
        client = FakeClient(folders=[{"id": 9, "name": "netzkultur", "parent_id": None}], assets=existing)
        fields, actions = sb_export.ensure_media(client, media, dry=False, replace=False)
        self.assertEqual(fields["a.png"]["id"], 1)
        self.assertEqual(fields["b.png"]["id"], 500)
        self.assertEqual(actions, ["b.png: hochladen"])
        self.assertIn(("upload_asset", "b.png", 9, None), client.calls)
        self.assertIn(("update_asset_meta", 1), client.calls)

        client = FakeClient()
        fields, actions = sb_export.ensure_media(client, media, dry=True, replace=False)
        self.assertEqual(client.calls, [])
        self.assertEqual(actions[0], "Asset-Ordner 'netzkultur' anlegen")
        self.assertIsNone(fields["a.png"]["id"])

    def test_write_stories_updates_only_body_name_and_pagetitle(self):
        part = sb_export.Part(1, "01 - Erstes Kapitel", None, [("Szene", "Text.", "s.md")])
        story = {"id": 11, "slug": "01-erstes-kapitel", "name": "Alt",
                 "content": {"component": "specialchapter", "pagetitle": "Alt", "abstract": "bleibt",
                             "headerpicture": {"id": 3}, "body": []}}
        client = FakeClient(stories=[story])
        report = sb_export.write_stories(client, [(part, story)], {}, parent_id=5, dry=False, publish=False)
        kind, story_id, sent, publish = client.calls[0]
        self.assertEqual((kind, story_id, publish), ("update_story", 11, False))
        self.assertEqual(sent["name"], "Kapitel 1: Erstes Kapitel")
        self.assertEqual(sent["content"]["pagetitle"], "Kapitel 1: Erstes Kapitel")
        self.assertEqual(sent["content"]["abstract"], "bleibt")
        self.assertEqual(sent["content"]["headerpicture"], {"id": 3})
        self.assertEqual(len(sent["content"]["body"]), 1)
        self.assertNotIn("slug", sent)
        self.assertTrue(report[0].startswith("Kapitel 1: Erstes Kapitel: ändern"))

    def test_write_stories_skips_unchanged_and_creates_missing(self):
        part = sb_export.Part(1, "01 - Erstes Kapitel", None, [("Szene", "Text.", "s.md")])
        body, _ = sc.build_body(None, part.scenes, lambda n: {})
        story = {"id": 11, "slug": "01-x", "name": "Kapitel 1: Erstes Kapitel",
                 "content": {"component": "specialchapter", "pagetitle": "Kapitel 1: Erstes Kapitel", "body": body}}
        client = FakeClient(stories=[story])
        report = sb_export.write_stories(client, [(part, story)], {}, parent_id=5, dry=False, publish=False)
        self.assertEqual(client.calls, [])
        self.assertEqual(report, ["Kapitel 1: Erstes Kapitel: unverändert"])

        client = FakeClient()
        sb_export.write_stories(client, [(part, None)], {}, parent_id=5, dry=False, publish=True)
        kind, sent, publish = client.calls[0]
        self.assertEqual((kind, publish), ("create_story", True))
        self.assertEqual(sent["slug"], "01-erstes-kapitel")
        self.assertEqual(sent["parent_id"], 5)
        self.assertEqual(sent["content"]["component"], "specialchapter")

        client = FakeClient()
        sb_export.write_stories(client, [(part, None)], {}, parent_id=5, dry=True, publish=False)
        self.assertEqual(client.calls, [])

    def test_order_warning_and_orphans(self):
        stories = [
            {"id": 1, "slug": "index", "is_startpage": True, "position": 0},
            {"id": 2, "slug": "02-b", "is_startpage": False, "position": 10},
            {"id": 3, "slug": "01-a", "is_startpage": False, "position": 20},
        ]
        self.assertIn("02, 01", sb_export.order_warning(stories))
        stories[1]["position"], stories[2]["position"] = 20, 10
        self.assertIsNone(sb_export.order_warning(stories))
        part = sb_export.Part(1, "01 - A", None, [])
        self.assertEqual([s["id"] for s in sb_export.orphan_stories(stories, [(part, stories[2])])], [1, 2])
```

- [ ] **Step 2: Tests laufen lassen, sie müssen scheitern**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: FAIL mit `ModuleNotFoundError: No module named 'sb_export'`

- [ ] **Step 3: `scripts/sb_export.py` anlegen**

```python
"""Manuskript nach Storyblok uebertragen: Special s/netzkultur auf meimberg.io.

Schreibt je Teil aus manuscript/Index.md den body, den Story-Namen und den
pagetitle der passenden Story. Alle anderen Felder werden in Storyblok gepflegt.
Spec: docs/specs/2026-09-27-storyblok-export-design.md

Beispiele:
    scripts/storyblok-export.py --trocken
    scripts/storyblok-export.py --kapitel 1
    scripts/storyblok-export.py --publish
"""

import argparse
import json
import os
import pathlib
import subprocess
import sys
from dataclasses import dataclass

from manuscript_index import body_of, chapter_number, chapters, flatten, read_index, strip_prefix
from sb_api import Client, StoryblokError
from sb_content import (ContentError, asset_field, build_body, find_media, match_story,
                        media_meta, slugify, story_title, strip_uids)

SPACE = 330326
FOLDER = "s/netzkultur/"
ASSET_FOLDER = "netzkultur"
EDITOR = "https://app.storyblok.com/#/me/spaces/330326/stories/0/0/{id}"
REPO = pathlib.Path(__file__).resolve().parent.parent
EXIF_TAGS = ["-XMP-dc:Description", "-XMP-iptcCore:AltTextAccessibility", "-XMP-dc:Rights",
             "-XMP-xmpRights:UsageTerms", "-XMP-photoshop:Source"]


@dataclass
class Part:
    number: int
    name: str
    intro: tuple | None
    scenes: list


def collect_parts(project, only):
    """Teile aus dem Index, only = Kapitelnummer oder None fuer alle."""
    parts, errors = [], []
    for name, kids in chapters(flatten(read_index(project))):
        number = chapter_number(name)
        if number is None:
            errors.append(f"Index: Kapitel ohne Nummer: {name}")
            continue
        if only is not None and number != only:
            continue
        intro_text = body_of(project, name)
        if intro_text is None:
            errors.append(f"{name}.md fehlt")
            continue
        scenes = []
        for kid in kids:
            text = body_of(project, kid)
            if text is None:
                errors.append(f"{kid}.md fehlt")
                continue
            scenes.append((strip_prefix(kid), text, f"{kid}.md"))
        parts.append(Part(number, name, (intro_text, f"{name}.md") if intro_text.strip() else None, scenes))
    if only is not None and not parts and not errors:
        errors.append(f"Kapitel {only} steht nicht im Index")
    if errors:
        raise ContentError(errors)
    return parts


def read_exif(path):
    result = subprocess.run(["exiftool", "-j", *EXIF_TAGS, str(path)], capture_output=True, text=True)
    if result.returncode != 0:
        raise ContentError([f"{path.name}: exiftool: {result.stderr.strip()}"])
    return json.loads(result.stdout)[0]


def check_offline(parts, assets_dir):
    """Alles pruefen, was ohne Netz geht. Liefert (medien, hinweise)."""
    names, warnings, errors = [], [], []

    def record(name):
        if name not in names:
            names.append(name)
        return {"filename": name}

    for part in parts:
        try:
            _, found = build_body(part.intro, part.scenes, record)
            warnings += found
        except ContentError as error:
            errors += error.messages
    media = {}
    for name in names:
        try:
            path = find_media(assets_dir, name)
            media[name] = (path, media_meta(read_exif(path), name))
        except ContentError as error:
            errors += error.messages
    if errors:
        raise ContentError(errors)
    return media, warnings


def load_token(repo):
    token = os.environ.get("STORYBLOK_MANAGEMENT_TOKEN")
    if token:
        return token
    env = repo / ".env"
    if env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            key, sep, value = line.partition("=")
            if sep and key.strip() == "STORYBLOK_MANAGEMENT_TOKEN":
                return value.strip().strip('"').strip("'")
    sys.exit("STORYBLOK_MANAGEMENT_TOKEN fehlt (Umgebung oder .env im Repo).")


def ensure_media(client, media, dry, replace):
    """Assets anlegen oder abgleichen. Liefert (dateiname -> Asset-Feld, aktionen)."""
    folder = next((f for f in client.asset_folders()
                   if f["name"] == ASSET_FOLDER and not f.get("parent_id")), None)
    existing = {}
    if folder:
        for asset in client.assets_in(folder["id"]):
            existing[asset["filename"].rsplit("/", 1)[-1]] = asset
    actions, fields = [], {}
    if folder is None:
        actions.append(f"Asset-Ordner '{ASSET_FOLDER}' anlegen")
        if not dry:
            folder = client.create_asset_folder(ASSET_FOLDER)
    for name, (path, meta) in media.items():
        asset = existing.get(name)
        if asset is None:
            actions.append(f"{name}: hochladen")
            if dry:
                fields[name] = asset_field(None, name, meta)
                continue
            asset = client.upload_asset(path, folder["id"])
        elif replace:
            actions.append(f"{name}: Datei ersetzen")
            if not dry:
                asset = client.upload_asset(path, folder["id"], replace_id=asset["id"])
        if not dry:
            client.update_asset_meta(asset["id"], meta)
        fields[name] = asset_field(asset["id"], asset["filename"], meta)
    return fields, actions


def write_stories(client, pairs, fields, parent_id, dry, publish):
    """body, Name und pagetitle je Teil schreiben. Liefert Berichtszeilen."""
    report = []
    for part, story in pairs:
        blocks, _ = build_body(part.intro, part.scenes, lambda name: fields[name])
        title = story_title(part.number, part.name)
        if story is None:
            slug = slugify(part.name)
            line = f"{title}: anlegen als {FOLDER}{slug} ({len(blocks)} Blöcke)"
            if not dry:
                created = client.create_story({
                    "name": title, "slug": slug, "parent_id": parent_id,
                    "content": {"component": "specialchapter", "pagetitle": title, "body": blocks},
                }, publish)
                line += f"  {EDITOR.format(id=created['id'])}"
            report.append(line)
            continue
        full = client.story(story["id"])
        content = dict(full["content"])
        changed = (full["name"] != title or content.get("pagetitle") != title
                   or strip_uids(content.get("body", [])) != strip_uids(blocks))
        if not changed and not publish:
            report.append(f"{title}: unverändert")
            continue
        verb = "ändern" if changed else "veröffentlichen"
        report.append(f"{title}: {verb} ({len(blocks)} Blöcke)  {EDITOR.format(id=story['id'])}")
        if not dry:
            content["pagetitle"] = title
            content["body"] = blocks
            client.update_story(story["id"], {"name": title, "content": content}, publish)
    return report


def chapter_stories(stories):
    return [s for s in stories if not s.get("is_startpage") and not s.get("is_folder")]


def order_warning(stories):
    """Meldung, wenn die Kapitel im Ordner nicht in Nummernfolge stehen."""
    ordered = sorted(chapter_stories(stories), key=lambda s: s.get("position", 0))
    numbers = [s["slug"][:2] for s in ordered]
    if numbers == sorted(numbers):
        return None
    return ("Reihenfolge im Ordner weicht ab: " + ", ".join(numbers)
            + ". Bitte in Storyblok per Drag-and-Drop korrigieren.")


def orphan_stories(stories, pairs):
    used = {story["id"] for _, story in pairs if story}
    return [s for s in stories if not s.get("is_folder") and s["id"] not in used]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--kapitel", type=int, metavar="N", help="nur Teil N (0 = Vorspann)")
    parser.add_argument("--trocken", action="store_true", help="nur prüfen und berichten, nichts schreiben")
    parser.add_argument("--publish", action="store_true", help="geschriebene Stories veröffentlichen")
    parser.add_argument("--bilder-ersetzen", action="store_true", help="Dateien vorhandener Assets neu hochladen")
    parser.add_argument("--projekt", type=pathlib.Path, default=REPO / "manuscript")
    args = parser.parse_args(argv)

    try:
        parts = collect_parts(args.projekt, args.kapitel)
        media, warnings = check_offline(parts, REPO / "assets")
    except ContentError as error:
        print("Abbruch, nichts geschrieben:\n  " + "\n  ".join(error.messages), file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"Hinweis: {warning}")

    client = Client(load_token(REPO), SPACE)
    try:
        stories = [s for s in client.stories_in(FOLDER) if not s.get("is_folder")]
        startpage = match_story(0, stories)
        if startpage is None:
            raise ContentError([f"Keine Startpage (special) in {FOLDER} gefunden"])
        pairs = [(part, match_story(part.number, stories)) for part in parts]
        fields, actions = ensure_media(client, media, args.trocken, args.bilder_ersetzen)
        report = write_stories(client, pairs, fields, startpage["parent_id"], args.trocken, args.publish)
    except (ContentError, StoryblokError) as error:
        print(f"Abbruch:\n  {error}", file=sys.stderr)
        return 1

    if args.trocken:
        print("Trockenlauf, nichts geschrieben.")
    for line in actions + report:
        print(line)
    if args.kapitel is None:
        for story in orphan_stories(stories, pairs):
            print(f"Ohne Gegenstück im Manuskript, unverändert: {story['full_slug']}")
        current = stories if args.trocken else [s for s in client.stories_in(FOLDER) if not s.get("is_folder")]
        warning = order_warning(current)
        if warning:
            print(warning)
    return 0
```

- [ ] **Step 4: Einstieg `scripts/storyblok-export.py` anlegen und ausführbar machen**

```python
#!/usr/bin/env python3
"""Manuskript nach Storyblok uebertragen. Details: scripts/sb_export.py."""

import sys

from sb_export import main

if __name__ == "__main__":
    sys.exit(main())
```

```bash
chmod +x scripts/storyblok-export.py
```

- [ ] **Step 5: `.env` in `.gitignore`**

An `.gitignore` anhängen:

```
# Zugangsdaten, z. B. STORYBLOK_MANAGEMENT_TOKEN fuer scripts/storyblok-export.py
.env
```

- [ ] **Step 6: Tests laufen lassen**

- Run: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`
- Expected: alle Tests PASS

- Run: `python3 scripts/storyblok-export.py --help`
- Expected: Hilfe mit `--kapitel`, `--trocken`, `--publish`, `--bilder-ersetzen`

- [ ] **Step 7: Offline-Prüfung gegen das echte Manuskript**

Ohne Token läuft das Skript bis nach der Offline-Prüfung:

```bash
env -u STORYBLOK_MANAGEMENT_TOKEN python3 scripts/storyblok-export.py --trocken
```

- Expected: Abbruch „Abbruch, nichts geschrieben“, bevor der Token gebraucht wird. Stand 2026-09-27 mit genau diesen Zeilen:
`c64.png: Rechte ungeklärt …`, `c64.png: Urheber (Copyright) fehlt`, `tracker.mp4: Rechte ungeklärt …`, `tracker.mp4: Alt-Text fehlt`, `tracker.mp4: Urheber (Copyright) fehlt`, sonst keine Fehler. Andere Fehler sind Befunde, die vor Task 9 geklärt werden.

- [ ] **Step 8: Commit**

```bash
git add scripts/sb_export.py scripts/storyblok-export.py
git commit -m "Storyblok-Export: Ablauf, Trockenlauf und Kommandozeile" -- scripts/sb_export.py scripts/storyblok-export.py scripts/test_storyblok_export.py .gitignore
```

---

### Task 7: Pflege der Regeln und des Stands

**Files:**
- Modify: `rules/werkzeuge.md` (Abschnitt „Skripte")
- Modify: `state/publikation.md` (Abschnitt „Angelegte Stories")

- [ ] **Step 1: `rules/werkzeuge.md` ergänzen**

Im Abschnitt `## Skripte` nach dem Absatz zu `scripts/kompilieren.py` einfügen:

```markdown
`scripts/storyblok-export.py` überträgt das Manuskript in das Special `s/netzkultur` auf meimberg.io: `body`, Story-Name und `pagetitle` je Kapitel, Bilder samt Nachweis als Assets. Alle anderen Felder pflegt Oli in Storyblok. Standard ist Entwurf, `--publish` veröffentlicht, `--trocken` schreibt nichts. Ein Bild ohne Alt-Text, Urheber oder entschiedene Rechtenutzung bricht den Lauf ab. Den Index lesen beide Skripte über `scripts/manuscript_index.py`. Aufbau und Entscheidungen: `docs/specs/2026-09-27-storyblok-export-design.md`.
```

- [ ] **Step 2: `state/publikation.md` ergänzen**

Am Ende des Abschnitts `## Angelegte Stories` einen Absatz anhängen:

```markdown
Seit 2026-09-27 erzeugt `scripts/storyblok-export.py` den Inhalt dieser Stories aus `manuscript/`. Die Handübertragung der Gemini-Entwürfe vom 2026-07-30 ist damit überholt; was dort noch im `body` steht, wird beim ersten Lauf ersetzt.
```

- [ ] **Step 3: Kontext-Lint**

- Run: `python3 scripts/kontext-lint.py`
- Expected: `Kontext-Architektur in Ordnung` ohne Hinweise. Meldet der Lint eine Längengrenze für `werkzeuge.md`, den neuen Absatz kürzen, nicht an anderer Stelle streichen.

- [ ] **Step 4: Commit**

```bash
git commit -m "Werkzeuge und Publikationsstand kennen den Storyblok-Export" -- rules/werkzeuge.md state/publikation.md
```

---

### Task 8: Nachweise auf meimberg.io anzeigen

Arbeitsverzeichnis: `/Users/oli/workspace-meimbergio/io.meimberg.www`

**Files:**
- Create: `src/components/elements/AssetCredit.tsx`
- Modify: `src/components/elements/Picture.tsx`, `src/components/elements/Gallery.tsx`, `src/components/elements/Video.tsx`

**Interfaces:**
- Consumes: Asset-Felder mit `alt`, `title`, `copyright`, `source` (Task 4, `asset_field`)
- Produces: `AssetCredit({ assets, showTitle }: { assets: StoryblokAsset[]; showTitle?: boolean })`

Das Repo hat keine Unittests für Komponenten; geprüft wird mit `npx tsc --noEmit`, `npm run lint` und im Browser.

- [ ] **Step 1: Ausgangslage prüfen**

- Run: `npx tsc --noEmit && npm run lint`
- Expected: ohne Fehler. Gibt es schon vorher Fehler, sie notieren, damit Step 6 nur neue Fehler bewertet.

- [ ] **Step 2: `src/components/elements/AssetCredit.tsx` anlegen**

```tsx
import { StoryblokAsset } from '@/types/component-types-sb'

type AssetCreditProps = {
	assets: StoryblokAsset[]
	showTitle?: boolean
}

// Bildunterschrift und Nachweis aus den Asset-Feldern. Ohne title und copyright
// rendert nichts, damit bestehende Bilder im Blog unverändert bleiben.
export default function AssetCredit({ assets, showTitle = true }: AssetCreditProps) {
	const title = showTitle && assets.length === 1 ? assets[0].title : undefined
	const credits: { text: string; source?: string }[] = []
	for (const asset of assets) {
		if (!asset.copyright || credits.some((c) => c.text === asset.copyright)) continue
		credits.push({ text: asset.copyright, source: asset.source || undefined })
	}
	if (!title && credits.length === 0) return null

	return (
		<figcaption className="mt-3 text-sm leading-6 text-zinc-500 dark:text-zinc-400">
			{title && <span>{title}</span>}
			{credits.map((credit, i) => (
				<span key={i} className="block text-xs">
					{credit.source ? (
						<a href={credit.source} target="_blank" rel="noopener noreferrer" className="underline">
							{credit.text}
						</a>
					) : (
						credit.text
					)}
				</span>
			))}
		</figcaption>
	)
}
```

- [ ] **Step 3: `Picture.tsx` umstellen**

In `src/components/elements/Picture.tsx`:

1. Import ergänzen: `import AssetCredit from '@/components/elements/AssetCredit.tsx'`
2. In allen drei Varianten (`keyvisual`, `small`, Standard) das `alt=""` des Hauptbildes ersetzen durch `alt={blok.image?.alt ?? ''}`. Das `alt=""` in `renderLightboxSlide` bleibt.
3. In allen drei Varianten den inneren `<div {...storyblokEditable(blok)} className="">` zu `<figure {...storyblokEditable(blok)} className="">` machen (schließendes Tag ebenso) und direkt vor dem schließenden `</figure>` einfügen:

```tsx
					<AssetCredit assets={blok.image ? [blok.image] : []} />
```

- [ ] **Step 4: `Gallery.tsx` umstellen**

In `src/components/elements/Gallery.tsx`:

1. Import ergänzen: `import AssetCredit from '@/components/elements/AssetCredit.tsx'`
2. Über der Komponente die feste Spaltenzuordnung einfügen:

```tsx
// Feste Klassen statt String-Verkettung, damit Tailwind sie beim Build findet.
const COLUMN_CLASSES: Record<string, string> = {
	'1': 'md:grid-cols-1 lg:grid-cols-1',
	'2': 'md:grid-cols-2 lg:grid-cols-2',
	'3': 'md:grid-cols-3 lg:grid-cols-3',
	'4': 'md:grid-cols-4 lg:grid-cols-4'
}
```

3. `const cols = 'md:grid-cols-' + blok.columns + ' lg:grid-cols-' + blok.columns` ersetzen durch:

```tsx
	const cols = COLUMN_CLASSES[String(blok.columns)] ?? COLUMN_CLASSES['3']
```

4. `alt="gallery-photo"` ersetzen durch `alt={asset.alt || 'gallery-photo'}`.
5. Direkt nach dem schließenden `</div>` des Grids (vor `<Lightbox`) einfügen:

```tsx
				<AssetCredit assets={images} showTitle={false} />
```

- [ ] **Step 5: `Video.tsx` umstellen**

In `src/components/elements/Video.tsx`:

1. Import ergänzen: `import AssetCredit from '@/components/elements/AssetCredit.tsx'`
2. Direkt nach dem schließenden `</div>` des Players, noch innerhalb von `<ElementWrapper>`, einfügen:

```tsx
      <AssetCredit assets={blok.file ? [blok.file] : []} />
```

- [ ] **Step 6: Typen und Lint**

- Run: `npx tsc --noEmit && npm run lint`
- Expected: keine neuen Fehler gegenüber Step 1. Meldet TypeScript, dass `alt`, `title`, `copyright` oder `source` auf `StoryblokAsset` fehlen, `AssetCredit` mit einem lokalen Typ `type CreditAsset = StoryblokAsset & { alt?: string | null; title?: string | null; copyright?: string | null; source?: string | null }` arbeiten lassen und die Props darauf umstellen.

- [ ] **Step 7: Im Browser prüfen**

Dev-Server über `preview_start` (Browser-Pane) starten, falls keine `.claude/launch.json` existiert mit `npm run dev` auf Port 3000 anlegen. Eine bestehende Blogseite mit Bild öffnen:
- Bild sieht aus wie vorher, keine Unterschrift, wenn das Asset kein `title`/`copyright` hat.
- Eine Seite mit `gallery` zeigt dieselbe Spaltenzahl wie vorher.

Die Special-Seiten mit Nachweisen werden in Task 9 geprüft, sobald die Inhalte in Storyblok stehen.

- [ ] **Step 8: Commit im Website-Repo**

`git log --oneline -10` ansehen und den Stil übernehmen.

```bash
git add src/components/elements/AssetCredit.tsx
git commit -m "Bilder, Bildreihen und Videos zeigen Bildunterschrift und Nachweis aus dem Asset" -- src/components/elements/AssetCredit.tsx src/components/elements/Picture.tsx src/components/elements/Gallery.tsx src/components/elements/Video.tsx
```

Nicht pushen. Oli entscheidet über das Deployment; es muss live sein, bevor das Special mit `--publish` veröffentlicht wird.

---

### Task 9: Erster Lauf gegen Storyblok

Dieser Task schreibt in Olis CMS und braucht seine ausdrückliche Zustimmung vor Step 3 und vor Step 5. Keine Veröffentlichung in diesem Task.

- [ ] **Step 1: Voraussetzungen mit Oli klären**

Oli fragen:
- Token: legt er `.env` mit `STORYBLOK_MANAGEMENT_TOKEN=…` im Repo an, oder darf der Wert aus `io.meimberg.contentmanager/.env` in die gitignorte `.env` dieses Repos kopiert werden? Den Wert nie ausgeben.
- Rechte für `c64.png` und `tracker.mp4` (und jedes weitere Medium, das die Offline-Prüfung meldet): trägt Oli sie mit `bild-einziehen.py` bzw. `exiftool` nach, oder sollen die Einbindungen vorerst aus dem Manuskript? Das Manuskript ändert nur Oli.

Weiter erst, wenn die Offline-Prüfung (Task 6, Step 7) keine Fehler mehr meldet.

- [ ] **Step 2: Trockenlauf über das ganze Buch**

- Run: `python3 scripts/storyblok-export.py --trocken`
- Expected: 18 Hinweise „offener Bildplatz übersprungen“, `Asset-Ordner 'netzkultur' anlegen`, eine Zeile „hochladen“ je verwendetem Medium, acht Stories „ändern“, keine „anlegen“, keine verwaisten Stories, keine Reihenfolge-Warnung. Ergebnis Oli zeigen.

- [ ] **Step 3: Nach Zustimmung Kapitel 1 als Entwurf schreiben**

- Run: `python3 scripts/storyblok-export.py --kapitel 1`
- Expected: Assets von Kapitel 1 hochgeladen, `Kapitel 1: Bevor das Internet ein öffentlicher Ort war: ändern (… Blöcke)` mit Editor-Link.

- [ ] **Step 4: In der Storyblok-Vorschau prüfen, gemeinsam mit Oli**

Editor-Link öffnen:
- Szenentitel als H2, `###` als H3.
- Bilder an der richtigen Stelle; die Demoszene-Screenshots als Bildreihe; `tracker.mp4` als Video.
- Unter jedem Bild Unterschrift und Nachweis (setzt Task 8 im Vorschau-Deployment voraus).
- Kapitelleiste und Verzeichnis unverändert, Kopfbild und Abstract unverändert.

- Dann ohne Änderung erneut: `python3 scripts/storyblok-export.py --kapitel 1`
- Expected: kein Upload, `Kapitel 1: …: unverändert`. Meldet der zweite Lauf „ändern“, normalisiert Storyblok den gespeicherten Body anders als erzeugt: gespeicherten und erzeugten Body per `client.story(id)` vergleichen, die Abweichung in `strip_uids` bzw. einer Normalisierung in `sb_content.py` mit Test abfangen, dann wiederholen.

- [ ] **Step 5: Nach Zustimmung das ganze Buch als Entwurf**

- Run: `python3 scripts/storyblok-export.py`
- Expected: acht Stories geändert, keine Warnungen außer den offenen Bildplätzen.

- [ ] **Step 6: Abschluss**

`git log origin/main..HEAD --oneline` in beiden Repos ansehen und Oli die ungepushten Commits nennen. Veröffentlichen mit `--publish` entscheidet Oli, sobald Task 8 live ist.
