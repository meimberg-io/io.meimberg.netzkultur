# Netzkultur — Eine Retrospektive

> Eine Kulturgeschichte des Netzes von Mailboxen und Modems bis TikTok, Brainrot und KI.
> Dieses Repo ist die Produktionsumgebung des Buches: Text, Quellen, Bilder, Prüfapparat.
> Diese Datei wird in jeder Session geladen und ist deshalb **nur ein Wegweiser**.

**Sprache:** Deutsch in allen Inhalten und in der Kommunikation. Code und Identifier englisch.

---

## Wo was liegt

| Verzeichnis | Inhalt |
|---|---|
| `chapters/` | Das Longform-Projekt. `Index.md` plus eine Datei je Abschnitt, `manuscript.md` ist das Kompilat |
| `drafts/kapitel/` | Die Ursprungsfassungen `01.md` bis `07.md`, aus denen die Szenen geschnitten wurden. Vollständig überführt, können weg, sobald das Ergebnis geprüft ist. **Nicht** weiterschreiben, die Wahrheit liegt in `chapters/` |
| `drafts/` | Kürzere Texte und Snippets rund um das Buch |
| `sources/` | Quellen-Snapshots, 1:1-Kopien. Herkunft je Datei in `sources/sources.md` |
| `assets/` | Bilder. Metadaten werden über den Lightroom-Katalog in `lightroom/` gepflegt |
| `notes/` | `decisions.md` (getroffene Entscheidungen), `issues.md` und `<NN>_issues.md` (offene Punkte), `kandidaten.md` (Stoff, der noch nicht drin ist) |
| `memory/` | `fakten.md` (bestätigte Fakten), `ton.md` (Formulierungsfallen), `bilder.md` (Metadaten und Rechte), `quellen.md` (Bewertung der Quellen), `redaktions-workflow.md`, `oli.md` |
| `longform-scripts/` | Eigene Longform-Compile-Steps, die das Plugin selbst lädt |
| `scripts/` | Repo-Werkzeuge: Prüftexte bauen, Bilder mit Lightroom-Metadaten einziehen |

## Wie Longform hier funktioniert

**Der Dateiname ist die Überschrift.** Der Compile-Step „Prepend Title" erzeugt sie aus dem
Szenennamen, das Format `$3{#} $1` macht aus der Einrückungstiefe die Überschriftenebene. Deshalb
steht in den Szenendateien selbst keine Überschrift. Wer eine Überschrift ändern will, benennt die
Datei um, nicht den Text.

**`Index.md` ist die einzige Wahrheit für Zugehörigkeit und Reihenfolge.** Auf der Platte liegen
alle Szenen flach in `chapters/`, die Verschachtelung existiert nur im Index. Longform pflegt ihn
beim Umsortieren selbst. Diese Information gehört deshalb an keinen zweiten Ort, insbesondere nicht
ins Frontmatter: eine Kopie wäre beim ersten Verschieben veraltet.

**Frontmatter trägt nur, was pro Datei gilt:** `status` (`draft`, `review`, `final`) und `comment`
für eine kurze redaktionelle Notiz. `strip-frontmatter` ist der erste Compile-Step, das landet also
nie im Manuskript.

**Ordnungspräfixe** im Dateinamen (`1.03 - Titel`) sind erlaubt, damit die Dateien im Dateisystem
sortiert und auch ausserhalb von Obsidian navigierbar sind. Der Step
`longform-scripts/strip-order-prefix.js` schneidet sie beim Kompilieren aus der Überschrift und
meldet, wenn die Nummern nicht zur Projektreihenfolge passen. Zweistellig nummerieren, sonst
sortiert das Dateisystem `1.10` vor `1.2`. Gültiges Schema: Kapitel `NN - Titel`, Abschnitt
`NN.MM - Titel`.

**Der Compile-Workflow** („Default Workflow") in dieser Reihenfolge, weil ein Agent die
Longform-Oberfläche nicht sehen kann:

1. `strip-frontmatter` — deshalb landet `status`/`comment` nie im Manuskript
2. `remove-links` — entfernt Wiki- **und** externe Links, also **auch alle Bilder**
3. `prepend-title` mit Format `$3{#} $1` — Überschrift aus Dateiname und Einrückungstiefe
4. „Ordnungspräfix entfernen" (eigener Step) — muss **nach** `prepend-title` stehen
5. `concatenate-text`, Trenner `\n\n---\n\n`
6. `write-to-note` nach `manuscript.md`

Schritt 2 ist eine Falle: das Kompilat enthält keine Bilder. Solange das Manuskript nur zum
Gegenlesen dient, ist das in Ordnung; für eine Ausgabe mit Bildern müsste `remove-wikilinks`
aus.

## Werkzeuge

**Prüftext bauen:** `scripts/kapitel-kompilieren.py` setzt Szenen anhand von `Index.md` zusammen
und liefert genau die drei Zuschnitte der Prüfebenen:

```
scripts/kapitel-kompilieren.py --kapitel 3     # ein Kapitel, für kohaerenz und plausibilitaet
scripts/kapitel-kompilieren.py --naht 1        # Ende Kapitel 1 + Anfang Kapitel 2
scripts/kapitel-kompilieren.py --abriss        # Überschriftenbaum, je zwei Sätze
```

Ohne Argument kommt das ganze Buch. Longform selbst kann nur den kompletten Draft kompilieren,
deshalb dieses Skript.

**Bilder besorgen:** der Agent `bildsuche` sucht Bilder zu einer Textstelle, klärt Urheber und
Lizenz an der Quelle und zieht sie mit `scripts/bild-einziehen.py` samt Metadaten ein. Er ist der
einzige Agent hier, der nicht prüft, sondern etwas herstellt. Regeln und Fallen:
[memory/bilder.md](memory/bilder.md).

## Prüfen

Fünf Agenten in `.claude/agents/`, jeder mit genau einer Linse, weil zusammengelegte Prüfungen sich
gegenseitig verdrängen: **`klarheit`** (versteht der Leser den Satz beim ersten Lesen),
**`sprache`** (Betonung, Wortwahl, Bilder), **`kohaerenz`** (Aufbau, Anschlüsse, Widersprüche),
**`plausibilitaet`** (Anachronismen, Größenordnungen, Belegliste), **`faktencheck`** (Recherche).
Welcher wann läuft: [memory/redaktions-workflow.md](memory/redaktions-workflow.md).

Geprüft wird auf drei Ebenen, weil ein Abschnitt allein die Anschlüsse nicht zeigt:

1. **Abschnitt** — `klarheit` und `sprache` auf die einzelne Szenendatei.
2. **Kapitel** — `kohaerenz` und `plausibilitaet` auf die Szenen eines Kapitels in der Reihenfolge
   aus `Index.md`, zusammengefügt. Ein Abschnitt für sich kann schlüssig sein und trotzdem nicht an
   den vorigen anschließen.
3. **Reihe** — die Nähte zwischen den Kapiteln (letzte Szene von N mit erster von N+1) und ein
   Struktur-Abriss über alles. Findet Dopplungen und Widersprüche über Distanz.

Der Hook [`.claude/hooks/redaktion-lint.py`](.claude/hooks/redaktion-lint.py) prüft jede
Schreiboperation unter `chapters/` und `drafts/` mechanisch auf lange Gedankenstriche.

---

## Konventionen

- **Nie lokal am Satz redigieren.** Vor der Änderung den Abschnitt lesen, bei Strukturfragen das
  Kapitel und die Einleitung. Danach prüfen, was die Änderung woanders zerrissen hat. Der
  Prüfradius richtet sich nach der Größe der Änderung.
- **Diskussion ist nicht Text.** Was Oli im Gespräch sagt, ist Begründung. In den Text gehört kein
  Satz, der eine Behauptung verneint, die nur in einer Vorfassung stand. Prüfen: Stünde dieser Satz
  auch da, wenn wir nie darüber geredet hätten?
- **Quellen reinkopieren, nicht verlinken.** Ein Pointer wird beim Materialsammeln nie konsultiert,
  eine lokale Kopie schon. Snapshots nach `sources/`, Herkunft in `sources/sources.md`. Staleness
  ist okay, solange die Herkunft dransteht.
- **Offene Punkte sofort festhalten** → `notes/<NN>_issues.md`, nicht nur im Chat und nicht in
  `decisions.md`. Dort steht, was entschieden ist, nicht was offen ist.
- **Bestätigte Fakten** → `memory/fakten.md`, sobald Oli einen Sachverhalt bestätigt. Gilt gegen
  anderslautendes Modellwissen.
- **Bildrechte:** keine Lizenz erfinden, Herkunft nie weglassen. Findet sich keine
  Lizenzangabe, entscheidet Oli pro Bild, ob es als Bildzitat läuft; bis dahin trägt die
  Datei den Marker „Rechte ungeklärt". Details in [memory/bilder.md](memory/bilder.md).
- **Texte nicht committen.** Oli committet redaktionelle Änderungen selbst. Werkzeuge, Skripte und
  Konfiguration dagegen schon.
