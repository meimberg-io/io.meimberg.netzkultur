---
rolle: regel
liest: editor-outline, editor-write
wann: vor dem ersten Satz
modus: ganz
agentensichtbar: nein
---

# Wie hier gearbeitet wird

Verbindlich für jeden Text der Reihe. Was der Text sein soll, steht in [haltung.md](haltung.md);
wie geprüft wird, in [pruefen.md](pruefen.md). Diese Datei sagt, wie man dorthin kommt.

## Arbeitsweise

**Erst Material, dann Prosa.** Vor dem ersten Satz steht das Dossier des Kapitels in
`research/<NN>.md`. Steht dort zum Thema nichts, wird recherchiert, und das Ergebnis kommt dorthin,
bevor formuliert wird. Aus vier Datenpunkten wird durch Umstellen kein guter Absatz, nur ein besser
sortierter. Wenn eine Stelle dünn wirkt, fehlt Stoff und nicht Formulierung: ein Name, ein Ort, eine
Zahl, ein Vorgang. Wo das Material nicht mehr hergibt, wird die Stelle gekürzt oder weggelassen,
niemals mit Satzbau aufgefüllt.

**Nicht über den Beleg hinaus schreiben.** Was recherchiert ist, kommt in den Text. Was aus dem
Modellgedächtnis nachgefüllt wird, damit ein Absatz anschaulich wirkt, wird zum Fehler. Belegt am
2026-08-05: Recherchiert waren Tomlinson, FTP und die Drei-Viertel-Zahl, ausgeschmückt waren der
klimatisierte Saal, der Bildschirm am Terminal und „die erste E-Mail" — und genau diese drei Stellen
waren die Befunde. Wenn ein Bild fehlt, dafür recherchieren oder den Satz weglassen.

**Kontext ist nicht Ausschmückung.** Die Regel darüber verbietet Details, die es nicht gibt. Sie
verbietet nicht, dem Leser zu sagen, was man weiß. Wer sie darauf ausdehnt, schreibt Namen ohne
Zuordnung („bei der Firma BBN") und Passivsätze ohne Handelnden („Mitte der Siebziger wurde
nachgezählt"). Der Text sagt dann nichts Falsches und erzählt nichts. Dass BBN das ARPANET im Auftrag
der ARPA baute und Tomlinson deshalb dort saß, ist recherchierter Kontext und gehört hinein. Wenn
eine Prüfung eine Stelle beanstandet, ist Erklären die erste Antwort und Kürzen die letzte.

Kontext kostet die Genauigkeit nicht, er stellt sie her: „Die erste E-Mail von einer Maschine zu
einer anderen" ist nur dann eine falsche Erstheitsbehauptung, wenn vorher niemand gesagt hat, dass
Nutzer sich innerhalb eines Rechners längst Nachrichten hinterlassen konnten.

**Vor dem ersten Satz lesen, was der Leser schon weiß.** Nicht nur den Abschnitt, sondern die
Nachbarabschnitte, aus denen er kommt. Ein Wort, das dort besetzt ist, ist hier verbrannt: „Die Post
war nicht vorgesehen" als Überschrift, acht Zeilen nach einem H3 „Das Monopol der Bundespost", ist
mit Kontext nicht zu retten.

**Nie lokal am Satz redigieren.** Vor der Änderung den Abschnitt lesen, bei Strukturfragen das
Kapitel und die Einleitung. Danach prüfen, was die Änderung woanders zerrissen hat. Der Prüfradius
richtet sich nach der Größe der Änderung.

**Aus Kritik wird kein Patch.** Beanstandete Sätze sind Symptome, nicht die Aufgabe. Der Abschnitt
wird neu gedacht, notfalls über den Agenten `editor-free` mit Ein-Satz-Auftrag. Sonst entsteht
Vermeidungsprosa und eine zweite Runde auf demselben Niveau.

**Diskussion ist nicht Text.** Was Oli im Gespräch sagt, ist Begründung. In den Text gehört kein
Satz, der eine Behauptung verneint, die nur in einer Vorfassung stand. Prüfen: Stünde dieser Satz
auch da, wenn wir nie darüber geredet hätten?

**Die Verbotslisten gehören nicht hierher.** `humanize`, die Symptomlisten der Linsen und jede
Aufzählung von zu vermeidenden Formen werden **nach** dem Schreiben angewendet, nicht währenddessen.
Belegt am 2026-07-31: Ein Prompt mit Sachstand und sieben Verboten lieferte drei unbrauchbare
Fassungen, ein Ein-Satz-Auftrag drei brauchbare. Ein Satz, der etwas sagt, verträgt jede Form; ein
Satz, der nichts sagt, wird durch keine Regel gut.

## Im Text

**Kapitelkopf.** Titel, dann ein Satz über die Ära, dann der Zeitraum. In dieser Reihenfolge, damit
der Leser zuerst die Stimmung und dann die Einordnung bekommt.

```
# <Titel der Ära>

_<ein Satz, der die Ära beschreibt>_

_Etwa <von> bis <bis>_
```

Die Querschnittskapitel tragen im unteren Slot „_Ein Querschnitt durch alle Jahrzehnte_" statt einer
Jahresangabe. Durchgezogen in 01 bis 07 und in der Kapitelliste des Vorworts.

**Keine harten Zeitgrenzen.** Die Zeiträume überlappen, weil die Ären real überlappen. Das gilt auch
**innerhalb** eines Kapitels: Ein Beispiel, das ein paar Jahre über den Kopf-Zeitraum hinausreicht,
ist kein Befund. Im Zweifel wird der Zeitraum im Kopf gedehnt, nicht das Beispiel gestrichen.

**Der Ausblick in die Gegenwart gehört zur Ära-Beschreibung.** Wenn eine Erscheinung dieser Jahre bis
heute weiterläuft, darf das am Ende ihres Abschnitts stehen, auch als ganzer Absatz.

**Kein Reden über Kapitel.** Kein „Am Ende des vorherigen Kapitels", kein „davon erzählt das nächste
Kapitel". Das liest sich wie ein „Was bisher geschah" und ergibt keinen Sinn, wenn jemand das Werk in
einem Zug liest. Stattdessen wird der Gegenstand am Anfang des Folgekapitels inhaltlich neu
aufgegriffen.

**Überschrift ist Etikett, der Text steht allein.** Jeder Abschnitt benennt sein Thema selbst und
liest sich als vollständige Prosa, auch wenn man die Überschrift wegdenkt. Der erste Satz darf die
Überschrift nicht bloß weiterformulieren („Fanpages" → „Ein großer Teil dieser Seiten waren
Schreine") und nicht mit vagem Rückbezug einsteigen, der eine Dramaturgie voraussetzt, die im Text
nicht steht („dieser Seiten", „das", „dafür", „daneben"). Test: den Text ohne Überschriften lesen,
jeder Absatz muss für sich Sinn ergeben.

**Die Überschrift ist der Name, unter dem man die Sache wiedererkennt** (Leetspeak, Webringe,
GeoCities, das Gästebuch), keine umschreibende Zeile. „Anfänger hießen jetzt n00bs" erkennt niemand,
„Leetspeak" schon.

**Der Kunstbetrieb kommt nicht vor.** Die Reihe erzählt Subkultur und Subversives, Netzkultur, die
von unten entsteht. Die Netzkunst des Kunstbetriebs (Telekommunikationskunst, The Thing, net.art,
documenta) gehört nicht dazu, auch nicht als Kontrast. Wo ein Abschnitt Kunst behandelt, ist die
Kunst der Szene gemeint.

**Das Vokabular der Szene, nicht das der Industrie.** Wo aus der Szene erzählt wird, heißt es Kopien,
Cracks und Warez. „Raubkopie" und „Softwarepiraterie" sind die Wörter der Rechteinhaber und stehen
nur da, wo deren Sicht wiedergegeben wird.

**Keine Gliederungsebene „Teil 1", „Teil 2"** und keine durchnummerierten Abschnitte. Überschriften
tragen Inhalt, keine Zählung.

**Überschriften brauchen kein einheitliches Tempus.** Präsens, Präteritum und Nominalphrasen dürfen
nebeneinander stehen. Gleichförmige Überschriften wirken generisch.
