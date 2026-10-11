---
role: state
readers: claude, editor
when: laufend, sobald ein Punkt offen bleibt
mode: lookup
agent-visible: no
---

# Offene Punkte: Kapitel 01

Alles, was an Kapitel 01 noch zu tun ist. Claude pflegt diese Liste **selbst und sofort**: Jeder
Befund, der nicht auf der Stelle behoben wird, landet hier, bevor er im Chat auftaucht.
Erledigtes wird gelöscht; was dabei entschieden wurde, kommt nach `decisions.md`.

- **Regeln der Reihe** → [konventionen.md](konventionen.md)
- **Abgelehnte Befunde** → [decisions.md](decisions.md)
- **Belegte Sachverhalte** → [knowledge/fakten.md](../knowledge/fakten.md)
- **Werkweite Punkte** → [issues.md](issues.md)

---

## Zu entscheiden (Oli)

- **01.06, vor Stufe 2** (geschärfte Outline vom 2026-09-30, `material/outline/01.06.md`):
  - **Der Eintrag `black hat` von 2001 im Jargon File.** Neu recherchiert, Primärquelle: erste Fassung
    mit dem Wort ist 4.3.0 vom 30. April 2001, vermerkt „[common among security specialists]",
    erklärt als „A cracker". Steht jetzt in Kernthese und Abschnitt 6 und baut den Schluss (das
    Wörterbuch hält ihn für einen Cracker, draußen kommt er als Hacker zurück). Ohne ihn: Hüte nur mit
    Western, „1990 kein Hut" und „spätestens Ende der Neunziger".
  - **Zwei Streichungen kommen teilweise zurück.** Kochs Gang zum Verfassungsschutz 1988 als
    Nebensatz (Faktencheck: sonst liest sich Stolls Spur als das, was die Gruppe zu Fall brachte) und
    Levys Punkt 1 mit zwei Wörtern Zitat, „unbegrenzt und vollständig" (Diagnose: sonst trägt „keiner
    setzt eine Grenze" nicht).
  - **Sundevils Ruf, mit Bruce Sterling beim Namen.** Kostet einen Belegpunkt und eine Person, trägt
    aber die Einordnung (Razzia gegen Betrug, öffentlich als Schlag gegen die Hacker gelesen) und den
    Übergang zu Abschnitt 6. Ohne ihn endet Abschnitt 5 auf den Mailboxen, und Abschnitt 6 beginnt
    wie bisher mit der Presse.
  - **§ 202a ohne die Neufassung von 2007?** Die Outline lässt 2007 draußen, Präteritum und „sollte
    straflos bleiben" tragen. Ein Halbsatz „seit 2007 genügt der Zugang" kostet einen Belegpunkt und
    beantwortet die Frage, die ein heutiger Leser hat.
  - **Umfang:** rund 1.040 statt 900 bis 950 Wörter, 32 statt 29 Belegpunkte. Die Dichte bleibt bei
    gut drei je hundert Wörter.

- **Wie heißt Horton im Text?** Für den neu gefassten H3 „Entstehung des Usenets" (01.04) ist das
  Berkeley-Gateway recherchiert, das die ARPANET-Verteiler `SF-LOVERS` und `HUMAN-NETS` in die
  `fa.*`-Gruppen einspeiste. Eingerichtet hat es **Mary Ann Horton**, die damals als *Mark Horton*
  veröffentlichte. Bellovin (2019) und en.Wikipedia schreiben durchgehend Mary Ann Horton und „she";
  die zeitgenössischen Usenet-Quellen kennen nur Mark Horton. Vorschlag und aktueller Stand im
  Entwurf: **Mary Ann Horton**, ohne den Namenswechsel im Text zum Thema zu machen. Betrifft die
  ganze Reihe, sobald sie später noch einmal vorkommt (B-News, `vi`, Berkeley-Unix).

- **Zeitraum des Kapitels.** Der Kopf sagt „etwa 1978 bis 1994". Die Demoszene-Bilder reichen bis
  1997, der Ausblick bis in die Gegenwart. Entweder den Zeitraum auf 1996/97 dehnen oder ihn als
  ungefähre Ära lesen und so lassen. (Bilder und Ausblick bleiben, das ist entschieden.)
  Mit dem neuen 01.01 (C64, Amiga) passt „1978 bis 1994" vorn wie hinten: C64 ab 1983 in
  Deutschland, Commodore-Konkurs und C64-Produktionsende 1994. Der neue Abschnitt verlangt keine
  Änderung.

- **Titel „Die Anfänge der Netzkunst".** Der Titel weckt die Erwartung auf den Kunstbetrieb, der in
  dieser Reihe nicht vorkommt (siehe [konventionen.md](konventionen.md)). Der H2 erzählt die Kunst der
  Szene: von unten, aus der Grenze der Maschine, ohne das Wort Kunst. Titel entsprechend fassen.
- **Der H2 braucht eine These.** Der Rahmensatz ordnet die drei H3 nur zeitlich zu („in denselben
  Jahren"), nicht sachlich. Was die drei verbindet, steht nirgends: Kunst aus der Grenze der
  Maschine, verteilt über dasselbe Netz wie die Raubkopien, entstanden aus einer Straftat, bezahlt
  nicht in Geld, sondern im Ansehen der Szene. Ohne diesen Satz liest sich der Abschnitt als drei
  Einzelthemen.
- **Die drei H3 laufen auf verschiedenen Achsen:** Demoszene ist eine Gemeinschaft, ASCII eine Form,
  der Tracker ein Werkzeug. Prüfen, ob eine gemeinsame Achse den Abschnitt rund macht oder ob der
  Rahmensatz genügt.

- **Reihenfolge der Stationen in 01.03.** Sie steht jetzt Post → Spam → MUDs → Karlsruhe → IRC und
  schiebt damit zwei Fäden ineinander: Mail (Station 1, 2, 4) und Echtzeit/Textwelten (3, 5).
  `copyedit-coherence` schlägt **Post → Spam → Karlsruhe → MUDs → IRC** vor. Dann läuft der Mail-Strang in
  einem Zug 1971 → 1978 → 1984, der Echtzeit-Strang 1978 → 1988, und der IRC-Einstieg findet die
  MUDs direkt vor sich statt zwei Stationen entfernt. Verschiebt zwei bestehende H3, deshalb deine
  Entscheidung.
- **Die MUD-Station widerlegt die IRC-Station.** Bestand schon vorher. Die MUDs schildern Spieler,
  „die zeitgleich online waren"; der IRC-Einstieg sagt zehn Jahre später „Mailboxen und
  Mailinglisten waren Schreibmedien" und lässt die MUDs genau da weg, wo sie seine Behauptung
  widerlegen. 01.02 nennt zusätzlich „Diskussionsforen und Chats" in Mailboxen. Entweder der
  IRC-Einstieg grenzt sich gegen die MUDs ab, oder er verzichtet auf die Erstheit.
- **Vier Premieren auf zwei Seiten.** „Die erste Spam-Mail" und „Die erste Mail nach Karlsruhe" als
  Überschriften, dazu „die erste Nachricht von einem Rechner zu einem anderen" und „die erste
  [Mailingliste]" im neuen H3. Die Erste-Geste entwertet sich. Eine davon kann anders ansetzen.
- **`SF-LOVERS` steht zweimal da, in zwei Medien.** Neu im H3 als Mailingliste, in 01.04 als
  „Stammgast in `rec.arts.sf-lovers`". Gleicher Name, kein Signal, dass es dieselbe Runde ist, die
  ins Usenet umgezogen ist. Als Bogen nutzen oder eines von beidem ersetzen.
- **Anonyme FTP-Archive haben keinen Platz.** Der neue H3 „Die ungeplante Erfindung der E-Mail" führt FTP
  als Nutzung ein (Dateien von einem fremden Rechner holen), nicht als Ort. Die öffentlichen Archive,
  in denen man stöberte, und ihre Suche (Archie) kommen nirgends vor, obwohl sie das sind, was vom
  Dateitransfer kulturell blieb. Entweder in „Das Erbe wandert ins Web" (01.10) aufnehmen oder
  bewusst weglassen.

## Zu erledigen (Claude)

- **01.01 nach dem dritten Prüflauf überarbeitet** (2026-09-29): erste Hälfte einzeln korrigiert,
  Amiga-Teil neu geordnet, Olis Satz eingebunden, Olis Korrekturen übernommen (Schlusssatz
  gestrichen, „später“, „Viele der alten Hefte …“). Der Abschnitt endet wieder auf den Compilern.
  Neue Fassung noch ohne Prüflauf (clarity, language).
- **Baustein für 01.04 „Die deutsche Ecke des Usenets": Amiga als Usenet-Knoten.** Entschieden
  (Oli, 2026-09-27): gehört nach 01.04, nicht nach 01.01. Private Knoten im Sub-Netz (`sub.*`)
  liefen auf Amigas mit Dillon UUCP, belegt über die UUCP-Karten `u.sub.*` vom Januar 1994;
  Material in `material/dossier-01.md`, Abschnitt „Heimcomputer (01.01)", Eintrag „Amiga im Usenet".

- **„Hierarchien" fällt im Schlussabsatz von „Entstehung des Usenets" (01.04) ohne Einführung** und
  wird vom Folge-H3 („Diese Hierarchien …") als bekannt vorausgesetzt. Bestand in der alten Fassung
  genauso, ist also kein Schaden des Umbaus, aber weiterhin die schwächste Naht im H2. Löst sich von
  selbst, wenn `fa.*` in „Die Kartografie der Subkulturen" einzieht, weil dort die erste Hierarchie
  benannt und gezeigt wird (siehe [kandidaten.md](../material/kandidaten.md)).

- **Prüflauf über den neu gefassten H3 „Entstehung des Usenets"** (01.04, Fassung vom 2026-08-07,
  201 Wörter): `copyedit-clarity`, `copyedit-language`, danach `copyedit-coherence` über den ganzen
  H2. Belege stehen vollständig in [dossier-01.md](../material/dossier-01.md) § „Die Gründung des
  Usenets" (recherchiert 2026-08-07, Snapshots nach `material/quellen/` fehlen noch). Im Text steht
  davon nur noch ein Bruchteil; alles Weggelassene ist eine Entscheidung und **kein Rechercheloch**,
  siehe [decisions.md](decisions.md). Zu prüfen bleibt für den Text, wie er jetzt dasteht:
  - **Bellovins Ein-bis-zwei-Beiträge-Prognose** und die Folgen für die Ablage. Aus seiner eigenen
    Darstellung von 2019, also Zeitzeuge über sich selbst, vierzig Jahre danach.
  - **Die Ankündigung von 1980** wird zitiert, ohne Ort und Anlass zu nennen (Usenix, Boulder,
    fünfseitiges Handout). Bewusst so; falls die Stelle einen Anker braucht, liegt er im Dossier.
  - **Die Cancel-Nachricht seit 1983** stammt noch aus der alten Fassung und ist nie belegt worden.
  - **Warum die Duke keinen ARPANET-Anschluss hatte, steht bewusst nicht im Text**, nur „und an
    einen zu kommen war nicht leicht". Die Bedingung ist belegt (Bellovin: „To be on it, you had to
    be a defense contractor or a university with a research contract from DARPA"), 01.03 hat sie dem
    Leser schon gesagt, und ausformuliert lud sie den Absatz politisch auf. Nicht nachtragen.

- **`copyedit-facts` über den neuen H3 „Die ungeplante Erfindung der E-Mail"** (01.03, vor der Spam-Mail
  eingefügt, weil E-Mail und Mailinglisten im ganzen Werk dreimal vorausgesetzt und nie eingeführt
  waren). `copyedit-clarity`, `copyedit-language` und `copyedit-plausibility` sind zweimal gelaufen und eingearbeitet, die
  Recherche fehlt noch. Bereits belegt: FTP RFC 114 vom 16. April 1971 (siehe
  [fakten.md](../knowledge/fakten.md)); Tomlinson bei BBN 1971, SNDMSG plus CPYNET, @-Zeichen.
  **Offen und vor der Veröffentlichung zu klären:**
  - Die Drei-Viertel-Zahl. Die Auftragsstudie wird als **1973** *und* als **1974 (MITRE)** datiert,
    die Quellen widersprechen sich; deshalb steht im Text nur „Mitte der Siebziger" und keine
    beauftragende Stelle. Zu klären ist außerdem die Messgröße: Anteil an Nachrichten, Paketen oder
    Bytes. Als Byte-Anteil ist die Zahl gegen den Dateitransfer erklärungsbedürftig.
  - Der Name der Agentur ist im Text bewusst weggelassen, weil sie ab dem 23. März 1972 **DARPA**
    hieß (zurückbenannt erst 1993). „ARPA" wäre für Mitte der Siebziger falsch, „DARPA" widerspricht
    dem Rahmenabsatz, der für 1969 vom ARPANET spricht. Wenn die Stelle einen Akteur braucht, muss
    die Umbenennung mit hinein.
  - `SF-LOVERS`: Gründungsjahr strittig (**1979 durch Roger Duffy/Duffey vom MIT** nach den
    ausführlicheren Quellen, fancyclopedia sagt „about 1975"), deshalb steht im Text kein Jahr und
    kein Name. Der Superlativ „die meistgelesene" braucht einen Maßstab und einen Zeitraum. Wer die
    Sammelausgaben einführte, ist ungeklärt.
    **Herausgelassen, weil nur sekundär belegt, aber der stärkere Stoff:** Die Liste wurde für
    einige Monate abgeschaltet, weil sich keine dienstliche Begründung finden ließ, und kam mit dem
    Argument zurück, so viel freiwilliger Verkehr sei die Belastungsprobe, die dem Netz sonst fehle.
    Daneben existiert eine abweichende Erzählung über den Golden-Fleece-Preis von Senator Proxmire.
    Wenn sich eine belastbare Quelle findet, gehört das in den Text: Es ist dieselbe Norm, an der
    zwei Absätze später die Werbemail scheitert.
  - MsgGroup 1975 als **erste** Mailingliste: Erstheitsbehauptung, bisher nur aus Timeline-Quellen.
    Steve Walker als Einrichter steht deshalb nicht im Text.
  - Aus Weltwissen und nicht belegt: der eigene Maschinensaal, Los Angeles/Boston als Beispielpaar
    und der Bandversand als übliche Praxis. Die Geografie stimmt (UCLA war der erste Knoten), aber
    die Ostküstenknoten kamen erst 1970 dazu, und der Rahmensatz „Seit 1969" lädt dazu ein, das
    Beispiel auf 1969 zu beziehen. Ebenfalls zu prüfen, ob Remote Login 1971 schon im Betrieb war
    oder erst nach der ICCC-Demo von 1972.
- **`copyedit-facts` über den neuen H3 „Ein Netz für Rechenzeit"** (01.03, geschrieben 2026-08-06,
  ersetzt den früheren H3 „Die ungeplante Erfindung der E-Mail" und erweitert ihn zur
  Nutzungsgeschichte in drei Stationen: Einloggen, Dateien holen, Nachrichten schreiben).
  `copyedit-clarity`, `copyedit-language`, `copyedit-coherence` und `copyedit-plausibility` sind
  gelaufen und eingearbeitet, die Recherche fehlt. Paketvermittlung, IMP, Erfinderfrage und die erste
  Übertragung von 1969 stehen nicht im Text und sind für diesen Abschnitt nicht zu recherchieren.
  Offen ist alles, was über den früheren Textstand hinausgeht:
  - **BBN als Auftragnehmer**, Firmensitz Cambridge, Massachusetts. Trägt zwei Absätze später die
    Pointe, dass Tomlinson dort arbeitete.
  - **Telnet und der Fernschreiber sind wieder aus dem Text heraus** (2026-08-06, Olis Kürzung): Der
    Abschnitt beantwortet jetzt nur noch Ort, Zweck, FTP und E-Mail. Das Einloggen steht als Zweck in
    einem Nebensatz, ohne Namen und ohne Gerät. Die Zeile „Telnet als Alltagswerkzeug" in
    [kandidaten.md](kandidaten.md) bleibt damit offen.
  - **Die ARPA als Geldgeber der amerikanischen Computerforschung** („finanzierte damals einen großen
    Teil"). Neu im Text, weil sonst nicht erklärt ist, was das Verteidigungsministerium mit
    Universitätsrechnern zu tun hat. Größenordnung belegen oder abschwächen.
  - **Mehrere Leute gleichzeitig an einem Großrechner**, Voraussetzung dafür, dass ein Postfach vor
    dem Netz überhaupt Sinn ergibt.
  - **FTP-Autor Abhay Bhushan (MIT).** RFC 114 und der 16. April 1971 sind belegt
    ([fakten.md](../knowledge/fakten.md)), der Name nicht. Ebenfalls offen, **ab wann FTP tatsächlich
    lief**: Ein Spezifikationspapier beendet den Bandversand nicht, der Text behauptet das jetzt auch
    nicht mehr, aber die Formulierung hängt am Beleg.
  - **Anonymes FTP:** Login als `anonymous` mit der eigenen Mailadresse als Passwort, ohne Prüfung.
    Im Text auf „in den Achtzigern" datiert, weil die Konvention eine verbreitete Mailadresse
    voraussetzt. Datierung belegen. Damit ist der Punkt „Anonyme FTP-Archive haben keinen Platz"
    (unten) beantwortet: sie stehen jetzt hier.
  - **Postfächer vor dem Netz**, Nachrichten zwischen Benutzern derselben Maschine, „seit Mitte der
    Sechziger" (CTSS am MIT, 1965). Trägt die Pointe der E-Mail-Station, deshalb belegpflichtig.
  - **Der Rüffel** aus dem Verteidigungsministerium: belegter Vorgang oder weitergereichte Anekdote?
    Dazu „allerdings aus **rein** bürokratischen Gründen", das Ausschließlichkeit behauptet, und die
    Frage, welche Behörde zuständig war. Steht seit dem früheren Textstand unbelegt da.
  - **Die Agentur ist im Text jetzt namenlos**, wo es um die Siebziger geht („Eine Untersuchung
    ergab", „Die Forschungsabteilung kassierte einen Rüffel"), weil sie ab dem 23. März 1972 DARPA
    hieß. Der Auftrag von 1968/69 nennt sie weiterhin ARPA. Wenn die Stelle einen Akteur braucht,
    muss die Umbenennung in den Text.
  - Unverändert offen aus dem früheren Textstand: die Drei-Viertel-Zahl samt Messgröße, `MsgGroup`,
    `SF-LOVERS`, der Bandversand als übliche Praxis.

- **`copyedit-facts` über den neuen H3 „Requests for Comments (RFCs)"** (01.03, geschrieben
  2026-08-06, eingesetzt zwischen „Das ARPANET" und „Die erste Spam-Mail"). Keine Linse ist bisher
  darüber gelaufen. Belegt ist nur die Nummer 114 vom 16. April 1971 ([fakten.md](../knowledge/fakten.md)),
  alles andere steht aus Modellwissen im Text:
  - **RFC 1 „Host Software", 7. April 1969, Steve Crocker an der UCLA.** Datum, Nummer und Autor
    gelten als gesichert, sind aber nicht geprüft. Im Text steht kein Titel und keine Nummer, nur
    „den ersten dieser Texte".
  - **Die Bescheidenheit des Namens als Absicht.** Der Text behauptet, Crocker habe bewusst nicht als
    Vorschrift überschrieben, weil ihm die Befugnis fehlte. Das ist Überlieferung der Beteiligten und
    trägt den ganzen Absatz. Wenn es sich nicht halten lässt, muss der Absatz anders ansetzen.
  - **„Doktoranden schrieben die Regeln auf."** Zusammensetzung der Network Working Group belegen;
    ebenso, dass Professoren und die Behörde tatsächlich nichts vorschrieben.
  - **Nummern werden nie neu vergeben, Texte nie geändert**, ein neuer erklärt den alten für überholt
    („Obsoletes/Obsoleted by"). Ab wann diese Praxis galt, ist offen: 1969 war sie vermutlich noch
    nicht ausformuliert, der Text stellt sie als von Anfang an geltend dar.
  - **Was inhaltlich in einem RFC steht** (zweiter Absatz): Adressierung
    und Wegfindung, Verbindungsauf- und -abbau, Dateitransfer, Aufbau einer Nachricht, dazu die Kürzel
    IP, TCP, FTP. Nur FTP ist über die 114 gedeckt; für die übrigen fehlt die jeweilige Nummer. Zu
    prüfen ist außerdem die Zeitlage: TCP und IP sind Mitte der Siebziger bis 1983 und liegen damit
    hinter dem Erzählstand des Abschnitts. Der Satz steht bewusst im Präsens als Ausblick auf die
    ganze Reihe, das muss beim Gegenlesen halten.
  - **Die IETF als heutige Verwalterin** der Reihe, „weder einer Regierung noch einem Konzern"
    gehörend. Gründungsjahr 1986 und die Trägerschaft prüfen; im Text steht bewusst kein Datum, weil
    der Abschnitt sonst aus der Ära fällt.
  - **„Nachlesen kann sie jeder."** Die durchgehende Verfügbarkeit aller Nummern bis RFC 1 belegen.
  - **Nicht im Text und bewusst weggelassen:** der RFC Editor als Amt und Jon Postels Amtszeit bis
    1998 (aus Umfangsgründen gestrichen, siehe Outline), die Scherz-RFCs samt RFC 1149 (Brieftaube,
    1. April 1990; von Oli gestrichen, weil der Platz für den Inhalt der Reihe gebraucht wurde),
    RFC 1855 (gehört als Pointe nach 01.07), IETF, Standard-Stufen, die Umstellung auf TCP/IP.

- **`copyedit-facts` über den AfroNet-Absatz** (01.02, Ende von „FidoNet verband die Inseln", Fassung
  von Oli, eingesetzt 2026-08-07). Zu prüfen sind:
  - **Ken Onwere, 1993, FidoNet-basiert, Nordamerika.** Bestätigt sich in zwei unabhängigen Quellen
    (siehe unten). Ergänzend belegt und noch nicht im Text: Onwere war ein in den USA geborener
    Nigerianer und lebte in San Diego; aufgebaut hat er das Netz mit vier Sysops, **Idette Vaughan**
    (*The BlackNet*), **Alex Hartley** (*Alex's Place*), **Nathaniel Saunders** (*Minority Affairs*)
    und **John Alston** (*VulcanNet*). Technisch war es ein **Echomail-Backbone**, der Konferenzen mit
    afrikanischen und afroamerikanischen Themen von der West- zur Ostküste verteilte, freiwillig
    betrieben und für jeden offen.
  - **„einer der ersten sicheren, unabhängigen digitalen Räume".** Die Erstheit ist ungedeckt, der
    Schutzraum dagegen belegt: Beteiligte beschreiben das AfroNet als den Ort, an dem man „seine
    Leute" fand, und als Verschnaufpause von dem Rassismus, der ihnen im übrigen frühen Netz
    entgegenschlug. Ältere Systeme liefen schon davor, etwa *SpiritDatatree* von William Murrell in
    Boston ab April 1992, was gegen „einer der ersten" spricht, wenn der Maßstab die einzelne Mailbox
    ist, und dafür, wenn der Maßstab der Verbund ist.
  - **Offen:** wie lange das AfroNet lief (keine Quelle nennt ein Ende) und wie groß es war (keine
    Knotenzahl). Der Hopkins-Syllabus sagt abweichend „teils schon in den 1980ern", meint damit aber
    vermutlich die beteiligten Mailboxen, nicht den Verbund.
  - **Stärkste ungenutzte Konkretion:** Das AfroNet verbreitete Berichte aus erster Hand über
    Rassismus bei **AT&T**. Steht bisher nur auf einer Seite (blacksoftware.com) und wäre, wenn es
    sich halten lässt, das Detail, das dem Absatz einen Vorgang statt einer Beschreibung gibt.
  - **Quellen, noch nicht nach `material/quellen/` gesichert:**
    [loriemerson.net](https://loriemerson.net/2021/04/12/excavating-future-histories-of-the-internet-afronet-newsletter-telegraph/) ·
    [blacksoftware.com](https://blacksoftware.com/before-blacks-had-the-internet/) ·
    [AFRONET BBS List, Africa Center (403 beim Abruf)](https://www.africa.upenn.edu/BBS_Internet/afro_bbs.html) ·
    [LARB, Alternative Internets and Their Lost Histories](https://lareviewofbooks.org/article/alternative-internets-and-their-lost-histories/).
    Dazu weiterhin Charlton McIlwain, *Black Software* (siehe [kandidaten.md](kandidaten.md)).
  - **Die Datierung verschiebt die Einordnung.** 1993 liegt neun Jahre hinter dem Fido-Start und
    zeitlich neben den kommerziellen Diensten, nicht neben Jennings. Im Fido-Abschnitt ist das ein
    Sprung nach vorn. Beim Gegenlesen prüfen.
  - **Dopplung mit dem Absatz davor.** Der endet auf „lange bevor das Wort ‚Internet' in Zeitungen
    stand", der AfroNet-Absatz beginnt mit „weit vor dem kommerziellen World Wide Web". Zwei Absätze
    hintereinander mit derselben Pointe.

- **Der Netiquette-Satz in 01.07 kann jetzt kürzer werden.** Dort steht „1995 erschien er als
  RFC 1855, in derselben Dokumentenreihe, in der auch die technischen Protokolle des Netzes stehen".
  Der Relativsatz war nötig, solange die Reihe nirgends eingeführt war. Mit dem neuen H3 in 01.03 ist
  sie es, und der Satz kann zum Rückbezug werden, ohne die Reihe noch einmal zu erklären. Nicht
  automatisch geändert, weil es ein fremdes Kapitel ist.

- **Archie gehört nach 01.10, nicht in 01.03.** Beim Schreiben von „Ein Netz für Rechenzeit"
  ausgebaut: Das Programm der McGill University in Montreal durchsuchte 1990 die Dateinamen der
  anonymen FTP-Archive und gilt als erste Suchmaschine des Netzes. In 01.03 riss es den Abschnitt um
  fünfzehn Jahre auseinander (`copyedit-coherence`, `copyedit-plausibility`). In „Das Erbe wandert ins
  Web" steht es dagegen am richtigen Platz, weil dort ohnehin erzählt wird, was vom alten Netz ins Web
  wanderte. Zu belegen sind Jahr, Ort, Urheber und die Erstheitsbehauptung.

- **Der H3 heißt jetzt „Das ARPANET" und ist von Gemini geschrieben** (eingesetzt von Oli,
  2026-08-06). Damit ist der frühere Einwand erledigt, die Überschrift decke den
  Mailinglisten-Absatz nicht mehr ab. Neu daran und noch offen:
  - **„die erste Mailingliste" steht jetzt in einer Zwischenüberschrift.** Genau diese
    Erstheitsbehauptung (MsgGroup 1975) ist oben als unbelegt vermerkt; in einer Überschrift wiegt
    sie schwerer als im Fließtext.
  - **Die Datierung des anonymen FTP ist weggefallen.** Vorher stand dort „in den Achtzigern wurde
    ein Ort daraus", jetzt schließt der `anonymous`-Absatz direkt an 1971 an, obwohl die Konvention
    eine verbreitete Mailadresse voraussetzt. `copyedit-plausibility` hatte den Sprung schon einmal
    gemeldet.
  - **MIT wird abgekürzt, ohne einmal ausgeschrieben zu sein**, an zwei Stellen.
  - **Die Auszeichnung der Fachbegriffe fehlt:** FTP, E-Mail und Mailingliste stehen ohne Fettung,
    `SF-LOVERS` kursiv statt in Codeschrift. Die übrigen H3 der Datei zeichnen den Erstauftritt
    eines Begriffs durchgehend fett aus (MUD, Avatar, Spam, Bots, IRC).
  - Ein langer Gedankenstrich war drin und ist raus (2026-08-06).

- **Kochs Todesdatum ist strittig.** de.Wikipedia „KGB-Hack" nennt den **30. Mai 1989** für den Fund der
  verbrannten Leiche bei Ohof, de.Wikipedia „Karl Koch (Hacker)" und en.Wikipedia „Karl Koch (hacker)" den **1. Juni 1989**; als Todestag gilt
  der 23. oder 24. Mai. Outline und Text verzichten deshalb aufs Tagesdatum („im Frühsommer 1989"). Wenn ein
  Datum in den Text soll: entscheiden und nach `knowledge/fakten.md`.
- **01.07 auf das Jargon File aus 01.06 umstellen.** Entschieden (Oli, 2026-09-30): 01.06 nennt das
  **Jargon File** beim Namen und führt es kurz ein (1975 von Raphael Finkel in Stanford begonnen, am
  MIT weitergeführt, 1990 von Eric S. Raymond neu herausgegeben), 01.07 greift darauf zurück, statt es
  als neu vorzustellen. **Erst umsetzen, wenn 01.06 aus der geschärften Outline neu geschrieben ist**,
  dann Kohärenz über beide. Vorschlag für den Absatz „Diese Sprache dokumentierte die Szene selbst …"
  in „Netiquette, Zeichen für den Ton und zwei Erfindungen, die blieben":
  - **Streichen, weil es jetzt in 01.06 steht:** Finkel, 1975, das Stanforder Labor, „wanderte ans
    MIT", die Einführung „in einer Datei zu sammeln, dem **Jargon File**" samt Fettung (der
    Erstauftritt ist jetzt in 01.06).
  - **Behalten, weil es neu ist:** was darin stand (Fachwörter, Scherze, Anekdoten), dass immer mehr
    Leute es ergänzten, das Buch von 1983 (_The Hacker's Dictionary_), Zugehörigkeit und Spott als
    Schluss.
  - **Rückbezug über den Inhalt, nicht über das Kapitel** (`rules/form.md`, Abschnitt Zeit): an das
    anknüpfen, was der Leser vom Jargon File schon weiß, das Wörterbuch, in dem die Hacker den Cracker
    vom Hacker trennten. Kein „wie oben", kein „bereits erwähnt".
  - **Jahreszahlen nicht verwirren:** 01.06 nennt die Fassung von 1990, 01.07 das Buch von 1983; 1983
    ist die ältere Form. Der Satz darf nicht so klingen, als sei das Buch aus der Fassung von 1990
    entstanden.
  - Richtung, nicht Wortlaut (Formulierung ist Stufe 2 oder Olis Hand): „Diese Sprache sammelten die
    Hacker im Jargon File, demselben Wörterbuch, in dem sie den Cracker vom Hacker trennten; 1983 war es
    als Buch erschienen, _The Hacker's Dictionary_." Dann weiter mit „Wer die Wörter kannte …".
- **01.06: Outline geschärft (2026-09-30), wartet auf Olis Freigabe, danach Stufe 2 neu.** Die zweite
  Fassung (Stufe 2 nach der Outline vom Vormittag) hat im zweiten Prüflauf die Substanz gehalten
  (`copyedit-plausibility` 3 statt 8 Befunde), die Prosa ist aber ins Stakkato gekippt
  (`copyedit-clarity` 19, `copyedit-language` 19). Oli: Plot schärfen, dann neu schreiben.
  **Erledigt:** Der Faktencheck der zweiten Fassung und die Nachrecherche stehen im Dossier
  (`material/dossier-01.md`, Abschnitt „Hackerkultur", markiert **Berichtigt (2)** und **Neu (2)**).
  Die Outline `material/outline/01.06.md` ist überschrieben: Spannung neu gefasst (§ 202a zog die
  Grenze 1986 an den Daten, das bloße Eindringen sollte straflos bleiben; Sundevil galt Betrug und
  wurde öffentlich zur Hackerjagd; der schwarze Hut kam erst 2001 ins Jargon File, als Wort der
  Sicherheitsleute und erklärt als Cracker), eine Klangvorgabe für Stufe 2 ersetzt „eine Tatsache je
  Satz", je Abschnitt ein Feld „Verbindungen", die Lücken im Vorwissen sind geschlossen, 32 statt 29
  Belegpunkte, rund 1.040 Wörter.
  **Offen:** die Fragen unter „Zu entscheiden", dann Stufe 2 mit der Klangvorgabe im Briefing, dann
  Prüflauf `copyedit-clarity`, `copyedit-language`, `copyedit-plausibility`.
  **Beim nächsten `copyedit-facts` zuerst**, weil neu und nur einfach belegt: dass das Abstreiten der
  Post den Anstoß gab (nur de.Wikipedia nach golem 2014, als Aussage von Holland und Fix); dass die
  Oktober-Warnung einer anderen Lücke galt (nur heise 2024, steht nicht im Text, trägt aber die
  Reihenfolge); „white-hat hacker" spätestens Ende der Neunziger (nur en.Wikipedia nach OED); das
  Internet von 1988 als Netz vor allem der Universitäten und Forschung (Weltwissen); Hübners
  Selbstanzeige (nur en.Wikipedia, nicht im Text). Primär geprüft und ohne Befund: Sterling zu
  Sundevil (Gutenberg), Jargon File 2.1.1, 3.0.0 und 4.3.0 (catb.org), BT-Drs. 16/3656.
- **Prüflauf über den neuen H3 „Malen mit gezählten Farben".** Neu geschrieben, von keinem Agenten
  gesehen: `copyedit-clarity`, `copyedit-language`, `copyedit-plausibility`, danach `copyedit-facts`. Zu belegen sind: sechzehn
  feste Farben beim C64 und die feldweise Farbverwaltung; beim Amiga die begrenzte Palette und der
  Austausch der Farben während des Bildaufbaus; das Erscheinungsjahr von _Deluxe Paint_ (1985,
  Electronic Arts, Amiga) und seine Stellung als Standardwerkzeug. Die genauen Farbzahlen sind auf
  Olis Wunsch bewusst aus dem Text heraus (2026-08-01), sie stehen weiterhin in den
  Bildmetadaten. Ungedeckt und am ehesten strittig: dass Motive
  „oft" aus Buchdeckeln, Comics und Plattencovern übernommen wurden. Der Streit darüber ist mit den
  beiden Bildern von der Party 1993 belegt (siehe unten), die Häufigkeitsaussage „oft" noch nicht.
- **Begriffskollision „Cracker".** Im Netzkunst-H2 heißt Cracker, wer Kopierschutz entfernt; in 01.06, wer in fremde Systeme eindringt. Laut Faktencheck vom 2026-09-29 kein Widerspruch: Das Wort ist in der Kopierszene ab 1980/81 sekundär belegt, das Jargon File beansprucht mit „coined c. 1985" nur die Bedeutung Sicherheitsbrecher. Die Outline vom 2026-09-30 entscheidet sich für einen Halbsatz im H3 „Cracker, White Hat, Black Hat": neu war die Bedeutung, nicht das Wort; kein Datum für die Kopierszene, keine Herkunftsbehauptung. Beim Prüflauf der neuen Fassung ansehen, ob der Halbsatz trägt, dann streichen. Offen bleibt die Einzelquelle für „ab 1980/81", der Faktencheck hat sie nicht festgehalten.
- **Kandidaten, die im Hackerkultur-H2 fehlen** und Recherche brauchen, falls der Abschnitt noch
  wachsen soll: die 414s und der Kongress-Auftritt von 1983, der Film _WarGames_ als Auslöser der
  öffentlichen Wahrnehmung, Legion of Doom gegen Masters of Deception, die 2600-Treffen als
  Offline-Struktur der Szene.
- **Hackerkultur in den späteren Kapiteln wieder aufgreifen.** Nach dem Start des öffentlichen
  Internets hat sich das Thema stark weiterentwickelt (Crypto Wars und Hacktivismus stehen schon in
  K02, aber ohne Bogen zur Szene aus K01; später Anonymous, Leaks, Bug-Bounty-Ökonomie, staatliche
  Angreifer). Gehört als Faden durchgezogen, nicht als Wiederholung. Die EFF kommt in K01 nicht vor:
  01.06 endet mit den Razzien vom Mai 1990, **K02 führt die EFF selbst ein** (Oli, 2026-09-29), siehe
  [issues-02.md](issues-02.md). → auch in [issues.md](issues.md)
- **Die „Release-Szene" wird vorausgesetzt, aber nie eingeführt.** Der Abschnitt „Bilder aus
  Buchstaben" nennt „die Textlogos in den Begleitdateien der späteren Release-Szene"; der Begriff
  fällt weder im Cracker-Absatz noch in K02 oder K03.
- **Zwei Abschnitte enden mit derselben Figur:** die Form überlebt ihren Anlass, dazu ein
  Archiv-Verweis (`pouet.net`/`demozoo.org` gegen `16colo.rs`). Einer von beiden braucht einen
  anderen Schluss.
- **Zweiter Prüflauf** über „Cracker und die Demoszene", den Tracker-Abschnitt und den
  Buchstaben-Abschnitt sowie über die neuen Nahtstellen des Umbaus: den Rahmenabsatz von „Das
  Usenet", den Rahmensatz von „Die Anfänge der Netzkunst", den neuen Einstieg von „IRC" und den
  Zitier-Absatz, der jetzt „Trolle, Flamewars" eröffnet.
- **Die ARPANET-Karte 1974 ist eine Rekonstruktion, kein Dokument.** `assets/01/arpanet_1974.png`
  geht auf [File:Arpanet 1974.svg](https://commons.wikimedia.org/wiki/File:Arpanet_1974.svg)
  zurück, gezeichnet von einem Commons-Nutzer „aus Notizen und Erinnerungen von 1974". Public
  Domain, also rechtlich unproblematisch, und Britannica benutzt dieselbe Datei. Aber die
  Knotenliste ist gegen nichts prüfbar. Wenn die Karte im Buch Belegcharakter bekommen soll, gegen
  eine echte BBN-Karte tauschen: [ARPA Network, Logical Map, September
  1973](https://commons.wikimedia.org/wiki/File:ARPA_Network,_Logical_Map,_September_1973.jpg) oder
  [Arpanet logical map, march
  1977](https://commons.wikimedia.org/wiki/File:Arpanet_logical_map,_march_1977.png), beide
  ebenfalls gemeinfrei. Die deutsche Legende steckt in `assets/01/arpanet_1974.svg`, dort ändern
  und mit `rsvg-convert -w 3272` neu rendern.
- **Rechte am Text der Werbemail von 1978 sind ungeklärt.** `assets/01/spam_1978.png` ist unser
  eigener Satz, der Wortlaut stammt aus der Abschrift von Brad Templeton
  ([spamreact.html](https://www.templetons.com/brad/spamreact.html)); ein Scan des Originals
  existiert nirgends. Eingetragen ist „Bildzitat § 51 UrhG" nach der Grundsatzentscheidung vom
  2026-07-30. Falls das nicht tragen soll: entweder auf Kopfzeilen und Einladungsblock kürzen oder
  gegen ein Foto des beworbenen Rechners tauschen ([DECSYSTEM-2020 KS-10, Jason Scott, CC BY
  2.0](https://commons.wikimedia.org/wiki/File:DECSYSTEM-2020_KS-10_(1979).jpg)). Ein frei
  lizenziertes Foto von Gary Thuerk gibt es nicht, weder auf Commons noch über Openverse.
- **Die Kürzungsmarke im Faksimile ist Deutsch mitten im englischen Ausdruck.** Bewusst so, damit
  niemand sie für Teil des Originals hält. Wenn das im Satzbild stört: Wortlaut in
  `assets/01/spam_1978.svg` ändern und mit `rsvg-convert -w 2400` neu rendern.
