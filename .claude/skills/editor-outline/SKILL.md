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
- `rules/arbeitsweise.md`.

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
 Ausdrücklich mit dabei:
   - Kontraste: was war vorher, was war anderswo, was hatte man erwartet
   - Konflikte: wer wollte was, woran hat es sich gerieben
   - offene Fragen und Widersprüche zwischen den Quellen
   - das Unfertige: „vielleicht gehört das eher nach vorn", „unklar, ob das stimmt"
 Belege in Klammern hinter der Aussage. Formulierung ist egal, Vollständigkeit nicht.
 Redundanz ist erlaubt und meist ein gutes Zeichen.>

## Worauf es ankommt
<zwei bis vier Zeilen: was der Leser mitnehmen soll, wenn er den Rest vergisst.
 Und was nur Beiwerk ist und im Zweifel gekürzt wird.>

## Weggelassen
<was zum Thema existiert und draußen bleibt, je mit einem Halbsatz warum>

## Umfang
<Wortzahl des späteren Textes. Der Sachstand darf und soll länger sein.>
```

Der Abschnitt **Sachstand** ist die eigentliche Arbeit. Ist er dünn, wird der Text dünn, und keine Formulierung rettet das. Ein Sachstand, der nur aus belegten Einzelfakten besteht, ist noch nicht fertig: Dann fehlt die Frage, warum diese Fakten nebeneinander stehen.

Ungeprüftes steht im Sachstand mit Markierung, geht aber nicht in die zweite Stufe und kommt nach `state/issues-<NN>.md`.

## Übergabe

Der Sachstand geht an Oli, bevor formuliert wird. Er ist die Stelle, an der er inhaltlich eingreift, und der Grund, warum er das Thema nicht selbst recherchieren muss. Danach `editor-write`.

Ein durchgearbeitetes Beispiel liegt in `beispiel/2-outline.md`.
