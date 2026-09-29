# Netzkultur — Eine Retrospektive

> Eine Kulturgeschichte des Netzes von Mailboxen und Modems bis TikTok, Brainrot und KI.
> Produktionsumgebung des Werks: Text, Material, Bilder, Prüfapparat.

**Sprache:** Deutsch in allen Inhalten und in der Kommunikation. Code und Identifier englisch.

## Karte

| Verzeichnis | Rolle | Ladeverhalten | Inhalt |
|---|---|---|---|
| `rules/` | `rule` | gezielt, je nach Aufgabe | `stimme.md` Klang · `form.md` Format · `pruefen.md` Prüfung und Prüfradius · `erzaehlhaltung.md` inhaltliche Fallen · `ablegen.md` was wohin gehört · `bilder.md` · `werkzeuge.md` |
| `knowledge/` | `knowledge` | Abfrage | `fakten.md`, von Oli bestätigt, schlägt Modellwissen |
| `material/` | `material` | Abfrage | `dossier-<NN>.md` je Kapitel · `quellen.md` Bewertung · `quellen/` Snapshots · `kandidaten.md` |
| `state/` | `state` | Abfrage | `decisions.md` abgelehnte Befunde · `issues.md`, `issues-<NN>.md` · `publikation.md` |
| `manuscript/` |  |  | Das Buch. `Index.md` plus eine Datei je Szene, `kompilat.md` ist das zusammengesetzte Ganze |
| `assets/` · `scripts/` |  |  | Bilder mit Metadaten · `kompilieren.py`, `kontext-lint.py`, `bild-einziehen.py` |
| `drafts/` |  |  | Olis unsortierter Notizzettel. **Wird ignoriert**, siehe unten |

## Der Vertrag

Jede Datei in den vier Rollen-Verzeichnissen trägt ihn im Frontmatter: `role`, `readers`, `when`, `mode`, `agent-visible`. `mode: full` heißt ganz lesen, `mode: lookup` heißt durchsuchen und **nie** ganz in den Kontext holen. `agent-visible: no` heißt: kommt in keinen Agenten-Auftrag. Ein `!` vor einem Leser heißt, dass dieser Lader die Datei ausdrücklich nicht sehen darf.

```bash
python3 scripts/kontext-lint.py
```

## Wann was gilt

| Situation | zuerst |
|---|---|
| Abschnitt schreiben oder neu fassen | zwei Stufen: `/editor-plot`, dann `/editor-write` |
| Klang, Publikum, Zielbild | `rules/stimme.md` |
| Kapitelkopf, Überschrift, Vokabular | `rules/form.md` |
| Änderungsrunde fertig | `rules/pruefen.md`, welche Linse, welcher Zuschnitt |
| Abschnitt fertig, vor der Übergabe | `rules/erzaehlhaltung.md` selbst durchgehen |
| Behauptung schreiben oder anzweifeln | `knowledge/fakten.md` durchsuchen |
| Befund vor der Übergabe an Oli | `state/decisions.md` als Filter |
| Offener Punkt, jetzt nicht behoben | `rules/ablegen.md`: kapitelbezogen nach `state/issues-<NN>.md`, sonst nach `state/issues.md` |
| Bild suchen oder einziehen | `rules/bilder.md`, Agent `editor-images` |
| Kompilieren, Longform-Konfiguration | `rules/werkzeuge.md` |

## Was nur hier steht

- **Beide Schreibstufen laufen über den Agenten `editor`, nicht in der Hauptsession**, auch bei einem einzelnen Absatz. Sein Verfahren steht in `.claude/agents/editor.md`.
- **`drafts/` wird nicht gelesen und nicht angefasst.** Unsortierte Notizen, Halbfertiges, Kopiertes. Weder durchsuchen noch beim Recherchieren heranziehen, außer Oli nennt ausdrücklich eine Datei daraus. Was dort brauchbar ist, wandert erst nach `material/`, wenn Oli es sagt.
- **Texte nicht committen.** Oli committet redaktionelle Änderungen selbst. Werkzeuge, Skripte und Konfiguration dagegen schon.
- **`manuscript/Index.md` ist die einzige Wahrheit für Zugehörigkeit und Reihenfolge.** Longform pflegt die Datei, nicht von Hand ändern.
- Der Hook `.claude/hooks/text-lint.py` prüft jede Schreiboperation unter `manuscript/` mechanisch auf lange Gedankenstriche.
