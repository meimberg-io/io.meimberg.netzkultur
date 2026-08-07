# Netzkultur — Eine Retrospektive

> Eine Kulturgeschichte des Netzes von Mailboxen und Modems bis TikTok, Brainrot und KI.
> Produktionsumgebung des Werks: Text, Material, Bilder, Prüfapparat.

**Sprache:** Deutsch in allen Inhalten und in der Kommunikation. Code und Identifier englisch.

## Karte

| Verzeichnis | Rolle | Ladeverhalten | Inhalt |
|---|---|---|---|
| `rules/` | `rule` | **ganz**, vor dem Handeln | `stimme.md` Klang · `form.md` Format · `arbeitsweise.md` Verfahren · `pruefen.md` Prüfung · `bilder.md` · `werkzeuge.md` Longform |
| `knowledge/` | `knowledge` | Abfrage | `fakten.md`, von Oli bestätigt, schlägt Modellwissen |
| `material/` | `material` | Abfrage | `dossier-<NN>.md` je Kapitel · `quellen.md` Bewertung · `quellen/` Snapshots · `kandidaten.md` |
| `state/` | `state` | Abfrage | `decisions.md` abgelehnte Befunde · `issues.md`, `issues-<NN>.md` · `publikation.md` |
| `manuscript/` |  |  | Das Buch. `Index.md` plus eine Datei je Szene, `kompilat.md` ist das zusammengesetzte Ganze |
| `assets/` · `scripts/` |  |  | Bilder mit Metadaten · `kompilieren.py`, `kontext-lint.py`, `bild-einziehen.py` |
| `beispiel/` |  |  | Eine Passage durch alle vier Stationen, als Muster für Outline und Briefing |
| `drafts/` |  |  | Olis unsortierter Notizzettel. **Wird ignoriert**, siehe unten |

## Der Vertrag

Jede Datei in den vier Rollen-Verzeichnissen trägt ihn im Frontmatter: `role`, `readers`, `when`, `mode`, `agent-visible`. `mode: full` heißt ganz lesen, `mode: lookup` heißt durchsuchen und **nie** ganz in den Kontext holen. `agent-visible: no` heißt: kommt in keinen Agenten-Auftrag. Ein `!` vor einem Leser heißt, dass dieser Lader die Datei ausdrücklich nicht sehen darf.

```bash
python3 scripts/kontext-lint.py
```

## Wann was gilt

| Situation | zuerst |
|---|---|
| Abschnitt schreiben oder neu fassen | `rules/arbeitsweise.md`, zwei Stufen: `/editor-outline`, dann `/editor-write` |
| Klang, Publikum, Zielbild | `rules/stimme.md` |
| Kapitelkopf, Überschrift, Vokabular | `rules/form.md` |
| Änderungsrunde fertig | `rules/pruefen.md`, welche Linse, welcher Zuschnitt |
| Behauptung schreiben oder anzweifeln | `knowledge/fakten.md` durchsuchen |
| Befund vor der Übergabe an Oli | `state/decisions.md` als Filter |
| Offener Punkt, jetzt nicht behoben | sofort nach `state/issues*.md`, vor der Chat-Antwort |
| Bild suchen oder einziehen | `rules/bilder.md`, Agent `editor-images` |
| Kompilieren, Longform-Konfiguration | `rules/werkzeuge.md` |

## Was nur hier steht

- **Formuliert wird über den Agenten `writer`, nicht in der Hauptsession**, auch bei einem einzelnen Absatz. Warum: `rules/arbeitsweise.md`.
- **`drafts/` wird nicht gelesen und nicht angefasst.** Unsortierte Notizen, Halbfertiges, Kopiertes. Weder durchsuchen noch beim Recherchieren heranziehen, außer Oli nennt ausdrücklich eine Datei daraus. Was dort brauchbar ist, wandert erst nach `material/`, wenn Oli es sagt.
- **Texte nicht committen.** Oli committet redaktionelle Änderungen selbst. Werkzeuge, Skripte und Konfiguration dagegen schon.
- **`manuscript/Index.md` ist die einzige Wahrheit für Zugehörigkeit und Reihenfolge.** Longform pflegt die Datei, nicht von Hand ändern.
- Der Hook `.claude/hooks/text-lint.py` prüft jede Schreiboperation unter `manuscript/` mechanisch auf lange Gedankenstriche.
