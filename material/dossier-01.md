---
role: material
readers: editor-outline, copyedit-facts
when: vor dem ersten Satz eines Abschnitts dieses Kapitels
mode: lookup
agent-visible: yes
---

# Dossier: Bevor das Internet ein öffentlicher Ort war

Recherchiertes Material für Kapitel 01. Herkunft steht am Eintrag; was hier steht, muss nicht neu
recherchiert werden. Was fehlt, wird vor dem Schreiben recherchiert und kommt hierher.

> Teile davon wurden unter dem alten Schnitt als „Die ersten digitalen Gesellschaften" recherchiert.

## Netze und Systeme

- **ARPANET → TCP/IP** am 1. Januar 1983 (Flag Day), gilt als Übergang zum heutigen Internet.
- **Usenet**: 1979 von den Duke-Doktoranden **Tom Truscott** und **Jim Ellis** entworfen, 1980 erste
  Verbindung Duke ↔ University of North Carolina; lief über UUCP, hieß „poor man's ARPANET";
  dezentral, kein zentraler Server.
- **Great Renaming** 1987: Neuordnung in die Hierarchien comp/misc/news/rec/sci/soc/talk; die
  **alt.\***-Hierarchie (1987) für alles Übrige, erste Gruppen u. a. alt.sex, alt.drugs,
  alt.rock-and-roll.
- **IRC**, Jarkko Oikarinen, Universität Oulu, 1988; Kanäle mit `#`, Nicks, Ops. Während des
  **Putschversuchs in Moskau im August 1991** liefen Live-Berichte über IRC (und Relcom/Usenet) nach
  draußen. (Zur Sicherheit „1991" ohne Tagesdatum verwenden.)
- **MUD** (Multi User Dungeon): erster 1978 an der University of Essex, **Roy Trubshaw** und
  **Richard Bartle**; textbasierte Mehrspielerwelten, Vorläufer der Online-Rollenspiele.
- **Eternal September**: ab September 1993 ließ **AOL** seine Kunden ins Usenet, der Neulingsstrom
  riss nicht mehr ab.
- **Deutschland**: Am **3. August 1984** empfing die **Universität Karlsruhe** die erste deutsche
  E-Mail über **CSNET**; Anbindung durch **Werner Zorn**, Adressat **Michael Rotert**.
  Deutschsprachiges Usenet unter der **de.\***-Hierarchie.
- **Tim Berners-Lee** schlug das **World Wide Web** 1989 am **CERN** vor. Brücke zu Kapitel 02.

## Umgangsformen

- **RFC 1855 „Netiquette Guidelines"**, Oktober 1995 (Sally Hambridge).
- **Godwins Gesetz**, Mike Godwin, 1990.
- **Killfile** = persönliche Filter-/Sperrliste gegen unerwünschte Poster.

## Szene

- **Chaos Computer Club** gegründet 1981; BTX-Hack gegen die Hamburger Sparkasse im November 1984.

## AfroNet

Recherchiert am 2026-08-07, noch nicht nach `material/quellen/` gesichert.

- **Ken Onwere**, in den USA geborener Nigerianer, wohnhaft in San Diego, gründete das **AfroNet**
  **1993** als FidoNet-basiertes Mailsystem.
- Aufgebaut mit vier Sysops: **Idette Vaughan** (*The BlackNet*), **Alex Hartley** (*Alex's Place*),
  **Nathaniel Saunders** (*Minority Affairs*), **John Alston** (*VulcanNet*).
- Technisch ein **Echomail-Backbone**, der Konferenzen mit afrikanischen und afroamerikanischen
  Themen von der West- zur Ostküste verteilte. Freiwillig betrieben, Zugang frei und offen.
- Beteiligte beschreiben es als den Ort, an dem man „seine Leute" fand, und als Verschnaufpause von
  dem Rassismus, der ihnen im übrigen frühen Netz entgegenschlug.
- Konkreter Vorgang, bisher **einfach belegt**: Das AfroNet verbreitete Berichte aus erster Hand
  über Rassismus bei **AT&T**.
- Ältere Einzelsysteme liefen davor, etwa *SpiritDatatree* von **William Murrell** in Boston ab
  **April 1992**.
- **Offen:** Laufzeitende und Knotenzahl nennt keine Quelle.
- Quellen: [loriemerson.net](https://loriemerson.net/2021/04/12/excavating-future-histories-of-the-internet-afronet-newsletter-telegraph/) ·
  [blacksoftware.com](https://blacksoftware.com/before-blacks-had-the-internet/) ·
  [LARB](https://lareviewofbooks.org/article/alternative-internets-and-their-lost-histories/) ·
  [AFRONET BBS List](https://www.africa.upenn.edu/BBS_Internet/afro_bbs.html) (403 beim Abruf).
  Dazu Charlton McIlwain, *Black Software*, bisher ungelesen.

## Die Gründung des Usenets

Recherchiert am 2026-08-07, noch nicht nach `material/quellen/` gesichert. Hauptquelle ist **Steve
Bellovins eigene Darstellung** „The Early History of Usenet" (achtteilig, CircleID / sein
Columbia-Blog, November/Dezember 2019). Beteiligter, also Zeitzeuge mit dem üblichen Vorbehalt,
aber die einzige Darstellung aus erster Hand.

- **Zugangsschranke ARPANET, wörtlich bei Bellovin:** „To be on it, you had to be a defense
  contractor or a university with a research contract from DARPA." Duke und die UNC waren beides
  nicht. Deckt die Formulierung in `fakten.md`, wonach der Grund für „ARPANET des armen Mannes" das
  **Zugangsprivileg** war, nicht der Leitungspreis.
- **Der Anlass war ein Upgrade, kein Netzplan.** Bellovin (Teil I): unmittelbarer Auslöser war „the
  desire to upgrade to 7th Edition Unix"; das dortige lokale Aushang-Programm musste ersetzt werden.
  en.Wikipedia nennt Usenet entsprechend „a replacement for a local announcement program". **Zwei
  Quellen, beide sekundär bis erste Hand, für den Text tragfähig, aber nicht überstrapazieren.**
- **UUCP lag schon auf der Maschine:** „7th Edition had UUCP (Unix-to-Unix Copy), a dial-up
  networking facility" (Bellovin, Teil I). Dazu: „The only thing that was halfway common was the
  dial-up modem, which ran at 300 bps." The Register (2010): „two 300 baud auto-diallers".
- **Erste Implementierung:** Bellovin schrieb sie an der UNC als **Bourne-Shell-Skript, rund 150
  Zeilen** („It was about 150 lines long", Teil IV), inklusive mehrerer Newsgroups und
  Cross-Posting; danach von ihm in C nachgezogen, aber nie veröffentlicht. Die **freigegebene**
  Fassung („A News") schrieben **Steve Daniel** und **Truscott** (en.Wikipedia). LivingInternet
  schreibt die Shell-Fassung fälschlich als „three pages" und den C-Umbau Truscott/Daniel zu; im
  Zweifel gilt Bellovin.
- **Öffentliche Vorstellung:** Januar 1980, **Usenix-Konferenz in Boulder, Colorado**. Ellis
  verteilte ein **fünfseitiges Handout „Invitation to a General Access UNIX Network"** (The
  Register; Scan: [archive.org](https://archive.org/details/usenet_a_general_access_unix_network_1980),
  Autoren Daniel/Ellis/Truscott). Bellovin selbst war nicht dabei: „This meeting was in Boulder; I
  wasn't there, but Tom Truscott and Jim Ellis were."
  - **Nur einfach belegt** (LivingInternet, sonst nirgends): Ellis habe alle **achtzig**
    mitgebrachten Kopien der Software verschenkt. Schöne Konkretion, aber ungedeckt.
- **Die Fehleinschätzung, tragende Perle.** Bellovin, Teil IV, wörtlich: „I predicted that the
  maximum Usenet volume, ever, would never exceed 1-2 articles per day." Er nennt das „one of my
  most laughable errors" und rechnet dagegen: heute „over 60 tebibytes per day, with more than
  100,000,000 posts per day". Die Annahme **prägte den Bau**: keine Verzeichnisse je Standort,
  Dateiname und Zeitstempel als einzige Metadaten, denn „they don't matter if you're only receiving
  1-2 articles per day".
- **Was sie erwarteten, laut Ankündigung** (Bellovin, Teil VI): „The first articles will probably
  concern bug fixes, trouble reports, and general cries for help." Und sein Befund über das, was
  fehlte: „The most interesting thing, though, is what the announcement didn't talk about: any
  non-technical use. We completely missed social discussions, hobby discussions, politial [sic]
  discussions, or anything else like that."
- **Der Zünder war fremder Inhalt.** Berkeley hing an **beiden** Netzen (UUCP-Verbindung zu Bell
  Labs Research **und** ARPANET-Anschluss). **Mary Ann Horton**, dort Doktorandin, richtete das
  Gateway ein und speiste die ARPANET-Verteiler **`SF-LOVERS`** (Science-Fiction) und
  **`HUMAN-NETS`** (gesellschaftliche Folgen der Vernetzung) in Usenet-Gruppen ein; die landeten in
  der Hierarchie **`fa.*`** für „from ARPANET". Bellovin, Teil VII: „With an actual traffic source,
  it was easy to sell folks on the benefits of Usenet. People would have preferred a real ARPANET
  connection but that was rarely feasible."
  - **Namensfrage:** Sie veröffentlichte damals als *Mark Horton*; Bellovin (2019) und en.Wikipedia
    schreiben durchgehend **Mary Ann Horton** und „she". Für den Text übernommen, ohne den
    Namenswechsel zum Thema zu machen. → Entscheidung liegt bei Oli, vermerkt in `issues-01.md`.
  - **`SF-LOVERS` ist damit der Bogen zu 01.02**, wo der Verteiler als ARPANET-Mailingliste
    eingeführt wird. Löst den offenen Punkt „SF-LOVERS steht zweimal da, in zwei Medien".
  - **Datierung des Gateways unscharf.** Berkeley kam laut Bellovin (Teil VII) im ersten Sommer als
    einer von vier neuen Standorten dazu (mit Reed College, University of Oklahoma und `vax135`);
    wann genau das Gateway lief und wann die Gruppen nach `fa.*` umzogen, sagt er nicht („at some
    point moved"). Im Text deshalb ohne Jahreszahl.
- **Wachstum:** **rund 50 Standorte im ersten Jahr**, darunter Bell Labs, Reed College, University
  of Oklahoma; **1983 über 500 Rechner** (en.Wikipedia). Beide Zahlen nur dort, nicht gegengeprüft.
- Quellen: Bellovin, *The Early History of Usenet*, Teile
  [I](https://circleid.com/posts/20191115_the_early_history_of_usenet_part_i_the_technological_setting) ·
  [IV](https://circleid.com/posts/20191123_the_early_history_of_usenet_part_iv_implementation_user_experience) ·
  [VI](https://circleid.com/posts/20191127_the_early_history_of_usenet_part_vi_the_public_announcement) ·
  [VII](https://circleid.com/posts/20191202_the_early_history_of_usenet_part_vii_usenet_growth_and_b_news) ·
  [The Register (2010)](https://www.theregister.com/2010/05/20/usenet_duke_server/) ·
  [LivingInternet](https://www.livinginternet.com/u/ui_netnews.htm) (schwächste der vier) ·
  en.Wikipedia „Usenet".
