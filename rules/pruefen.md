---
rolle: regel
liest: claude
wann: nach einer Änderungsrunde, vor einem Prüflauf
modus: ganz
agentensichtbar: nein
---

# Wie geprüft wird

Fünf Linsen, jede in einem eigenen Lauf. Der Grund für die Trennung ist belegt: Sobald zwei Prüfungen
in einem Lauf sitzen, gewinnt die am leichtesten begründbare. Fakten verdrängen Sprache,
Sprachfehler verdrängen Verständlichkeit.

Jede Linse ist ein Skill in `.claude/skills/` und läuft über den Agenten `copyedit`, damit sie kein
Projektwissen hat.

| Linse | Prüft | Kosten |
|---|---|---|
| `copyedit-clarity` | Erster Eindruck, Doppeldeutigkeit, falsche Assoziation | billig |
| `copyedit-language` | Betonung, Wortwahl, Bilder, Grammatik, Register, Rhythmus | billig |
| `copyedit-coherence` | Aufbau, Anschlüsse, Bezüge, Widersprüche über Distanz | mittel, braucht den ganzen Text |
| `copyedit-plausibility` | Anachronismen, Größenordnungen, Zuordnung. Liefert die Liste „Zu belegen" | mittel |
| `copyedit-facts` | Recherche gegen die Belegliste | teuer, Minuten |

## Zuschnitt

Den Umfang bestimmt Claude, nicht Oli. Maßstab ist die Größe der Änderung:

- **Satz geändert** → `copyedit-clarity` und `copyedit-language` auf den betroffenen Abschnitt.
- **Absatz umgebaut oder verschoben** → zusätzlich `copyedit-coherence` mit Abschnitts-Umfang.
  Verschieben zerreißt Anschlüsse, das ist der häufigste Folgeschaden.
- **Kapitel fertig** → `copyedit-coherence` und `copyedit-plausibility` über das ganze Kapitel.
- **Werk fertig** → `copyedit-coherence` im Werk-Umfang plus `copyedit-facts` gegen die Belegliste.

Nicht nach jedem Komma, sondern am Ende einer Änderungsrunde.

**Einzelne exponierte Stellen lohnen einen Mini-Lauf.** Eine neue Überschrift, ein Einstiegssatz,
eine Bildunterschrift durch `copyedit-clarity` schicken, zusammen mit dem Abschnitt, den sie
ankündigt. Dort entscheidet der erste Eindruck alles. Wer sich die Überschrift gerade selbst
ausgedacht hat, ist ihr schlechtester Prüfer.

**Oli ruft die Linsen selbst auf.** Ein neu geschriebener Abschnitt geht direkt an ihn, ohne
vorgeschalteten Prüflauf und ohne die Frage, ob einer laufen soll. *(2026-08-06 entschieden.)* Was
das nicht ersetzt: Vor der Übergabe liest Claude den Abschnitt einmal als Leser durch. Das ist Urteil
und keine Prüfroutine.

## Hier laufen die Verbotslisten, nicht beim Schreiben

`humanize` und jede andere Symptomliste (lange Gedankenstriche, Floskeln, Antithese-Pointen,
Dreiklänge, Frage-Überschriften, gleichförmige Satzlängen) gehört an den **fertigen** Text. Beim
Schreiben angewendet erzeugt sie Vermeidungsprosa: Ein Agent, der sieben Dinge vermeiden muss,
schreibt um Formulierungen herum statt zur Sache hin. Belegt am 2026-07-31 und erneut am 2026-08-07.

Geprüft wird dabei der Inhalt, nicht das Muster. Eine Form ist kein Befund, solange der Satz etwas
sagt: „Nicht nur X, sondern vor allem Y" ist ein Gefälle zwischen zwei Aussagen und in Ordnung,
solange beide etwas behaupten. Ein Befund entsteht erst, wo die Form eine leere Stelle verdeckt.

## Zwei Regeln, die nicht verhandelbar sind

**Nie den alten Befund mitgeben.** Der einzige Wert dieser Agenten ist der unbelastete Blick. Ein
mitgeliefertes Protokoll macht daraus eine Abhakliste. Ob eine gemeldete Stelle behoben ist, prüft
Claude selbst.

Das gilt **auch für Agenten, die schreiben sollen**, und dort strenger. Dafür gibt es den Agenten
`editor-free`: Er schreibt eine Passage neu, ohne von bestehenden Kontexten gebremst zu werden. Der
Auftrag besteht aus der Passage und einem Satz, was daraus werden soll. Keine Sachstandsliste, keine
Registerdefinition, keine Verbotsliste. Ein normaler Agent im Repo hilft dabei nicht, weil er sich
die Regeln selbst anliest, wenn man sie ihm nicht gibt, und dann genauso ausweichend schreibt.

**Zweiter Lauf nach dem Einarbeiten.** Nicht wegen der alten Befunde, sondern weil Reparaturen neue
Schäden erzeugen. Das ist der Normalfall, nicht die Ausnahme.

## Was die Agenten sehen dürfen

| Datei | Sichtbar für |
|---|---|
| `memory/fakten.md` | `copyedit-facts`, `copyedit-plausibility` — sie schlagen dort nach, bevor sie eine Behauptung anzweifeln |
| `research/<NN>.md` | `copyedit-facts` — die Belegbasis, gegen die geprüft wird |
| alles andere | **nein** |

`notes/decisions.md` sehen die Agenten **nie**. Claude gleicht jeden Befund vor der Übergabe an Oli
dagegen ab und legt nur vor, was offen ist. Abgeglichen wird über die **Stelle** im Text, nicht über
die Formulierung des Befunds: Derselbe Fall kommt beim nächsten Lauf oft anders benannt. Lehnt Oli
einen Befund ab, kommt er sofort dorthin. Ohne das meldet jeder Lauf dieselben zwanzig Fälle, und die
neuen gehen darin unter.

Meldet ein Agent etwas als falsch und Oli bestätigt, dass es stimmt, kommt der Sachverhalt mit Datum
nach `memory/fakten.md`. Ohne das meldet jeder neue Lauf denselben vermeintlichen Fehler.

Wiederholt sich eine Ablehnung über mehrere Werke hinweg, ist sie keine Einzelentscheidung mehr,
sondern eine Stilregel und gehört nach [schreiben.md](schreiben.md).
