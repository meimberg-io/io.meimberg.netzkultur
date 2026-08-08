---
name: editor-write
description: Zweite Stufe des Schreibens - gibt den Intake eines Abschnitts an den Agenten writer und setzt den zurückkommenden Text ein. Nutzen, wenn der Intake steht und Prosa daraus werden soll. Formuliert nicht selbst.
---

# Formulieren

Du formulierst nicht. Du übergibst den Intake an den Agenten `writer` und setzt ein, was zurückkommt. Auch bei einem einzelnen Absatz. Warum: `rules/arbeitsweise.md`.

## Ablauf

1. Intake laden: `material/intake/<NN>.<MM>.md`. Gibt es keinen, ist Stufe 1 noch nicht gelaufen; dann `editor-outline` statt zu improvisieren.
2. Agent `writer` starten. Sein Auftrag ist der **Intake im Wortlaut**, sonst nichts. Nicht eindampfen, nicht kommentieren, keine Regeln beilegen: Sein Prompt steht in `.claude/agents/writer.md` und wird automatisch geladen.
3. Kommt eine `Fehlt:`-Zeile zurück, ist das ein Rechercheauftrag. Ergebnis ins Dossier, Intake ergänzen, neu laufen lassen. Nicht selbst überschreiben.
4. Text in `manuscript/` einsetzen und dabei `rules/form.md` anwenden: Dateiname, Kapitelkopf, Überschriften.
5. Den neuen Abschnitt in Longform an der richtigen Stelle einsortieren, damit er in `manuscript/Index.md` steht. Eine Szene, die dort fehlt, kommt in keinem Prüfzuschnitt vor.
6. Einmal als Leser lesen.

Soll der Abschnitt einem bestimmten Ton folgen, leg dem Auftrag einen bis zwei Absätze aus `rules/stimme.md` bei, ausgewählt nach dem, was dieser Abschnitt zu tun hat. Nie mehr als zwei, sonst kopiert der `writer` statt zu treffen.

## Übergabe

Der Abschnitt geht direkt an Oli. Keine `copyedit-`Linse von hier aus starten, auch nicht als Angebot.

Trifft der Text nicht, wird nicht am Satz nachgebessert. Der Intake wird geschärft und der `writer` läuft neu. Fast immer fehlte Stoff, oder der Auftragssatz war eine Themenangabe statt eines Ziels.
