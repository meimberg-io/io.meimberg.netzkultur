# Redaktions-Workflow: wann welche Linse läuft

Fünf Linsen, jede in einem eigenen Lauf. Der Grund für die Trennung ist belegt: Sobald zwei
Prüfungen in einem Lauf sitzen, gewinnt die am leichtesten begründbare. Fakten verdrängen Sprache,
Sprachfehler verdrängen Verständlichkeit.

Jede Linse ist ein Skill in `.claude/skills/` und läuft über den Agenten `copyedit`, damit sie kein
Projektwissen hat.

| Linse | Prüft | Kosten |
|---|---|---|
| `copyedit-clarity` | Erster Eindruck, Doppeldeutigkeit, falsche Assoziation | billig |
| `copyedit-language` | Betonung, Wortwahl, Bilder, Grammatik, Register, Rhythmus | billig |
| `copyedit-coherence` | Aufbau, Anschlüsse, Bezüge, Widersprüche über Distanz, Leserführung | mittel, braucht den ganzen Text |
| `copyedit-plausibility` | Anachronismen, Größenordnungen, Zuordnung, Reichweite. Liefert die Liste „Zu belegen" | mittel |
| `copyedit-facts` | Recherche gegen die Belegliste | teuer, Minuten |

## Schreiben in zwei Schritten

Erst der Inhalt, dann der Ton: Skill `editor-outline`, dann Skill `editor-write`. Dort steht das
Verfahren. Der Grund für die Trennung: Wer Inhalt und Klang gleichzeitig verhandelt, ändert bei jedem
Einwand beides und landet in Flickwerk.

## Zuschnitt

Den Umfang bestimmt Claude, nicht Oli. Maßstab ist die Größe der Änderung:

- **Satz geändert** → `copyedit-clarity` und `copyedit-language` auf den betroffenen Abschnitt.
- **Absatz umgebaut oder verschoben** → zusätzlich `copyedit-coherence` mit Abschnitts-Umfang. Verschieben
  zerreißt Anschlüsse, das ist der häufigste Folgeschaden.
- **Kapitel fertig** → `copyedit-coherence` und `copyedit-plausibility` über das ganze Kapitel.
- **Werk fertig** → `copyedit-coherence` im Werk-Umfang plus `copyedit-facts` gegen die Belegliste.

Nicht nach jedem Komma, sondern am Ende einer Änderungsrunde.

**Oli ruft die Linsen selbst auf.** Ein neu geschriebener Abschnitt geht direkt an ihn, ohne
vorgeschalteten Prüflauf und ohne die Frage, ob einer laufen soll. Er liest den Text zuerst selbst und
startet danach die `/copyedit-`Commands, wenn er sie haben will. *(2026-08-06 entschieden.)*

Was das nicht ersetzt: Vor der Übergabe liest Claude den Abschnitt einmal als Leser durch. Das ist
Urteil und keine Prüfroutine, und es lässt sich nicht an eine Linse delegieren.

**Nicht über den Beleg hinaus schreiben.** Was recherchiert ist, kommt in den Text; was aus dem
Modellgedächtnis nachgefüllt wird, um einen Absatz anschaulich zu machen, wird zum Fehler. Belegt am
2026-08-05: Recherchiert waren Tomlinson, FTP und die Drei-Viertel-Zahl, ausgeschmückt waren der
klimatisierte Saal, der Bildschirm am Terminal und „die erste E-Mail" — und genau diese drei Stellen
waren die Befunde (Sichtgeräte gab es 1971 kaum, Tomlinsons Leistung ist die Mail *zwischen*
Rechnern, der Saal ist ungedeckt). Wenn ein Bild fehlt, entweder dafür recherchieren oder den Satz
weglassen.

**Kontext ist nicht Ausschmückung.** Die Regel darüber verbietet Details, die es nicht gibt. Sie
verbietet nicht, dem Leser zu sagen, was man weiß. Wer sie darauf ausdehnt, schreibt Namen ohne
Zuordnung („bei der Firma BBN") und Passivsätze ohne Handelnden („Mitte der Siebziger wurde
nachgezählt"), und der Text sagt dann nichts Falsches und erzählt nichts. Richtig ist die
Unterscheidung: Der klimatisierte Saal war Dekoration ohne Beleg und gehört heraus; dass BBN das
ARPANET im Auftrag der ARPA baute und Tomlinson deshalb dort saß, ist recherchierter Kontext und
gehört hinein. Wenn eine Prüfung eine Stelle beanstandet, ist Erklären die erste Antwort und Kürzen
die letzte.

Nebeneffekt, an dem sich das prüfen lässt: **Kontext kostet die Genauigkeit nicht, er stellt sie
her.** „Die erste E-Mail von einer Maschine zu einer anderen" ist nur dann eine falsche
Erstheitsbehauptung, wenn vorher niemand gesagt hat, dass Nutzer sich innerhalb eines Rechners längst
Nachrichten hinterlassen konnten. Steht der Satz davor, ist die Aussage präzise **und** lesbar. Die
kleinere Formulierung war beides nicht. *(2026-08-05, an Olis Gegenentwurf zum H3 in 01.02: Lesefluss,
keine falschen Sätze, und der Leser wird mit angenehmem Kontext versehen.)*

**Vor dem ersten Satz lesen, was der Leser schon weiß.** Nicht nur den Abschnitt, sondern die
Nachbarabschnitte, aus denen er kommt. Ein Wort, das dort besetzt ist, ist hier verbrannt: „Die Post
war nicht vorgesehen" als Überschrift, acht Zeilen nach einem H3 „Das Monopol der Bundespost", ist
nicht mit Kontext zu retten. *(2026-08-05)*

**Aus Kritik wird kein Patch.** Wenn Oli Stellen beanstandet, sind die genannten Sätze die Symptome,
nicht die Aufgabe. Der Abschnitt wird neu gedacht, notfalls über `editor-free`. Sonst entsteht
Vermeidungsprosa, und es kommt eine zweite Runde auf demselben Niveau zurück. Siehe
[ton.md](ton.md), „Bei Kritik nicht Satz für Satz nachbessern".

**Einzelne exponierte Stellen lohnen einen Mini-Lauf.** Eine neue Überschrift, ein Einstiegssatz,
eine Bildunterschrift durch `copyedit-clarity` schicken, zusammen mit dem Abschnitt, den sie ankündigt.
Dort entscheidet der erste Eindruck alles, und der Lauf dauert unter einer Minute, wenn der Text
direkt im Auftrag steht statt in einer Datei. Wer sich die Überschrift gerade selbst ausgedacht
hat, ist ihr schlechtester Prüfer.

## Zwei Regeln, die nicht verhandelbar sind

**Nie den alten Befund mitgeben.** Der einzige Wert dieser Agenten ist der unbelastete Blick. Ein
mitgeliefertes Protokoll macht daraus eine Abhakliste. Ob eine gemeldete Stelle behoben ist,
prüft Claude selbst.

Das gilt **auch für Agenten, die schreiben sollen**, und dort noch strenger. Dafür gibt es den Agenten
**`editor-free`**: Er schreibt eine Passage neu, ohne von bestehenden Kontexten und Regeln
gebremst zu werden. Der Auftrag an ihn besteht aus der Passage und einem Satz, was daraus werden
soll. Keine Sachstandsliste, keine Registerdefinition, vor allem **keine Verbotsliste**.

Ein Agent, der sieben Dinge vermeiden muss, schreibt um Formulierungen herum statt zur Sache hin;
heraus kommen Umschreibungen wie „den Kopierschutz aus dem Original geholt", weil „entfernt" verboten
schien. Belegt am 2026-07-31: Ein durchdesignter Prompt mit Sachstand und sieben Verboten lieferte
drei unbrauchbare Fassungen, ein Ein-Satz-Auftrag drei brauchbare. Ein normaler Agent im Repo hilft
dabei nicht, weil er sich `decisions.md` und die Ton-Regeln selbst anliest, wenn man sie ihm nicht
gibt, und dann genauso ausweichend schreibt. Deshalb `editor-free` nehmen.

**Zweiter Lauf nach dem Einarbeiten.** Nicht wegen der alten Befunde, sondern weil Reparaturen
neue Schäden erzeugen. Das ist der Normalfall, nicht die Ausnahme.

## Vier Dateien neben dem Text

Jedes größere Werk hat vier Ablagen, die streng getrennt bleiben:

| Datei | Inhalt |
|---|---|
| **`konventionen.md`** | Die Regeln der Reihe. Wird **beim Schreiben** gelesen. |
| **`decisions.md`** | Nur die **abgelehnten Befunde**. Wird **nur nach einem Prüflauf** gelesen, als Filter. |
| **`<NN>_issues.md`** | Die **To-do-Liste pro Kapitel**, getrennt in „zu entscheiden (Oli)" und „zu erledigen (Claude)". |
| **`issues.md`** | Dasselbe für alles, was mehr als ein Kapitel betrifft. |

**Claude pflegt die Issue-Listen selbst und sofort.** Jeder Befund, der nicht auf der Stelle behoben
wird, kommt dorthin, **bevor** er im Chat auftaucht, und ohne dass Oli darum bittet. Ein Punkt, der
nur in einer Nachricht steht, ist verloren; Oli müsste sonst jedes Mal fragen, was eigentlich noch
offen ist. Behobene Punkte werden gestrichen.

`decisions.md` enthält damit ausschließlich Befunde, die Oli abgelehnt hat. Die Konventionen, die sich aus
seinen Korrekturen ergeben haben, stehen in `notes/konventionen.md`.

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
[fakten.md](fakten.md). `copyedit-plausibility` und `copyedit-facts` schlagen dort nach, bevor sie eine
Behauptung anzweifeln. Meldet ein Agent etwas als falsch und Oli bestätigt, dass es stimmt, kommt
der Sachverhalt dorthin, mit Datum. Ohne das meldet jeder neue Lauf denselben vermeintlichen
Fehler.
