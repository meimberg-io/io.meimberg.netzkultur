---
role: rule
readers: claude
when: nach einer Änderungsrunde
mode: full
agent-visible: no
---

# Prüfen

Eine Linse pro Lauf, jede über den Agenten `copyedit`. Zwei Prüfungen in einem Lauf verdrängen einander: Fakten schlagen Sprache, Sprache schlägt Verständlichkeit.

| Linse | Prüft | Kosten |
|---|---|---|
| `copyedit-clarity` | Erster Eindruck, Doppeldeutigkeit, falsche Assoziation | billig |
| `copyedit-language` | Betonung, Wortwahl, Bilder, Grammatik, Register, Rhythmus | billig |
| `copyedit-humanize` | Maschinelle Muster: Satzlängen, Antithesen, Dreiklänge, Floskeln | billig |
| `copyedit-coherence` | Aufbau, Anschlüsse, Bezüge, Widersprüche über Distanz | mittel |
| `copyedit-plausibility` | Anachronismen, Größenordnungen; liefert „Zu belegen" | mittel |
| `copyedit-facts` | Recherche gegen die Belegliste | teuer |

| Geändert | Linsen | Umfang |
|---|---|---|
| Satz | clarity, language | Abschnitt |
| Absatz umgebaut oder verschoben | zusätzlich coherence | Abschnitt |
| Kapitel fertig | coherence, plausibility, humanize | `--kapitel N` |
| Werk fertig | coherence, dann facts | `--naht N`, `--abriss` |

Am Ende einer Änderungsrunde, nicht nach jedem Komma. Oli ruft die Linsen selbst auf; Claude liest den Abschnitt vorher einmal als Leser.

## Reparieren statt flicken

**Ein Prüflauf liefert Befunde, keine Aufgabenliste.** Vor der ersten Änderung steht ein Urteil über den ganzen Abschnitt.

- **Bis etwa fünf Befunde:** einzeln beheben, nach jedem Eingriff den Absatz ganz lesen.
- **Mehr, oder mehrere zum Aufbau:** nicht flicken. Der Abschnitt geht zurück auf Stufe 1. Zwanzig einzeln reparierte Sätze ergeben einen Text, der an zwanzig Stellen stimmt und im Ganzen tot ist: Jede Reparatur wird defensiv formuliert, und die Übergänge zwischen den geflickten Stellen trägt niemand mehr.

Der Befundberg ist die Diagnose, nicht die Aufgabe. Die Ursache ist fast immer eine von vieren:

- zu wenig Material, der Text füllt
- der Auftragssatz war ein Thema statt eines Ziels
- die Klangprobe passte nicht zu dem, was der Abschnitt tun sollte
- der Abschnitt will zu viel auf einmal

Welche es war, gehört ins Briefing der Neufassung. Ohne das kommt dieselbe Fassung zurück.

**Eine Form ist kein Befund, solange der Satz etwas sagt.** Ein Befund entsteht, wo die Form eine leere Stelle verdeckt.

Nie den alten Befund an einen Agenten mitgeben. Nach dem Einarbeiten ein zweiter Lauf, weil Reparaturen neue Schäden erzeugen. Jeden Befund gegen `state/decisions.md` abgleichen, über die **Stelle** im Text, nicht über die Formulierung; nur Offenes an Oli. Abgelehnter Befund sofort nach `state/decisions.md`, bestätigter Sachverhalt nach `knowledge/fakten.md`.

Was diese Reihe inhaltlich falsch machen kann, steht in [erzaehlhaltung.md](erzaehlhaltung.md) und wird von Claude selbst geprüft.

## Was die Agenten sehen

Maßgeblich ist `agent-visible` im Vertrag. Sichtbar sind `knowledge/fakten.md` für `plausibility` und `facts`, dazu `material/` für `facts`. Alles andere nicht, `state/decisions.md` nie.
