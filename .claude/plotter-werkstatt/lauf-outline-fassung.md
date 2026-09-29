# Outline: Das arme Netz — wie das Usenet entstand

**Zieltext:** Einleitung / 1. Abschnitt eines ca. vierseitigen Artikels über das Usenet. Umfang: 3 Absätze (≈ 350–420 Wörter). Schwerpunkt Netzkultur, Publikum technik-/netzkultur-affin. Deckt ausschließlich Entstehung ab (Warum, Wann, Wer, Woraus) und übergibt an den Rest des Artikels.

**Kernthese:** Das Usenet entstand nicht aus einer Vision vom globalen Diskursraum, sondern aus Mangel — ein Ersatz für ein kaputtgegangenes Login-Anschlagbrett, gebaut von Leuten, die vom ARPANET aus Geld- und Politikgründen ausgeschlossen waren. Genau diese Armut erzwang die Bauweise (dezentral, ohne Aufnahmegremium, empfängerkontrolliert), aus der später die Netzkultur wurde.

**Spannung:** Die Erfinder haben ihr eigenes Werk um Größenordnungen unterschätzt — 1–2 Artikel pro Tag, maximal 50–100 Sites „ever" — und ausgerechnet das Soziale, das das Netz später ausmachte, kam in der Gründungsschrift mit keinem Wort vor.

---

## Szenarium- & Material-Dossier (Inhaltliche Basis für Stufe 2)

### Akteure, Haltungen & O-Töne

* **[Bellovin 2024]:** Steven M. Bellovin, damals Doktorand UNC Chapel Hill, erster Implementierer. Selbstkritik zur Traffic-Prognose: „I estimated that the peak eventual traffic would be 1–2 articles per day, from 50–100 sites maximum, ever." Nachsatz: „this was grossly wrong even in the short term."
* **[Bellovin 2024 / Blindstelle]:** Zum Fehlen jeder sozialen Nutzung in der Gründungsschrift: „We simply did not anticipate the many things that people would want to talk about with random strangers." Er nennt es „short-sighted", man habe schließlich Amateurfunk gekannt.
* **[Bellovin 2024 / Fazit]:** „Our biggest failure, though, was that we never planned for success."
* **[Daniel via Hauben 1993]:** Stephen Daniel, Duke-Doktorand, schrieb die erste C-Version (A News). Zur Formel „poor man's ARPANET": „but we knew we were excluded. Even if we had been allowed to join, there was no way of coming up with the money."
* **[Daniel via Hauben 1993 / Kosten]:** „It was commonly accepted at the time that to join the ARPANET took political connections and $100,000."
* **[Daniel via Hauben 1993 / Enttäuschung]:** „we were initially disappointed at how few people joined us. We attributed this lack more to the cost of autodialers than lack of desire."
* **[Daniel via Hauben 1993 / arme Verwandte]:** Zum ersten ARPANET-Gateway: „It definitely felt second class to be in read-only mode on human-nets and sf-lovers."
* **[Daniel via Hauben 1993 / Architekturphilosophie]:** „Usenet was organized around netnews, where the receiver controls what is received. The ARPANET lists were organized around mailing lists, where there is a central control for each list."
* **[Truscott via Giganews]:** Tom Truscott, Duke-Doktorand, Sommer 1979 Praktikum bei Ken Thompson in den Bell Labs. Motiv: „We felt alone and isolated from other computer science departments."
* **[Truscott via Giganews / Modell]:** „Usenet was largely modeled as a distributed newsletter without a single point of failure." Und zur Volumenschätzung: „A typical newsletter had ten or twenty items per month, and we naively modeled that too."
* **[Truscott via Hauben 1993 / Boulder]:** Bericht über Ellis' Auftritt: 5-seitige Einladung, „We made up 80 copies and they were gobbled up (not surprising, there were a record-smashing 400 attendees)". Am meisten Applaus bekam die Beschreibung von „Duke's two home-built 300 baud autodialers".
* **[Ellis]:** Jim Ellis, Duke-Doktorand, verstorben 2001, hielt den Vortrag in Boulder und prägte den Namen „Usenet" als Anspielung auf die Nutzergruppe Usenix.
* **[Horton]:** Mary Ann Horton, damals Doktorandin in Berkeley, baute das Gateway von den ARPANET-Listen SF-LOVERS und HUMAN-NETS ins Usenet — die erste echte Inhaltsquelle. Später mit Matt Glickman (Schüler) Autorin von B News.

### Evidenz, Zahlen & Chronologie

* **[Datierung]:** Entwurf „dates to the fall of 1979" (Bellovin). Erste Knoten: `duke` (Duke CS), `unc` (UNC Chapel Hill CS), `phs` (Physiology Dept., Duke Medical School).
* **[Boulder Januar 1980]:** Öffentliche Ankündigung auf der Usenix-Tagung in Boulder, Colorado; Ellis verteilt „Invitation to a General Access UNIX Network"; 80 Exemplare, 400 Teilnehmende. Bellovin selbst ist nicht anwesend.
* **[Delaware Sommer 1980]:** A News geht auf dem Konferenz-Tape der Usenix-Tagung in Delaware in die allgemeine Verteilung. Im dortigen Handout steht der berühmte Satz.
* **[Wachstum Spafford 1988]:** 1979: 3 Sites / ~2 Artikel pro Tag · 1980: 15 / ~10 · 1981: 150 / ~20 · 1982: 400 / ~50 · 1983: 600 / ~120 · 1984: 900 / ~225 · 1986: 2.500 / ~500 · 1988: 11.000 / ~1.800.
* **[Netzkarte 1981]:** Bellovins Karte vom 5. April 1981 (erstellt von Mary Ann Horton) zeigt rund 20 Knoten — 15 Monate nach der Ankündigung.
* **[Telefonkosten]:** Ferngespräche außerhalb der lokalen Zone kosteten nach Entfernung und Tageszeit. Nachttarif ca. 0,50 US-Dollar für drei Minuten.
* **[Übertragungsrate]:** 300 bps Modem, effektiv ca. 1.000 Byte pro Minute. Der UUCP-Quellcode (~120 KB) hätte zwei Stunden gedauert und ca. 20 US-Dollar gekostet — inflationsbereinigt über 60 US-Dollar.
* **[ARPANET-Größe]:** 1977 mehr als 50 Sites von Hawaii bis Norwegen; ca. 280 angeschlossene Rechner 1981.

### Technischer & ökonomischer Kontext (Weltwissen für Stufe 2)

* **[Zugangsregel ARPANET]:** Bellovin wörtlich: „to be on the ARPANET, you needed to be part of the military, be a defense contractor, or have a Department of Defense research contract." Weder Duke noch UNC erfüllten das.
* **[Hardware]:** Duke CS: PDP-11/70. UNC CS: PDP-11/45. 16-Bit-Adressraum, kein Programm konnte mehr als 64 KB auf einmal ansprechen. Der IBM PC lag noch zwei Jahre in der Zukunft.
* **[Auslöser 7th Edition]:** Duke hatte unter 6th Edition Unix das `login`-Kommando so verändert, dass es Ankündigungen genau einmal pro Nutzer anzeigte. Der Umstieg auf 7th Edition machte den Patch unbrauchbar — eine Neuimplementierung wurde nötig.
* **[Warum nicht einfach Rundmail]:** Bewusst verworfen. Man wollte beim Login benachrichtigt werden und später Massendiskussion von persönlicher Post trennen.
* **[UUCP]:** 7th Edition Unix brachte UUCP mit — Wählleitungs-Dateikopie und Remote-Ausführung. Kein eigenes Protokoll nötig: „There was no point in reinventing the wheel."
* **[Autodialer aus Eigenbau]:** Modems unter Rechnersteuerung waren „very rare". Duke baute zwei 300-Baud-Autodialer selbst — DTR-Leitung schaltet ein Relais, das die Wählimpulse nachbildet (0,6 s auf, 0,4 s zu). Akustikkoppler umgingen zudem das AT&T-Anschlussmonopol, weil die einzige Verbindung zum Telefonnetz aus Schall bestand.
* **[Sterntopologie & Kostenumlage]:** Duke als Zentralknoten pollt jede Site, so oft sie will — Bedingung: die Site erstattet Duke die Telefonkosten. Bellovin rückblickend zur Gefahr: zentrale Knoten „effectively controlled what other sites could be on the network, and what they could see."
* **[Ortstarif-Absurdität]:** Duke und UNC liegen keine 15 Kilometer auseinander, gehörten aber zu verschiedenen Telefongesellschaften — Gespräche zwischen ihnen waren gebührenpflichtige „toll calls".

### Netzkultur-Kontext: Warum Selbsthilfe die einzige Option war

* **[Unix ohne Support]:** Der Konsent-Beschluss von 1956 verbot AT&T das Geschäft außerhalb der Telekommunikation. Folge: Unix ging für die Kosten des Magnetbands an Universitäten, aber ohne jeden Support. Bell-Labs-Folie auf Konferenzen: „No advertising, no support, no bug fixes, payment in advance."
* **[Tape-Kultur vor dem Netz]:** Bellovin über die Usenix-Treffen: man brachte eine Rolle Magnetband mit den eigenen Änderungen mit und nahm die Änderungen der anderen mit nach Hause. Das Usenet automatisiert genau diesen bereits existierenden Gabentausch.
* **[Namensherkunft]:** „Usenet" ist ein Wortspiel auf „Usenix" — und die Nutzergruppe hieß vorher schlicht „Unix Users Group", bis die Markenanwälte der Bell Labs eine Umbenennung erzwangen. Der Name trägt also gleich zwei Konzernabwehrreflexe in sich.
* **[Anti-Gremien-Haltung]:** Aus der Einladung von 1980, vorweggenommene Kritik und Antwort: „This is a sloppy proposal. Let's start a committee. No thanks! … But let's get started now. Once the net is in place, we can start a committee. And they will actually use the net, so they will know what the real problems are."
* **[Erwartete Inhalte]:** „The first articles will probably concern bug fixes, trouble reports, and general cries for help." Ergänzend genannt: „have/want"-Anzeigen. Bellovin bestätigt: Kleinanzeigen für Gebrauchtwagen waren von Anfang an eingeplant — aber nur regional gedacht.
* **[Haftungsfrage 1980]:** Die Einladung beantwortet die Frage nach Missbrauch schon vorab: Wer haftet? „Not us! And we do not intend that any innocent bystander be held liable either. We are looking into this matter. Suggestions are solicited."
* **[Sicherheit bewusst weggelassen]:** Kryptografische Authentifizierung wurde diskutiert und verworfen: „Promising false security is worse than leaving things insecure." Man wusste, dass man es nicht sicher hinbekommen würde.
* **[Wie schnell die Norm kippte]:** Weniger als drei Jahre nach dem Start begrüßt Bellovins neuer Vorgesetzter in den Bell Labs ihn mit: „Hi, Steve, I've seen your flames on Netnews." Das Wort „flame" ist im Oxford English Dictionary ab 1981 belegt, taucht in einer Mailinglist aber schon 1978 auf.
* **[Henne-Ei-Problem]:** Bellovin: „without more content, there was nothing to attract users, but without more users, there was no one to generate content." Aufgelöst durch Hortons Gateway zu den ARPANET-Listen — ausgerechnet das Netz, von dem man ausgeschlossen war, lieferte den ersten Gesprächsstoff.

### Offengelegte Widersprüche & Quellenkritik

* **[Widerspruch „geplantes Weltnetz" vs. Beleglage]:** Die verbreitete Gründungserzählung („zwei Studenten wollten die Unix-Welt vernetzen") kollidiert mit dem Aktenstand: Auslöser war ein durch ein Unix-Upgrade kaputtgegangenes lokales Anschlagbrett. Ellis und Truscott hatten zwar größere Ziele als Duke-Verwaltungsmeldungen, dachten aber ausdrücklich regional („the entire area"), nicht global.
* **[Widerspruch Selbstbild vs. Zahlen]:** Der Gründungstext gibt sich pragmatisch und selbstsicher, doch die Kernprognose lag um drei Größenordnungen daneben (50–100 Sites „ever" vs. 11.000 Sites bis 1988). Die Fehlprognose ist keine Fußnote, sie ist ins Design eingebaut: A News hatte fünfstellige Artikelnummern, kannte nur eine Lesemarke und erlaubte kein Lesen außer der Reihe.
* **[Widerspruch Zitatherkunft]:** Die Formel „a poor man's ARPANET" stammt nicht aus der Einladung vom Januar 1980, sondern aus dem Handout zur Usenix-Tagung in Delaware im Sommer 1980: „A goal of Usenet has been to give every UNIX system the opportunity to join and benefit from a computer network (a poor man's ARPANET, if you will)". Daniel weiß selbst nicht mehr, wer sie geprägt hat. Wer sie den Gründern als Gründungsmotto in den Mund legt, verschiebt die Chronologie.
* **[Widerspruch Wachstumszahlen]:** Wikipedia nennt „50 Sites im ersten Jahr". Spaffords Erhebung nennt 15 für 1980, Bellovins Karte zeigt im April 1981 rund 20 Knoten. Für Stufe 2 gilt die Spafford-Reihe; die 50 sind nicht belegt.
* **[Widerspruch Autorschaft]:** Populärquellen schreiben die C-Fassung mal Bellovin, mal Truscott, mal Daniel zu. Belegt ist: Bellovin schrieb den Prototyp (rund 150 Zeilen Bourne Shell, danach eine eigene C-Fassung), die ausgelieferte A-News-Version stammt von Stephen Daniel mit Truscott.
* **[Widerspruch PR vs. Selbstauskunft]:** Kommerzielle Usenet-Anbieter erzählen die Gründung gern als bewussten Gegenentwurf zum zentralistischen ARPANET. Bellovins Fachaufsatz sagt das Gegenteil: die Sterntopologie mit Duke als Nabe war eine Kostenentscheidung, deren Machtwirkung man nicht durchdacht hatte.

---

## Abschnitte

### Abschnitt 1 (Absatz 1): Ein kaputter Login-Gruß

* **Punkt:** Der Ursprung ist banal und lokal — kein Manifest, sondern ein Wartungsproblem im Herbst 1979.
* **Womit:** Duke steigt auf 7th Edition Unix um, der selbstgebaute Ankündigungs-Patch im `login` funktioniert nicht mehr `[Auslöser 7th Edition]`; Hardware-Rahmen PDP-11/70 und /45, 64 KB pro Programm `[Hardware]`; dasselbe Upgrade bringt UUCP mit — der Grund, warum aus dem Wartungsjob ein Netz werden konnte `[UUCP]`; Ellis und Truscott wollen mehr als Verwaltungsmeldungen, denken aber regional, inklusive Gebrauchtwagenanzeigen `[Widerspruch „geplantes Weltnetz" vs. Beleglage]`; erste drei Knoten `duke`, `unc`, `phs` `[Datierung]`.
* **Perspektive/Gegenstimme:** Gegen die Heldenerzählung: Truscott beschreibt das Motiv nüchtern als Isolationsgefühl gegenüber anderen Informatik-Fachbereichen `[Truscott via Giganews]`; Modell war eine verteilte Hauspost-Zeitung ohne Single Point of Failure `[Truscott via Giganews / Modell]`.
* **Läuft hinaus auf:** Die Frage, warum diese Leute überhaupt selbst bauen mussten, statt sich an das bereits existierende Netz anzuschließen.

### Abschnitt 2 (Absatz 2): Das Netz für die, die nicht reindurften

* **Punkt:** Das Usenet ist ein Ausschluss-Produkt. Die Mittellosigkeit ist keine Anekdote, sie hat die Architektur bestimmt — offen für jeden, weil es kein Gremium gab, das Zugang hätte vergeben können.
* **Womit:** Die ARPANET-Zugangsregel `[Zugangsregel ARPANET]`; Daniels Kostenrechnung „political connections and $100,000" `[Daniel via Hauben 1993 / Kosten]` und der Satz „we knew we were excluded" `[Daniel via Hauben 1993]`; die Herkunft der Formel „poor man's ARPANET" korrekt datiert `[Widerspruch Zitatherkunft]`, `[Delaware Sommer 1980]`; Ellis' Auftritt in Boulder mit 80 Kopien vor 400 Leuten `[Boulder Januar 1980]`, `[Truscott via Hauben 1993 / Boulder]`; die Anti-Gremien-Passage aus der Einladung als Haltung, nicht als Floskel `[Anti-Gremien-Haltung]`; die materielle Basis: zwei selbstgebaute 300-Baud-Autodialer `[Autodialer aus Eigenbau]`, Ortsgespräche, die keine waren `[Ortstarif-Absurdität]`, 0,50 Dollar für drei Minuten `[Telefonkosten]`.
* **Perspektive/Gegenstimme:** Die Selbsthilfe-Kultur war erzwungen, nicht gewählt — AT&T durfte Unix nicht unterstützen, „no support, no bug fixes" `[Unix ohne Support]`; das Usenet automatisierte nur den Bandtausch, den es schon gab `[Tape-Kultur vor dem Netz]`. Gegen das Bild vom bewussten Gegenentwurf: die Sterntopologie war eine Kostenentscheidung, deren Machtwirkung unreflektiert blieb `[Widerspruch PR vs. Selbstauskunft]`, `[Sterntopologie & Kostenumlage]`.
* **Läuft hinaus auf:** Dass die Erbauer zwar das Netz richtig bauten, aber vollständig falsch einschätzten, wofür Menschen es benutzen würden.

### Abschnitt 3 (Absatz 3): Die Fehlprognose, aus der die Netzkultur wurde

* **Punkt:** Die Gründungsschrift kennt Bugreports und Kleinanzeigen — aber keine Gesellschaft. Alles, was das Usenet kulturell ausmachte, ist ungeplant entstanden, und zwar schneller, als die Beteiligten mitkamen.
* **Womit:** Bellovins Prognose 1–2 Artikel pro Tag, 50–100 Sites „ever" `[Bellovin 2024]`, Truscotts Newsletter-Analogie `[Truscott via Giganews / Modell]`; die Blindstelle: kein Wort über soziale Nutzung `[Bellovin 2024 / Blindstelle]`, `[Erwartete Inhalte]`; die Wachstumsreihe von 3 Sites auf 11.000 `[Wachstum Spafford 1988]` gegen die zähen ersten 15 Monate `[Netzkarte 1981]`, `[Daniel via Hauben 1993 / Enttäuschung]`; die Ironie des Durchbruchs: Inhalt kam ausgerechnet aus dem ARPANET, per Gateway zu SF-LOVERS und HUMAN-NETS `[Horton]`, `[Henne-Ei-Problem]`; wie schnell die Umgangsformen kippten `[Wie schnell die Norm kippte]`; Sicherheit war bewusst weggelassen `[Sicherheit bewusst weggelassen]`, Haftung offen gelassen `[Haftungsfrage 1980]`.
* **Perspektive/Gegenstimme:** Aus Sicht der Beteiligten fühlte man sich trotz eigenem Netz weiter als arme Verwandtschaft — „read-only mode on human-nets and sf-lovers" `[Daniel via Hauben 1993 / arme Verwandte]`. Dagegen der eine Punkt, in dem sie den Etablierten voraus waren: beim Usenet bestimmt der Empfänger, was er bekommt, nicht ein Listenbetreiber `[Daniel via Hauben 1993 / Architekturphilosophie]`.
* **Läuft hinaus auf:** Bellovins Bilanz „we never planned for success" `[Bellovin 2024 / Fazit]` — und damit die Übergabe an den Hauptteil des Artikels: was aus einem Netz wird, das für den Erfolg nie ausgelegt war (Hierarchien, Great Renaming, Backbone Cabal, alt.*, Spam, Niedergang).

---

## Quellen

* **[Bellovin 2024]** = Bellovin, Steven M.: „Netnews: The Origin Story", IEEE Annals of the History of Computing, 2024, DOI 10.1109/MAHC.2024.3420896 (Preprint: cs.columbia.edu/~smb/papers/netnews-hist.pdf) — Erstimplementierer, begutachteter Fachaufsatz; wichtigste Einzelquelle.
* **[Hauben 1993]** = Hauben, Ronda: „The Evolution of Usenet: The Poor Man's ARPANET" (Netizens, Kapitel 2), 1993/1997 — enthält die E-Mail-Korrespondenz mit Stephen Daniel, Truscotts Boulder-Bericht und Spaffords Wachstumsreihe.
* **[Truscott/Ellis 1980]** = Truscott, Tom / Ellis, Jim: „Invitation to a General Access UNIX Network", Duke University 1980; Nachdruck im Australian Unix Users Group Newsletter, Bd. IV Nr. II, April/Mai 1980, S. 15–18 — Primärdokument, auch als Anhang B in [Bellovin 2024].
* **[Giganews/Truscott]** = Giganews Usenet History: Interview mit Tom Truscott, giganews.com/usenet-history/truscott/ — Anbieter-PR-Umfeld, aber wörtliche Selbstauskunft; nur für O-Töne verwendet.
* **[Spafford 1988]** = Spafford, Gene: Usenet-Wachstumsstatistik, vorgelegt auf einem IETF-Treffen 1988, Usenet History Archives (nethist.901011) — zitiert nach [Hauben 1993].
* **[Horton 1981]** = Horton, Mary Ann: „USENET Logical Map", 5. April 1981 — abgedruckt in [Bellovin 2024], Fig. 1.
* **[Salus/USENIX]** = Salus, Peter H.: „The Strange Birth and Long Life of Unix", IEEE Spectrum 2005, sowie USENIX-Jubiläumsdarstellung (usenix.org, login: 2015) — Beleg für Konsent-Beschluss 1956, fehlenden AT&T-Support und die Bandtausch-Kultur der Nutzergruppen.
* **[Wikipedia/Usenet]** = Wikipedia-Artikel „Usenet", Abruf 08/2026 — nur als Abgleich verwendet; Angabe „50 Sites im ersten Jahr" widerspricht [Spafford 1988] und wird nicht übernommen.
