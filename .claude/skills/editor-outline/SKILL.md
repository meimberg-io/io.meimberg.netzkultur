---
name: editor-outline
description: Erste Stufe des Schreibens - erarbeitet den vollständigen Sachstand eines Abschnitts, also alles, was gesagt werden soll, sortiert und mit Zusammenhängen, Kontrasten und offenen Fragen. Nutzen, bevor Prosa entsteht. Liefert keinen fertigen Text, aber auch keine Stichpunktliste.
---

# Sachstand

Hier wird entschieden, **was** gesagt wird. Und zwar vollständig: Was hier nicht steht, kommt später nicht in den Text.

**Das ist keine Gliederung und keine Faktenliste.** Aus einer Liste von Fakten kann die zweite Stufe nur zwei Dinge machen, Fakten aneinanderreihen oder sich Bedeutung dazu ausdenken. Beides ist falsch. Was du lieferst, ist der ausgedachte Gedankengang in Rohform: schlampig formuliert, aber fertig gedacht.

Das Vorbild ist eine gesprochene Notiz, die jemand macht, der das Thema kennt und alles loswerden will, was er dazu zu sagen hat, bevor er es schön schreibt. Redundant, teilweise unentschieden, deutlich länger als der spätere Text. Vollständig.

## Vorher lesen

- `material/dossier-<NN>.md`: der Stoff. Zu wenig darin heißt: jetzt recherchieren und das Ergebnis mit Quelle eintragen, bevor der Sachstand entsteht.
- `knowledge/fakten.md` nach dem Thema durchsuchen. Gilt gegen Modellwissen.
- `material/quellen.md`: welche Quelle als Beleg taugt und welche nicht.
- Die Nachbarabschnitte in `manuscript/`: worauf der Abschnitt hinausläuft, welche Begriffe dort schon eine Bedeutung haben.
- `rules/arbeitsweise.md` und `rules/erzaehlhaltung.md`. Das zweite entscheidet, was aus dem Dossier überhaupt in Frage kommt.

## Ergebnis

```
## Auftrag
<ein Satz: was der Abschnitt beim Leser hinterlassen soll. Das Ziel, nicht das Thema.>

## Vorwissen
<was der Leser davor gelesen hat, welche Begriffe eingeführt sind, welche Wörter
 nebenan besetzt sind>

## Sachstand
<Fließtext, lang, vollständig, in der Reihenfolge, in der es erzählt werden soll.
 Nicht die Fakten allein, sondern was sie bedeuten und wie sie zusammenhängen.
 Ausdrücklich mit dabei: Kontraste (was war vorher, was war anderswo), Konflikte
 (wer wollte was, woran hat es sich gerieben), offene Fragen.

 GESCHRIEBEN FÜR DEN LESER, NICHT FÜR DEN REDAKTEUR. Alles, was hier steht, kann so
 in den Text. Was du beim Recherchieren gedacht hast, steht weiter unten.

 Zwei Regeln, die den Unterschied ausmachen:
   - Nichts verneinen, was nicht vorher behauptet wurde. „Es lag nicht am Geld"
     setzt voraus, dass jemand Geld ins Spiel gebracht hat. Hat niemand. Steht die
     Fehlannahme nur in der Fachliteratur, ist sie eine Notiz und kein Satz.
   - Jeder Name bekommt bei der ersten Nennung seine Rolle. „Bellovin sagt" ist
     wertlos, solange nicht dasteht, wer das ist und warum er es wissen muss.
 Belege in Klammern. Formulierung ist egal, Vollständigkeit nicht.>

## Worauf es ankommt
<zwei bis vier Zeilen: was der Leser mitnehmen soll, wenn er den Rest vergisst.
 Und was nur Beiwerk ist und im Zweifel gekürzt wird.>

## Weggelassen
<was zum Thema existiert und draußen bleibt, je mit einem Halbsatz warum>

## Redaktionelle Notizen
<Alles, was Oli wissen soll und der Leser nicht: verbreitete Fehlannahmen, gegen die
 du beim Recherchieren angeschrieben hast, Zweifel an einer Quelle, Vorschläge zur
 Anordnung, Hinweise an den Schreiber. Dieser Abschnitt geht NICHT ins Briefing.
 Er ist der Grund, warum der Sachstand sauber bleibt.>

## Umfang
<Wortzahl des späteren Textes. Der Sachstand darf und soll länger sein.>
```

**Das Dossier ist ein Steinbruch, keine Abarbeitungsliste.** Es enthält absichtlich mehr, als in den Text kann. Wer alles mitnimmt, was belegt ist, schreibt eine Abhandlung. Faustregel: Der Sachstand ist etwa doppelt so lang wie der Zieltext, nicht fünfmal. Passt mehr hinein, war die Auswahl zu schwach.

Herkunft der Software gehört fast nie hinein: wer welche Fassung schrieb, welche Sprache, welches Upgrade, welche Konferenz. Ein Halbsatz reicht, meist gar nichts.

Der Abschnitt **Sachstand** ist die eigentliche Arbeit. Ist er dünn, wird der Text dünn, und keine Formulierung rettet das. Ein Sachstand, der nur aus belegten Einzelfakten besteht, ist noch nicht fertig: Dann fehlt die Frage, warum diese Fakten nebeneinander stehen.

**Gegenprobe vor der Übergabe:** Lies den Sachstand als jemand, der nur das Vorwissen hat. Jede Stelle, an der du stutzt, weil ein Name, ein Begriff oder ein Gegensatz vorausgesetzt wird, den es im Text nicht gibt, ist ein Fehler im Sachstand und nicht einer, den der Schreiber reparieren kann.

Ungeprüftes steht im Sachstand mit Markierung, geht aber nicht in die zweite Stufe und kommt nach `state/issues-<NN>.md`.

## Übergabe

Der Sachstand geht an Oli, bevor formuliert wird. Er ist die Stelle, an der er inhaltlich eingreift, und der Grund, warum er das Thema nicht selbst recherchieren muss. Danach `editor-write`.

Ein durchgearbeitetes Beispiel liegt in `beispiel/2-outline.md`.
