# Netzkultur — Eine Retrospektive

Eine Kulturgeschichte des Netzes, von Mailboxen und Modems bis TikTok, Brainrot und KI. Dieses Repo ist die Werkstatt dazu: der Text selbst, das recherchierte Material, die Bilder und der Prüfapparat.

Geschrieben wird mit Claude Code. Was die Agenten dabei dürfen und woran sie sich halten, steht in `CLAUDE.md` und in `rules/`. Diese Datei hier ist für den Menschen.

## Wie eine Passage entsteht

Immer in zwei Schritten, und zwischen beiden schaust du drauf.

```
/editor-outline 01.03      # was gesagt werden soll: Fakten, Reihenfolge, Auftrag
                           # → du liest die Outline und korrigierst sie
/editor-write 01.03        # wie es gesagt wird: fertige Prosa
                           # → du liest den Text
```

Der zweite Schritt formuliert nicht selbst, sondern beauftragt einen Agenten, der das Projekt nicht kennt und nur ein Briefing bekommt: Auftrag, Material, eine Klangprobe, das Vorwissen des Lesers. Das ist Absicht. Ein Schreiber, dem man vorher zwanzig Regeln zeigt, schreibt um die Regeln herum statt zur Sache hin.

Wenn ein Text nicht trifft, liegt es fast immer an einer von zwei Stellen: Das Material war zu dünn, oder der Auftragssatz war eine Themenangabe statt eines Ziels. Beides repariert man in der Outline, nicht am Satz.

## Wie geprüft wird

Fünf Linsen, jede ein eigener Aufruf, jede blind für das Projekt:

```
/copyedit-clarity          # versteht man den Satz beim ersten Lesen
/copyedit-language         # Satzbau, Betonung, Bilder, Rhythmus
/copyedit-coherence        # Aufbau, Anschlüsse, Widersprüche über Distanz
/copyedit-plausibility     # Anachronismen, Größenordnungen, was belegt werden muss
/copyedit-facts            # Recherche gegen die Belegliste
```

Zwei Prüfungen in einem Lauf verdrängen einander, deshalb einzeln. Welche wann sinnvoll ist, steht in `rules/pruefen.md`; die Prüftexte für Kapitel, Nähte und den Struktur-Abriss baut `scripts/kompilieren.py`.

## Was wo liegt

| Ordner | Was drin ist |
|---|---|
| `manuscript/` | **Das Buch.** Eine Datei je Abschnitt, flach abgelegt. `Index.md` bestimmt Zugehörigkeit und Reihenfolge und wird von Longform gepflegt, nicht von Hand. `kompilat.md` ist das zusammengesetzte Ganze zum Gegenlesen. |
| `material/` | **Der Stoff.** Pro Kapitel ein Dossier mit Fakten, Zahlen und Anekdoten, an jedem Eintrag die Quelle. `quellen/` enthält die Snapshots der Originale, `quellen.md` sagt, welche davon als Beleg taugt und welche nur Zeitzeuge ist. `kandidaten.md` sammelt Stoff, der noch keinen Platz hat. |
| `knowledge/` | **Was gesichert ist.** `fakten.md` enthält Sachverhalte, die du bestätigt hast und die gegen anderslautendes Modellwissen gelten. Ein Eintrag hier verhindert, dass dieselbe Stelle in jedem Prüflauf wieder als Fehler gemeldet wird. |
| `state/` | **Wo wir stehen.** Offene Punkte pro Kapitel und werkweit, getrennt nach „du entscheidest" und „Claude erledigt". Dazu `decisions.md`: Befunde, die du abgelehnt hast, damit sie nicht wiederkommen. |
| `rules/` | **Die Vorgaben.** Klang, Format, Arbeitsweise, Prüfverfahren, Bildrechte, Longform-Mechanik. Kurz gehalten, weil sie vollständig gelesen werden. |
| `assets/` | Bilder. Urheber, Lizenz und Bildunterschrift stehen in der Datei selbst, gepflegt über Lightroom. |
| `beispiel/` | Eine Passage von Dossier über Outline und Briefing bis zum fertigen Text. Zum Nachschauen, wie fein das Material sein muss. |
| `drafts/` | **Dein Notizzettel.** Unsortiertes, Halbfertiges, Kopiertes. Agenten fassen das nicht an und lesen es nicht, außer du nennst ausdrücklich eine Datei daraus. |
| `scripts/`, `longform-scripts/`, `lightroom/` | Werkzeuge und Katalog. |

## Wohin mit …

- **einem Fund beim Recherchieren** → ins Dossier des Kapitels, `material/dossier-<NN>.md`, mit Quelle am Eintrag. Ohne Quelle markiert als `(ungeprüft)`.
- **einer Entscheidung über einen strittigen Fakt** → `knowledge/fakten.md`, mit Datum und mit der Angabe, was das Modell stattdessen annimmt.
- **einem Befund, den du nicht willst** → `state/decisions.md`. Sonst meldet ihn jeder Prüflauf erneut.
- **einer offenen Frage** → `state/issues-<NN>.md`.
- **einem Einfall ohne Platz** → `material/kandidaten.md`.
- **allem, was du nur schnell irgendwo ablegen willst** → `drafts/`.

Claude legt diese Dinge im Normalfall selbst ab, bevor sie im Chat auftauchen. Was nur in einer Nachricht steht, ist verloren.

## Handgriffe

```bash
python3 scripts/kompilieren.py --kapitel 3    # ein Kapitel als Prüftext
python3 scripts/kompilieren.py --naht 1       # Übergang von Kapitel 1 zu 2
python3 scripts/kompilieren.py --abriss       # Struktur über das ganze Buch
python3 scripts/kontext-lint.py               # hält die Ablage in Ordnung
```

Die Struktur dieses Repos stammt aus dem Template in `io.meimberg.writer`; dort steht auch, warum es so gebaut ist.
