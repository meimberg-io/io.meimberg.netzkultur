# Redaktions-Workflow: wann welcher Prüf-Agent läuft

Fünf Agenten in `.claude/agents/`, jeder mit genau einer Linse. Der Grund für die Trennung ist
belegt: Sobald zwei Prüfungen in einem Lauf sitzen, gewinnt die am leichtesten begründbare.
Fakten verdrängen Sprache, Sprachfehler verdrängen Verständlichkeit.

| Agent | Linse | Kosten |
|---|---|---|
| `klarheit` | Erster Eindruck, Doppeldeutigkeit, falsche Assoziation | billig |
| `sprache` | Betonung, Wortwahl, Bilder, Grammatik, Register, Rhythmus | billig |
| `kohaerenz` | Aufbau, Anschlüsse, Bezüge, Widersprüche über Distanz, Leserführung | mittel, braucht den ganzen Text |
| `plausibilitaet` | Anachronismen, Größenordnungen, Zuordnung, Reichweite. Liefert die Liste „Zu belegen" | mittel |
| `faktencheck` | Recherche gegen die Belegliste | teuer, Minuten |

## Zuschnitt

Den Umfang bestimmt Claude, nicht Oli. Maßstab ist die Größe der Änderung:

- **Satz geändert** → `klarheit` und `sprache` auf den betroffenen Abschnitt.
- **Absatz umgebaut oder verschoben** → zusätzlich `kohaerenz` mit Abschnitts-Umfang. Verschieben
  zerreißt Anschlüsse, das ist der häufigste Folgeschaden.
- **Kapitel fertig** → `kohaerenz` und `plausibilitaet` über das ganze Kapitel.
- **Werk fertig** → `kohaerenz` im Werk-Umfang plus `faktencheck` gegen die Belegliste.

Nicht nach jedem Komma, sondern am Ende einer Änderungsrunde.

**Einzelne exponierte Stellen lohnen einen Mini-Lauf.** Eine neue Überschrift, ein Einstiegssatz,
eine Bildunterschrift durch `klarheit` schicken, zusammen mit dem Abschnitt, den sie ankündigt.
Dort entscheidet der erste Eindruck alles, und der Lauf dauert unter einer Minute, wenn der Text
direkt im Auftrag steht statt in einer Datei. Wer sich die Überschrift gerade selbst ausgedacht
hat, ist ihr schlechtester Prüfer.

## Zwei Regeln, die nicht verhandelbar sind

**Nie den alten Befund mitgeben.** Der einzige Wert dieser Agenten ist der unbelastete Blick. Ein
mitgeliefertes Protokoll macht daraus eine Abhakliste. Ob eine gemeldete Stelle behoben ist,
prüft Claude selbst.

Das gilt **auch für Agenten, die schreiben sollen**, und dort noch strenger. Dafür gibt es den Agenten
**`frei formulieren`**: Er schreibt eine Passage neu, ohne von bestehenden Kontexten und Regeln
gebremst zu werden. Der Auftrag an ihn besteht aus der Passage und einem Satz, was daraus werden
soll. Keine Sachstandsliste, keine Registerdefinition, vor allem **keine Verbotsliste**.

Ein Agent, der sieben Dinge vermeiden muss, schreibt um Formulierungen herum statt zur Sache hin;
heraus kommen Umschreibungen wie „den Kopierschutz aus dem Original geholt", weil „entfernt" verboten
schien. Belegt am 2026-07-31: Ein durchdesignter Prompt mit Sachstand und sieben Verboten lieferte
drei unbrauchbare Fassungen, ein Ein-Satz-Auftrag drei brauchbare. Ein normaler Agent im Repo hilft
dabei nicht, weil er sich `decisions.md` und die Ton-Regeln selbst anliest, wenn man sie ihm nicht
gibt, und dann genauso ausweichend schreibt. Deshalb `frei formulieren` nehmen.

**Zweiter Lauf nach dem Einarbeiten.** Nicht wegen der alten Befunde, sondern weil Reparaturen
neue Schäden erzeugen. Das ist der Normalfall, nicht die Ausnahme.

## Drei Dateien neben dem Text

Jedes größere Werk hat drei Ablagen, die streng getrennt bleiben:

| Datei | Inhalt |
|---|---|
| **`decisions.md`** | Nur **Beschlüsse**: gesetzte Konventionen, abgelehnte Befunde, aufgelöste Konflikte, Ton-Regeln. Keine Aufgaben. |
| **`<NN>_issues.md`** | Die **To-do-Liste pro Kapitel**, getrennt in „zu entscheiden (Oli)" und „zu erledigen (Claude)". |
| **`issues.md`** | Dasselbe für alles, was mehr als ein Kapitel betrifft. |

**Claude pflegt die Issue-Listen selbst und sofort.** Jeder Befund, der nicht auf der Stelle behoben
wird, kommt dorthin, **bevor** er im Chat auftaucht, und ohne dass Oli darum bittet. Ein Punkt, der
nur in einer Nachricht steht, ist verloren; Oli müsste sonst jedes Mal fragen, was eigentlich noch
offen ist. Behobene Punkte werden gestrichen.

`decisions.md` enthält damit: Befunde, die Oli abgelehnt hat, plus die Konventionen, die sich aus
seinen Korrekturen ergeben haben.

**Die Agenten sehen diese Datei nicht**, sonst wird aus dem frischen Blick eine Abhakliste.
Claude gleicht jeden Befund vor der Übergabe an Oli dagegen ab und legt nur vor, was offen ist.
Abgeglichen wird über die Stelle im Text, nicht über die Formulierung des Befunds: Derselbe Fall
kommt beim nächsten Lauf oft anders benannt.

Lehnt Oli einen Befund ab, kommt er sofort dorthin. Ohne das meldet jeder Lauf dieselben zwanzig
Fälle, und die neuen gehen darin unter.

Wiederholt sich eine Ablehnung über mehrere Werke hinweg, ist sie keine Einzelentscheidung mehr,
sondern eine Stilregel und gehört in die Format-Spec.

## Faktenbasis

Bestätigte Sachverhalte, die dem Modellwissen widersprechen, stehen in
[fakten.md](fakten.md). `plausibilitaet` und `faktencheck` schlagen dort nach, bevor sie eine
Behauptung anzweifeln. Meldet ein Agent etwas als falsch und Oli bestätigt, dass es stimmt, kommt
der Sachverhalt dorthin, mit Datum. Ohne das meldet jeder neue Lauf denselben vermeintlichen
Fehler.
