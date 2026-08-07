---
role: rule
readers: claude
when: nach einer Änderungsrunde
mode: full
agent-visible: no
---

# Prüfen

Hier laufen die Symptomlisten, nicht beim Schreiben. Eine Linse pro Lauf, jede über den Agenten `copyedit`. Zwei Prüfungen in einem Lauf verdrängen einander: Fakten schlagen Sprache, Sprache schlägt Verständlichkeit.

| Linse | Prüft | Kosten |
|---|---|---|
| `copyedit-clarity` | Erster Eindruck, Doppeldeutigkeit, falsche Assoziation | billig |
| `copyedit-language` | Betonung, Wortwahl, Bilder, Grammatik, Register, Rhythmus | billig |
| `copyedit-coherence` | Aufbau, Anschlüsse, Bezüge, Widersprüche über Distanz | mittel |
| `copyedit-plausibility` | Anachronismen, Größenordnungen, Zuordnung; liefert „Zu belegen" | mittel |
| `copyedit-facts` | Recherche gegen die Belegliste | teuer |

## Zuschnitt

Umfang nach Größe der Änderung, am Ende einer Änderungsrunde statt nach jedem Komma. Zuschnitte baut `scripts/kompilieren.py`.

| Geändert | Linsen | Umfang |
|---|---|---|
| Satz | clarity, language | Abschnitt |
| Absatz umgebaut oder verschoben | zusätzlich coherence | Abschnitt |
| Kapitel fertig | coherence, plausibility | `--kapitel N` |
| Werk fertig | coherence, dann facts | `--naht N`, `--abriss` |

Neue Überschrift, Einstiegssatz oder Bildunterschrift: Mini-Lauf mit `clarity`, zusammen mit dem Abschnitt, den sie ankündigt.

Oli ruft die Linsen selbst auf. Ein neuer Abschnitt geht direkt an ihn. Claude liest ihn vorher einmal als Leser.

## Was in dieser Reihe zusätzlich geprüft wird

Die Linsen sind blind und kennen die Erzählhaltung nicht. Diese Prüfung macht Claude selbst, am fertigen Abschnitt:

- **Leitfragen-Rahmen im Einstieg.** Der Abschnitt fängt mit einer Sache an, nicht mit einer Frage, die er dann beantwortet.
- **Analytische Abschnitts-Schlüsse.** „Auch das war eine soziale Lösung …", „das gab es schon vor den Plattformen", „genau darin liegt der Kern". Ein Schluss darf schlicht zum nächsten Element überleiten.
- **Analytische Glossen** mitten im Text: „bekam damit denselben Rang wie …".
- **Behaupteter Vibe.** „Die waren cool", „avantgardistisch", „revolutionär". Zeigen statt behaupten.
- **Featureliste statt Strang.** Gästebuch, Besucherzähler und animierte GIFs gehören in ihren Strang, nicht je in einen eigenen Abschnitt. Und die große Klammer erkennen: nicht „Winamp", sondern „die Musik wandert ins Netz".
- **Genanntes ohne Anschauung.** Wird eine Seite erwähnt (Suck.com), muss dastehen, was daran war, sonst weglassen.
- **Das schön Sinnlose klein eingeführt.** „Zwischen all dem standen auch ein paar Seiten …" für etwas, das kulturell im Zentrum steht.

## Befunde

- Nie den alten Befund mitgeben. Ob eine gemeldete Stelle behoben ist, prüft Claude selbst.
- Nach dem Einarbeiten zweiter Lauf. Reparaturen erzeugen neue Schäden.
- Eine Form ist kein Befund, solange der Satz etwas sagt. Ein Befund entsteht, wo die Form eine leere Stelle verdeckt.
- Jeden Befund gegen `state/decisions.md` abgleichen, über die **Stelle** im Text, nicht über die Formulierung. Nur Offenes an Oli.
- Abgelehnter Befund sofort nach `state/decisions.md`, bestätigter Sachverhalt nach `knowledge/fakten.md`.

## Was die Agenten sehen

Maßgeblich ist `agent-visible` im Vertrag. Sichtbar sind `knowledge/fakten.md` für `plausibility` und `facts`, dazu `material/` für `facts`. Alles andere nicht, `state/decisions.md` nie.
