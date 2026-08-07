# Netzkultur — Eine Retrospektive

> Eine Kulturgeschichte des Netzes von Mailboxen und Modems bis TikTok, Brainrot und KI.
> Dieses Repo ist die Produktionsumgebung des Buches: Text, Quellen, Bilder, Prüfapparat.
> Diese Datei wird in jeder Session geladen und ist deshalb **nur ein Wegweiser**.

**Sprache:** Deutsch in allen Inhalten und in der Kommunikation. Code und Identifier englisch.

---

## Die Kontext-Architektur

Jede Datei außerhalb von `chapters/` gehört zu genau **einem** Moment im Ablauf. Der Moment steht im
Frontmatter der Datei, und `scripts/kontext-lint.py` hält das durch. Eine Datei ohne Leser wird
verdrahtet oder gelöscht: So ist `memory/digest.md` neun Monate lang unbemerkt tot gewesen, während
die Kapitel ohne ihr Material geschrieben wurden.

| Ebene | Frage | Modus | Wer lädt |
|---|---|---|---|
| `rules/` | Wie wird gearbeitet? | **ganz gelesen**, max. 150 Zeilen | die Skills, deterministisch |
| `research/` | Welcher Stoff liegt vor? | durchsucht | `editor-outline`, `editor-write`, `copyedit-facts` |
| `memory/` | Was ist gesichert wahr? | durchsucht | die Fakten-Linsen |
| `notes/` | Wo stehen wir? | durchsucht | ich, zwischen den Läufen |
| `sources/` | Was ist das Rohmaterial? | 1:1-Kopien | beim Materialsammeln |

**Die Asymmetrie ist Absicht.** Beim **Schreiben** wird Material geladen und keine Verbotsliste. Beim
**Prüfen** laufen die Verbotslisten, und die Linsen sehen sonst nichts. Ein Agent, der sieben Dinge
vermeiden muss, schreibt um Formulierungen herum statt zur Sache hin; ein Absatz ohne Stoff wird
durch keine Regel gut.

| Datei | Inhalt |
|---|---|
| `rules/schreiben.md` | Arbeitsweise und was im Text gilt. Vor dem ersten Satz |
| `rules/haltung.md` | Erzählhaltung, Publikum, Ton |
| `rules/pruefen.md` | Welche Linse wann, Blindheitsregeln, was die Agenten sehen dürfen |
| `rules/bilder.md` | Rechteregel und die Fallen der Metadaten |
| `research/<NN>.md` | Dossier pro Kapitel: recherchiertes Material mit Herkunft |
| `research/quellen.md` | Welche Quelle taugt wofür: Belegapparat, Zeitzeuge, Steinbruch |
| `memory/fakten.md` | Von Oli bestätigt, gilt gegen Modellwissen |
| `notes/issues.md`, `notes/<NN>_issues.md` | Offene Punkte, werkweit und pro Kapitel |
| `notes/decisions.md` | Abgelehnte Befunde. Filter nach einem Prüflauf, nie beim Schreiben |
| `notes/kandidaten.md` | Stoff, der noch nicht drin ist |
| `notes/publikation.md` | Zielplattform und Stand |

## Wo der Text liegt

| Verzeichnis | Inhalt |
|---|---|
| `chapters/` | Das Longform-Projekt. `Index.md` plus eine Datei je Abschnitt, `manuscript.md` ist das Kompilat |
| `drafts/kapitel/` | Die Ursprungsfassungen `01.md` bis `07.md`. Vollständig überführt. **Nicht** weiterschreiben, die Wahrheit liegt in `chapters/` |
| `drafts/` | Kürzere Texte und Snippets rund um das Buch |
| `sources/` | Quellen-Snapshots, 1:1-Kopien. Herkunft je Datei in `sources/sources.md` |
| `assets/` | Bilder. Metadaten werden über den Lightroom-Katalog in `lightroom/` gepflegt |
| `longform-scripts/` | Eigene Longform-Compile-Steps, die das Plugin selbst lädt |
| `scripts/` | Repo-Werkzeuge: Prüftexte bauen, Bilder einziehen, Kontext prüfen |

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
4. „Ordnungspräfix entfernen" (eigener Step) — muss **nach** `prepend-title` stehen, sonst
   greift er ins Leere: vorher existiert die Überschrift noch gar nicht. Bei Hauptkapiteln
   setzt er an die Stelle des Präfixes eine laufende Kapitelnummer (Option „Nummer bei
   Hauptkapiteln", `$2`); der Vorspann als erste Szene bleibt ohne. Das kann `prepend-title`
   nicht selbst, weil sein `$2` alle Ebenen träfe und den Vorspann als 1 zählt. Die Nummer
   wird gezählt, nicht aus dem Dateinamen gelesen — fehlt ein Kapitel im Index, läuft sie
   gegen das Ordnungspräfix.
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

**Kontext prüfen:** `scripts/kontext-lint.py` prüft, ob jede Datei unter `rules/`, `research/`,
`memory/` und `notes/` einen Leser hat, ob dieser Leser sie tatsächlich lädt, ob kein Skill auf einen
toten Pfad zeigt und ob die Regeldateien kurz genug zum Ganzlesen sind. Nach jeder Änderung an der
Kontext-Ebene laufen lassen.

**Bilder besorgen:** der Agent `editor-images` sucht Bilder zu einer Textstelle, klärt Urheber und
Lizenz an der Quelle und zieht sie mit `scripts/bild-einziehen.py` samt Metadaten ein. Er ist der
einzige Agent hier, der nicht prüft, sondern etwas herstellt. Regeln und Fallen:
[rules/bilder.md](rules/bilder.md).

## Wie Skills, Agenten und Commands hier zusammenhängen

Das Verfahren steht im **Skill**, die Kontextlosigkeit im **Agenten**, der Aufruf im **Command**. Ein
Agent ist nichts anderes als ein Skill ohne Projektwissen: Er lädt denselben Skill und weiß sonst
nichts. Deshalb gilt für die Aufteilung nur eine Frage: Muss die Arbeit blind sein oder nicht?

- **`editor-outline`** und **`editor-write`** laufen im Kontext, weil sie das Projekt kennen müssen.
  Nur Skill, kein Agent.
- Die fünf Lektorat-Linsen laufen alle über **einen** Agenten, `copyedit`. Der Auftrag nennt den
  Skill. Die Isolation entsteht durch den einzelnen Aufruf und nicht durch eine eigene Datei je
  Linse: Fünfmal `copyedit` aufrufen sind fünf frische Kontexte. Blindheit ist hier die Funktion, ein
  Prüfer, der weiß, was gemeint war, prüft nichts.
- Ein Agent ist eine **Rolle**, kein Berechtigungsprofil. Dass `copyedit-plausibility` nicht
  recherchieren darf, steht im Skill und nicht in einem eigenen Agenten mit anderem Werkzeugset.
- **`editor-free`** behält seine Methode im Agenten. Ein Skill wäre in meinem Kontext, und damit wäre
  der Agent nicht mehr frei.
- Zu jedem Skill gibt es einen gleichnamigen Command in `.claude/commands/`.

## Schreiben

**`/editor-outline`** baut erst das Inhalts-Skelett aus dem Kapitel-Dossier, das Oli prüft, bevor
Prosa entsteht. **`/editor-write`** formuliert daraus in einem Zug gegen [rules/haltung.md](rules/haltung.md)
und [rules/schreiben.md](rules/schreiben.md) und legt den Text dann vor. Die Outline ist Planung,
nicht Gliederung: Wer sie Punkt für Punkt in Sätze übersetzt, bekommt Staccato. Die Linsen startet
Oli selbst, sie laufen nicht automatisch hinterher.

## Prüfen

Fünf Linsen, jede allein, weil zusammengelegte Prüfungen sich gegenseitig verdrängen:
**`/copyedit-clarity`** (versteht der Leser den Satz beim ersten Lesen),
**`/copyedit-language`** (Betonung, Wortwahl, Bilder), **`/copyedit-coherence`** (Aufbau, Anschlüsse,
Widersprüche), **`/copyedit-plausibility`** (Anachronismen, Größenordnungen, Belegliste),
**`/copyedit-facts`** (Recherche). Welche wann läuft und was die Agenten sehen dürfen:
[rules/pruefen.md](rules/pruefen.md).

Geprüft wird auf drei Ebenen, weil ein Abschnitt allein die Anschlüsse nicht zeigt:

1. **Abschnitt** — `copyedit-clarity` und `copyedit-language` auf die einzelne Szenendatei.
2. **Kapitel** — `copyedit-coherence` und `copyedit-plausibility` auf die Szenen eines Kapitels in der Reihenfolge
   aus `Index.md`, zusammengefügt. Ein Abschnitt für sich kann schlüssig sein und trotzdem nicht an
   den vorigen anschließen.
3. **Reihe** — die Nähte zwischen den Kapiteln (letzte Szene von N mit erster von N+1) und ein
   Struktur-Abriss über alles. Findet Dopplungen und Widersprüche über Distanz.

Der Hook [`.claude/hooks/redaktion-lint.py`](.claude/hooks/redaktion-lint.py) prüft jede
Schreiboperation unter `chapters/` und `drafts/` mechanisch auf lange Gedankenstriche.

---

## Was in jeder Session gilt

Alles Weitere steht in `rules/` und wird dort geladen, wo es gebraucht wird. Hier stehen nur die vier
Regeln, für die es keinen späteren Leser gibt:

- **Texte nicht committen.** Oli committet redaktionelle Änderungen selbst. Werkzeuge, Skripte und
  Konfiguration dagegen schon.
- **Offene Punkte sofort festhalten** → `notes/<NN>_issues.md`, nicht nur im Chat und nicht in
  `decisions.md`. Dort steht, was entschieden ist, nicht was offen ist.
- **Bestätigte Fakten** → `memory/fakten.md`, sobald Oli einen Sachverhalt bestätigt. Recherchiertes
  Material dagegen → `research/<NN>.md`, sofort beim Finden, mit Herkunft am Eintrag.
- **Quellen reinkopieren, nicht verlinken.** Ein Pointer wird beim Materialsammeln nie konsultiert,
  eine lokale Kopie schon. Snapshots nach `sources/`, Herkunft in `sources/sources.md`. Staleness
  ist okay, solange die Herkunft dransteht.
