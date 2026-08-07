---
role: rule
readers: editor-outline, editor-write, claude
when: bevor an einem Abschnitt gearbeitet wird
mode: full
agent-visible: no
---

# Arbeitsweise

Klang: [stimme.md](stimme.md). Format: [form.md](form.md). Prüfung: [pruefen.md](pruefen.md).

## Zwei Stufen

1. `editor-outline`: was gesagt wird. Stichpunkte, Fakten, Reihenfolge. Geht an Oli, bevor Prosa entsteht.
2. `editor-write`: wie es gesagt wird. Prosa in einem Zug.

Nie beides in einem Schritt. Ändern sich bei einem Einwand Inhalt und Formulierung gleichzeitig, zurück auf Stufe 1.

Bei Kritik zuerst klären, ob Inhalt oder Formulierung gemeint ist. Inhaltliche Kritik nicht am Satz reparieren. Wie mit einem Befundberg umzugehen ist, steht in [pruefen.md](pruefen.md) unter Reparieren statt flicken.

## Formuliert wird über den Agenten `writer`

Nie in der Hauptsession, auch nicht bei einem einzelnen Absatz. Er bekommt Auftrag, Material, Klangprobe, Vorwissen des Lesers.

Keine Regelwerke, keine Konventionen, keine Verbotslisten ins Briefing. Belegt am 2026-07-31: Ein Prompt mit Intake und sieben Verboten lieferte drei unbrauchbare Fassungen, ein Ein-Satz-Auftrag drei brauchbare. Symptomlisten laufen nach dem Schreiben, siehe [pruefen.md](pruefen.md).

Das gilt für das Schreiben aus Material. Beim **Umschreiben** eines fertigen Textes ist es anders: Dort steht der Inhalt schon, es gibt nichts, worum man herumschreiben könnte, und eine mechanische Liste (Gedankenstrich, Dreiklang, Floskel) ist dann ein brauchbares Werkzeug. Der Unterschied ist nicht die Liste, sondern ob der Text noch entsteht.

## Material vor Prosa

- Vor der Outline steht das Dossier `material/dossier-<NN>.md`. Fehlt Stoff, recherchieren und dort eintragen, nicht später. Aus vier Datenpunkten wird durch Umstellen kein guter Absatz, nur ein besser sortierter.
- Nur Belegtes in den Text. Belegt am 2026-08-05: Ausgeschmückt waren der klimatisierte Saal, der Bildschirm am Terminal und die Erstheitsbehauptung. Genau diese drei Stellen waren später die Befunde.
- Wirkt eine Stelle dünn, fehlt Material, nicht Formulierung.
- Wer eine Person, Firma oder Behörde nennt, sagt, wofür sie steht. Recherchierter Kontext ist keine Ausschmückung, er stellt die Genauigkeit erst her: „Die erste E-Mail von einer Maschine zu einer anderen" ist nur dann eine falsche Erstheitsbehauptung, wenn vorher niemand gesagt hat, dass Nutzer sich innerhalb eines Rechners längst Nachrichten hinterlassen konnten.

## Prüfradius

Nie lokal am Satz redigieren. Vor der Änderung den Abschnitt lesen, bei Strukturfragen das Kapitel und die Einleitung. Danach prüfen, was die Änderung woanders zerrissen hat.

Vor dem ersten Satz lesen, was der Leser schon weiß, also auch die Nachbarabschnitte. Ein Wort, das dort besetzt ist, ist hier verbrannt: „Die Post war nicht vorgesehen" als Überschrift, acht Zeilen nach einem H3 „Das Monopol der Bundespost", ist nicht zu retten.

Was Oli im Gespräch sagt, ist Begründung, kein Textbaustein.

## Sofort ablegen, nicht im Chat lassen

Vor der Antwort im Chat, ohne Aufforderung:

| Was | Wohin |
|---|---|
| Bestätigter Sachverhalt gegen das Modellwissen | `knowledge/fakten.md`, mit Datum |
| Befund, den Oli abgelehnt hat | `state/decisions.md`, mit Datum |
| Offener Punkt, jetzt nicht behoben | `state/issues.md` oder `issues-<NN>.md` |
| Stoff, der noch keinen Platz hat | `material/kandidaten.md` |

Behobene Punkte streichen, nicht abhaken. Keine dieser Dateien ist ein Logbuch.
