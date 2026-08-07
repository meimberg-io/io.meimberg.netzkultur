---
role: rule
readers: claude
when: beim Kompilieren und beim Ändern der Longform-Konfiguration
mode: full
agent-visible: no
---

# Werkzeugkette

Was ein Agent an diesem Repo nicht sehen kann, weil es in der Obsidian-Oberfläche steckt.

## Longform

**Der Dateiname ist die Überschrift.** Der Compile-Step „Prepend Title" erzeugt sie aus dem Szenennamen, das Format `$3{#}  $1` macht aus der Einrückungstiefe die Überschriftenebene. Deshalb steht in den Szenendateien selbst keine Überschrift. Wer eine ändern will, benennt die Datei um.

**`text/Index.md` ist die einzige Wahrheit für Zugehörigkeit und Reihenfolge.** Auf der Platte liegen alle Szenen flach in `text/`, die Verschachtelung existiert nur im Index. Longform pflegt ihn beim Umsortieren selbst. Diese Information gehört an keinen zweiten Ort, insbesondere nicht ins Frontmatter der Szenen.

**Ordnungspräfixe** im Dateinamen (`01.03 - Titel`) sind erlaubt, damit die Dateien auch außerhalb von Obsidian sortiert sind. `longform-scripts/strip-order-prefix.js` schneidet sie beim Kompilieren aus der Überschrift und meldet, wenn die Nummern nicht zur Projektreihenfolge passen.

## Der Compile-Workflow

„Default Workflow", in dieser Reihenfolge:

1. `strip-frontmatter`, deshalb landen `status` und `comment` nie im Manuskript
2. `remove-links`, entfernt Wiki- **und** externe Links, also **auch alle Bilder**
3. `prepend-title` mit Format `$3{#}  $1`
4. „Ordnungspräfix entfernen" (eigener Step), muss **nach** `prepend-title` stehen, sonst greift er ins Leere: vorher existiert die Überschrift noch nicht. Bei Hauptkapiteln setzt er an die Stelle des Präfixes eine laufende Kapitelnummer (`$2`); der Vorspann als erste Szene bleibt ohne. Das kann `prepend-title` nicht selbst, weil sein `$2` alle Ebenen träfe. Die Nummer wird gezählt, nicht aus dem Dateinamen gelesen: Fehlt ein Kapitel im Index, läuft sie gegen das Ordnungspräfix.
5. `concatenate-text`, Trenner `\n\n---\n\n`
6. `write-to-note` nach `manuscript.md`

Schritt 2 ist die Falle: Das Kompilat enthält keine Bilder. Solange `manuscript.md` nur zum Gegenlesen dient, ist das in Ordnung; für eine Ausgabe mit Bildern müsste `remove-links` heraus.

## Skripte

`scripts/kompilieren.py` baut die drei Prüfzuschnitte (`--kapitel`, `--naht`, `--abriss`) aus `text/Index.md`. Longform selbst kann nur den kompletten Draft kompilieren, deshalb dieses Skript.

`scripts/kontext-lint.py` prüft die Verträge dieses Repos; seine eigenen Tests liegen im Template-Repo `io.meimberg.writer`. Bilder zieht `scripts/bild-einziehen.py` ein, Regeln in [bilder.md](bilder.md).
