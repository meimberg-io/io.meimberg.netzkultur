# Dossier: Entstehung des Usenet (1979–1981)

**Auftrag:** Intro bzw. erster Abschnitt (2–3 Absätze) eines rund vierseitigen Artikels über das Usenet für ein Tech- und Netzkultur-Publikum; nur Entstehungsgrund, Zeitpunkt und Umstände.
**Annahmen:** Zielumfang des Dossiers nach der Stufe „Intro / einzelner Abschnitt" bemessen, nicht nach dem Gesamtartikel. Sprache des Zieltexts: Deutsch. Netzkultur als Schwerpunkt heißt hier: Zugangsregeln, Kostenverteilung und Nutzungsabsicht der Beteiligten, nicht die spätere Newsgroup-Kultur der 1990er.
**Recherchestand:** 2026-08-08 · 5 Quellen (davon 1 Primärdokument, 3 Beteiligten-Berichte) · Beleglage: solide für Motiv, Entwurf und Ankündigung; dünn für das Datum des ersten übertragenen Artikels und für alle Site-Zahlen vor 1982.

## Kern-Narrativ & Roter Faden

Am Anfang stand kein Kommunikationsentwurf, sondern ein Wartungsärgernis: Beim Umstieg auf 7th Edition Unix wollte die Informatik in Duke eine selbstgebaute Ankündigungsfunktion im `login`-Kommando loswerden. Aus dem lokalen Ersatz wurde in derselben Sitzung ein Netz, weil das ARPANET für die Beteiligten nicht erreichbar war: dort kam nur hinein, wer Militär, Rüstungsauftragnehmer oder DoD-Vertragsnehmer war. Gebaut wurde deshalb aus dem, was ohne Genehmigung und ohne Etat vorhanden war (UUCP, Telefonleitung, selbstgebaute Wählmodems), und die Sparzwänge dieser Ausgangslage haben das Netz länger geprägt als jede Absicht seiner Erfinder: Die Nutzung, für die das Usenet heute steht, kommt in der Gründungsankündigung nicht vor.

(**Alternativer Bogen:** Ausschluss als Hauptachse — Studierende ohne Etat bauen sich ein Ersatznetz, weil das offizielle für sie gesperrt ist. Kostet den technischen Zufall am Anfang, der die spätere Formatarmut erst erklärt.)

## Fakten- & Chronologie-Skelett

- **Anfang 1979** — 7th Edition Unix erscheint; der Umstieg von 6th Edition zwingt Duke, jede lokale Änderung zu portieren oder aufzugeben · Duke CS · darunter eine Änderung an `login`, die eine Meldung einmal pro Nutzer anzeigt; bei 15 Zeichen/Sekunde auf Hardcopy-Terminals ist eine längere Meldung bei jedem Login nicht zumutbar `[belegt: Bellovin §3; CircleID-I]`
- **Herbst 1979** — Ellis und Truscott laden zu einer Besprechung ins Duke CS, Bellovin (UNC) kommt dazu · drei Festlegungen: lokale Verwaltungsmeldungen, netzweite Verteilung, Transport über UUCP statt eigenem Protokoll · Duke wird zentraler Wählknoten und pollt die anderen · Truscotts eigenes Bild vom Vorhaben: „a distributed newsletter without a single point of failure", Vorbild ein Rundbrief mit zehn oder zwanzig Beiträgen im Monat, Anlass das Gefühl, „alone and isolated from other computer science departments" zu sein `[belegt: Bellovin §3; CircleID-II; Truscott-Interview]`
- **Jahreswende 1979/80** — Bellovin schreibt den Prototyp in rund 150 Zeilen Bourne Shell; er braucht auf einer unbelasteten PDP-11/70 über eine Minute pro Artikel · erste Knoten `duke` und `unc`, als dritter `phs` (Physiologie, Duke Medical School, betreut von Dennis Rockwell) `[belegt: Bellovin §4; Daniel u. Truscott bei Hauben-2]`
- **1980-01** — Jim Ellis hält auf der Usenix-Tagung in Boulder einen kurzen Vortrag und verteilt 80 Kopien der fünfseitigen „Invitation to a General Access UNIX Network" (Verfasser: Tom Truscott) unter 400 Teilnehmern · am meisten Anklang findet die Beschreibung der zwei selbstgebauten 300-Baud-Wählmodems `[belegt: Bellovin §7 · Kopienzahl einfach belegt: Truscott bei Hauben-2]`
- **1980-01-24** — Der Musterartikel im Anhang der Invitation trägt den Zeitstempel `Thu Jan 24 01:39:20 EST 1980`, den Pfad `duke!unc!smb` und als Inhalt einen Bugfix an `cron.c` · frühestes greifbares Abbild eines Usenet-Artikels, aber ein Formatbeispiel, kein Archivfund `[einfach belegt: Invitation S. 3]`
- **1980, Sommer** — A News, die C-Fassung von Stephen Daniel mit Truscott, geht auf das Conference-Tape der Usenix in Delaware · das begleitende Handout enthält die Formulierung „a poor man's ARPANET, if you will" `[belegt: Hauben-2]`
- **Aufnahmeregeln im Vergleich** — ARPANET: Militär, Rüstungsauftrag oder DoD-Forschungsvertrag; verbreitete Annahme unter den Ausgeschlossenen: politische Verbindungen plus 100.000 $ · Usenet: „Admission to the net is open to all UNIX licensees", Telefonkosten geschätzt 10–20 $/Monat, von Duke weiterberechnet `[belegt: Bellovin §2; Invitation S. 1; Daniel bei Hauben-2]`
- **Dimensionierung** — Bellovins Schätzung des dauerhaften Spitzenverkehrs: 1–2 Artikel pro Tag von höchstens 50–100 Sites, „ever" · daraus die Artikel-ID aus 8 Zeichen Rechnername plus 5 Ziffern, weil 7th Edition Unix Dateinamen auf 14 Zeichen begrenzt `[belegt: Bellovin §4]`

## Wendepunkte & Ursache-Wirkung-Kausalitäten

### W1 — Die Besprechung im Duke CS, Herbst 1979

- **Problem:** Eine lokale Ankündigungsfunktion sollte den Versionswechsel überleben; parallel wollten Ellis und Truscott Meldungen über Institutsgrenzen hinweg sichtbar machen, ohne Zugang zum ARPANET zu haben.
- **Entscheidung & Zielkonflikt:** Eigenes Netzprotokoll (Kontrolle über Routing und Format, aber Monate Arbeit und teure Hardware) gegen UUCP (bereits in 7th Edition enthalten, an fast jedem Forschungsstandort vorhanden, dafür Stapelbetrieb, 300 bit/s, Verzögerung im Tagesbereich). Entschieden wurde für UUCP, ausdrücklich mit der Begründung, ein neues Protokoll wäre eine Neuerfindung ohne Nutzen.
- **Folge:** Kurzfristig konnte das Netz ohne Genehmigung, ohne Etat und ohne Behörde entstehen; Duke übernahm die Telefonrechnung und stellte sie den gepollten Standorten in Rechnung. Langfristig erbte das Usenet die Eigenschaften der Telefonrechnung: Sternstruktur, Abhängigkeit von wenigen zahlungskräftigen Knoten, Verteilung per Fluten statt per Routing.
- **Fehlannahme:** Die zentralen Knoten galten als bloße Kostenstelle. Dass sie steuern, was andere Standorte überhaupt zu sehen bekommen, wurde erst mit der Backbone-Cabal in den 1980ern zum Thema. `[belegt: Bellovin §3, §9]`
- **Belegtiefe:** `[belegt: Bellovin §3, Anhang A; Invitation S. 1, S. 4]`

### W2 — Die Ankündigung in Boulder, Januar 1980

- **Problem:** Ein Netz aus zwei Rechnern im selben Landkreis ist kein Netz; die Beteiligten brauchten Standorte, die mitmachen und ihre eigenen Telefonkosten tragen.
- **Entscheidung & Zielkonflikt:** Offene Aufnahme aller Unix-Lizenznehmer gegen kontrollierten Kreis. Zweiter Konflikt, im Dokument selbst ausgetragen: erst Gremium, dann Netz gegen erst Netz, dann Gremium. Die Invitation beantwortet den Einwand „This is a sloppy proposal. Let's start a committee." mit „No thanks!" und der Begründung, erst die Nutzung zeige die echten Probleme.
- **Folge:** Beitreten konnte jeder mit Unix-Lizenz und Telefonanschluss, ohne Antrag an eine Behörde. Zugleich war das Format auf die geschätzte Größenordnung gebaut: keine Hierarchie in den Newsgroup-Namen, kein Lesen außerhalb der Reihenfolge, kein Threading, keine Löschsteuerung. Auf Missbrauch antwortete das Dokument mit „Not us!" und der Bitte um Vorschläge.
- **Fehlannahme:** Die Verkehrsschätzung lag um Größenordnungen daneben. Sichtbar wurde das ab etwa 1981/82, als A News die Last nicht mehr trug und Mary Ann Horton mit Matt Glickman B News schrieb; Bellovin nennt das Nichteinplanen von Erfolg im Rückblick den größten Fehler.
- **Belegtiefe:** `[belegt: Invitation S. 1, S. 4; Bellovin §4, §8; CircleID-IX]`

## Einbezogene Nutzervorgaben

- „nur, warum es entstanden ist, wann und so weiter" → Recherche auf 1979–1981 begrenzt; Great Renaming, alt.*-Hierarchie, Spam-Geschichte und das Ende der Provider-Feeds bleiben draußen.
- „Netzkultur ist hier der Schwerpunkt" → Auswahl auf Zugangsregeln, Kostenverteilung, Selbstverständnis der Beteiligten und die Differenz zwischen Absicht und späterer Nutzung gelenkt; Protokolldetails nur, wo sie eine kulturelle Folge haben.
- Quellenhinweis Bellovin 2025 geprüft → Volltext samt Anhang B (Originalankündigung) beschafft und als Primärgrundlage verwendet; Anhang B ist die Reproduktion des AUUGN-Abdrucks April/Mai 1980.
- „zwei, drei Absätze" → Chronologie bewusst auf acht Punkte gekürzt; ein Wendepunkt trägt den Abschnitt, der zweite liefert die Schlusspointe.

## Zu vermeidende KI-Mythen & Klischees

- **„Poor man's ARPANET" stand in der Gründungsankündigung** → In der Invitation vom Januar 1980 kommt die Formulierung nicht vor; belegt ist sie erst im Handout zum A-News-Tape der Sommer-Usenix 1980, dort als Einschub mit „if you will"; Stephen Daniel gibt an, nicht zu wissen, wann sie geprägt wurde `[umstritten: Invitation vs. Hauben-2]`
- **Usenet als bewusstes Gegenprojekt zum Militärnetz** → Anlass war eine Login-Meldung beim Unix-Versionswechsel; der Ausschluss vom ARPANET erklärt die Bauweise, nicht den Anstoß `[belegt: Bellovin §3; Daniel bei Hauben-2]`
- **Die Erfinder wollten ein Diskussionsnetz** → Die Ankündigung nennt Bugfixes, Fehlermeldungen, Hilferufe, „have/want"-Anzeigen und Gebrauchtwagen; soziale Nutzung fehlt vollständig, Bellovin bezeichnet die Auslassung im Rückblick als kurzsichtig `[belegt: Invitation S. 1; Bellovin §7]`
- **Ein Erfinderpaar** → Truscott und Ellis hatten die Idee, den ersten lauffähigen Code schrieb Bellovin, die verteilte C-Fassung Stephen Daniel mit Truscott, UUCP auf knappe Maschinen portierte Dennis Rockwell `[belegt: Bellovin §4; Daniel u. Truscott bei Hauben-2]`
- **Kein Big-Bang:** Es gibt kein belegtes Datum eines ersten übertragenen Artikels. Die Gründung verteilt sich auf Entwurf (Herbst 1979), Shell-Prototyp (Jahreswende), öffentliche Ankündigung (Januar 1980) und die erste verteilbare Fassung (Sommer 1980).
- **Gesperrt:** Geburtsstunde des Social Web · Wiege des Internets · Vorläufer von Reddit/Twitter · Wilder Westen des Netzes · Graswurzelrevolution · Pioniere · Siegeszug · „veränderte alles" · „das erste soziale Netzwerk" ohne das Wörtchen „wohl", das Bellovin selbst setzt.
- **Zahlen mit Vorsicht:** „50 Standorte im ersten Jahr" (verbreitet, ohne Primärquelle) gegen Spaffords Tabelle von 1988 (1980: 15 Standorte, 1981: 150) gegen die überlieferten Netzkarten (April 1981 rund 23 Knoten, Juni 1981 rund 30) — die Frühzahlen zählen erkennbar Verschiedenes `[umstritten: Hauben-2 vs. Karten]`; „1–2 Artikel pro Tag" ist Bellovins Schätzung von 1979, kein gemessener Verkehr `[belegt: Bellovin §4]`; „10–20 $/Monat" ist eine Werbeangabe aus der Ankündigung, keine Abrechnung `[einfach belegt: Invitation S. 1]`; „80 Kopien, 400 Teilnehmer" beruht allein auf Truscotts Erinnerung `[einfach belegt: Truscott bei Hauben-2]`

## Quellen

- **Bellovin** = Steven M. Bellovin, „Netnews: The Origin Story", IEEE Annals of the History of Computing 47(1), 2025, S. 7–21, https://www.cs.columbia.edu/~smb/papers/netnews-hist.pdf (Erlebnisbericht des Erstimplementierers; Selbstdarstellung eines Beteiligten, aber mit Primärdokument im Anhang und ausdrücklicher Benennung eigener Fehler)
- **Invitation** = Tom Truscott, „Invitation to a General Access UNIX Network", Handout Usenix Boulder Januar 1980, Nachdruck in AUUGN Vol. IV No. II, April–Mai 1980, S. 15–18; Reproduktion als Anhang B in Bellovin (Primärdokument)
- **CircleID-I / -II / -IX** = Steven M. Bellovin, „The Early History of Usenet", Teil I, II und IX, circleid.com, November 2019 bis Januar 2020 (frühere Fassung derselben Darstellung, nicht unabhängig von Bellovin)
- **Hauben-2** = Ronda Hauben, „The Evolution of Usenet: the Poor Man's ARPANET", Kapitel 2 in: M. u. R. Hauben, Netizens, 1997, https://www.columbia.edu/~hauben/book-pdf/CHAPTER%202.pdf (enthält wörtliche Beiträge von Stephen Daniel, Tom Truscott und Gregory G. Woodbury sowie Spaffords IETF-Wachstumstabelle von 1988)
- **Truscott-Interview** = „Usenet Interview with Tom Truscott", giganews.com/usenet-history/truscott/ (Beteiligtenaussage auf der Seite eines Usenet-Anbieters; für Motive und Selbstbild brauchbar, für Zahlen nicht)

**Lücken:** Kein Datum und kein Text des tatsächlich ersten zwischen `duke` und `unc` übertragenen Artikels; die überlieferten Archive (UTZOO) setzen erst im Februar 1981 ein — schließen ließe sich das nur durch Bänder oder Ausdrucke aus den Duke-/UNC-Beständen. Jim Ellis hat keine eigene ausführliche Darstellung hinterlassen und ist 2001 gestorben; sein Anteil ist ausschließlich über Truscott und Bellovin überliefert. Die Site-Zahlen für 1980 und 1981 stammen sämtlich aus Rückblicken, nicht aus zeitgenössischen Zählungen. Das AUUGN-Original von 1980 wurde nur als Reproduktion in Bellovin gesichtet, nicht im Archivscan gegengelesen.
