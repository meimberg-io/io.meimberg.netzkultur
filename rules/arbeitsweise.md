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

Nie in der Hauptsession, auch nicht bei einem einzelnen Absatz. Er bekommt Auftrag, Intake, Klangprobe und das Vorwissen des Lesers. Projektregeln bekommt er nicht.

**Belegt am 2026-08-08**, vier Läufe über denselben Intake: Sein Briefing ist Olis Blog-Prompt, angepasst aufs Sachbuch (dritte Person, keine Überschriften, kein Fazit, Länge aus dem Auftrag). Sprachlich das beste Ergebnis, das das Projekt bisher hatte. Die verbliebenen Schwächen lagen sämtlich im Intake, keine in der zweiten Stufe. Der Hebel für die Qualität ist deshalb der Intake.

Damit ist die zweite Stufe ein **Umschreiben**, und darauf beruht, dass eine lange Symptomliste im Briefing hier nützt statt zu schaden: Der Inhalt steht schon, es gibt nichts, worum man herumschreiben könnte. Beim Erzeugen aus dem Nichts wäre dieselbe Liste schädlich.

Was am fertigen Text stört und aus einem einzelnen Fall stammt, wird **nicht** ins Briefing nachgetragen. Ein Regelwerk, das jeden Einzelfall aufnimmt, ist in einem halben Jahr wieder die Verbotsliste, gegen die es gebaut wurde. Soll eine Einzelheit tragen, etwa ein wörtliches Zitat, wird sie im Intake betont.

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
