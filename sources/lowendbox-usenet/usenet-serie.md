# LowEndBox — USENET-Serie von raindog308 (2022)

> Snapshot der Teile 1 und 2 von <https://lowendbox.com/tag/usenet/>, gezogen am 2026-07-31 aus dem
> gerenderten DOM. Originaltexte auf Englisch, bereinigt um Navigation, Autorenbiografie und
> Kommentarformular. Read-only Rohstoff.
>
> LowEndBox ist ein Blog über billiges VPS-Hosting; der Autor schreibt unter dem Handle
> **raindog308** und erzählt als Zeitzeuge, nicht als Historiker. **Keine Belegquelle**, aber eine
> dichte Sammlung von Szene-Erinnerungen mit belegbaren Anknüpfungspunkten. Ein Namensfehler ist
> bereits aufgefallen (siehe Anmerkung am Ende).

Die Serie hat drei Teile. Teil 3 („Let's Give SABnzbd and Vampira a Spin!", 7.5.2022,
<https://lowendbox.com/blog/usenet-part-3-lets-give-sabnzbd-and-vampira-a-spin/>) ist eine
Schritt-für-Schritt-Anleitung, wie man das Usenet heute mit SABnzbd nutzt, und hier nicht
mitgeschnitten. Auf der Tag-Seite steht außerdem eine Werbung für den Dienst TorBox (2024), die
Usenet-Zugang, Torrents und Seeding als ein Paket verkauft.

---

## Teil 1: „Wasn't USENET Part of AOL or Something Back in the Dial-Up Days?" (25. April 2022)

In this article we begin a series on USENET, a "worldwide distributed discussion system available on
computers," as Wikipedia puts it. USENET was begun in 1980 and has changed dramatically over its
lifetime. We'll explain what USENET is and how you can use it. We'll also talk with Frugal Usenet,
one of our community advertisers. If you've never known much about USENET, you're in for an education
about a fascinating technology that still underlies hundreds of TBs a day of traffic.

Are you interested in having a discussion with people from around the world centered on a specific
topic? What platform would you use in, say, 1980? Certainly not Discord or a vBulletin forum. In
fact, the web doesn't even exist yet. TCP/IP itself is only a few years old.

My friend, you would use USENET. USENET is a news service, though for "news" don't think "as put out
by a journalist" but rather "posts from users". USENET runs on the NNTP protocol, and it's probably
easier if I just describe the experience.

Individual sites or organizations (or really anyone) run a news server. They decide which newsgroups
(or just "groups") to carry, and the groups are outlined in various hierarchies with top-level names
like "comp" (computer-related), "rec" (recreation), "soc" (society/social), etc. For example, the
group devoted to the C programming language is comp.lang.c.

The news server is set to a given retention and posts expire. So if you login in June and your site
has a 60-day retention on its news server, you'll see things back to April but not earlier.
Retentions are configurable down to the group level.

When you post something, it's similar to the old FIDOnet or bulletin board days. What you post is
shared with others who subscribe to whatever group you're posting to. This is by no means instant! In
the 1980s-1990s, some hosts would only exchange news once a day. Of course, modern USENET servers
exchange very quickly.

Note that the medium is text. While binaries are exchanged, they're uuencoded — similar to how you'd
mail someone a file. In fact, people share code using .shar files, which were text files that were
valid shell scripts. You'd download, set to executable, execute, and it would create and populate all
the files of its archive. In essence, this acted like a tar file, but .shar files were easy to post
on newsgroups or in email.

Yes, I know — I wouldn't grab a random multi-thousand-line shell script from a random stranger and
execute it, but it was a simpler time.

### USENET at Its Peak

I was a heavy USENET user throughout the 90s, using trn or tin on a SunOS or Linux machine. Our
university carried all groups and I remember when the massive 9GB hard drives arrived, mainly due to
USENET growth.

I conducted and bid on auctions in rec.games.frp.marketplace, which is again a sign of a gentler
time. People mailed checks or money orders and strangers sent books. I voted yes or no on new
newsgroups. I asked code questions in comp.lang.c, and remember having discussions on at least a
dozen other groups devoted to various interests at the time.

Everything you did was tied to your name and email, though these were not impossible to forge. Still,
I remember people posting with signatures with their email routinely and often phone numbers as well.

Things got unwieldy at times because of "cross-posts". Someone with too much passion or a grudge
would decide they wanted everyone to hear about it and so they'd post the same message to every
newsgroup. There was a team — I want to say a midwestern university but I don't remember — that came
up with some heuristics to analyze the post flow and issue cancels for people who cross-posted. It
was all very much reminiscent — or is that preminiscent? — of later email spam wars and filtering.

Naturally, you can't go anywhere without humans turning it into porn, so there were newsgroups that
distributed erotic fiction. alt.sex.stories was a famous one. A kid at my school wrote a long
sadistic murder fantasy piece about a fellow student, who he referred to by name. As I recall, the
school — and every other institution who carried that group — was grappling with these sorts of free
speech / online code of conduct / acceptable use issues for the first time.

Some groups evolved into established communities with bodies of reference materials. For example,
many groups composed FAQs (an early use of the term online) that were then auto-posted once a month.
Some of these — such as the one from comp.lang.c — later were published as books and are invaluable
resources.

Before the web existed, the main options for sharing things with the public were via anonymous FTP
server or via USENET. For most users, it was far easier to get a USENET account than to setup an FTP
server (this was a pre-VPS era!) or get a directory on an existing one. Most ISPs of the period
provisioned USENET access as part of their account packages, and that allowed you to share your
thoughts to a huge audience.

### The Third Era

USENET went through two eras — and potentially three. […] I'd put the timestamp [for the end of the
first era] sometime in the mid-2000s.

The second era has been dominated by use of USENET to distribute binaries. Although it's a grossly
inefficient platform (you have to encode to text and then decode), there are hundreds of terabytes
per day of USENET traffic. Is most of this bandwidth devoted to distributing public domain books,
Linux distribution ISOs, and open source repositories? Yes, I'm sure that must be the case.

Remember, nothing is permanent on USENET. It's all "in motion" all the time. How fast can someone
notice content, file a DMCA, have it acknowledged…the traffic gone long before the paperwork arrives.
That's not to say that all of USENET's traffic is this way. It depends how you count it. By megabyte?
Yes, 99.99% binaries. By user? There are still many communities whose home is on USENET.

So is USENET just hanging around as a weird legacy protocol for a few diehards and pirates? Or is
there a third era of USENET on the horizon? One that goes back to its discussion roots?

---

## Teil 2: „Spambots, Scientology Wars, and the Internet's First Deity" (29. April 2022)

Would you like some more USENET lore? OK, let's talk about Menudo (note the capital letter), green
card lawyers, kooks and spambots, war with Scientology, Joel Furr T-shirts, eternal September, how
Google ruined the party …and the Internet's first deity. And that's just the first 30 years.

### Die Abstimmung über neue Newsgroups

Last time we talked about a newsgroup. What if you want a new newsgroup? There is a complex and
probably now irrelevant process for voting. […] back in the day, you'd campaign in different groups
for your group, discuss, etc. and then there would be a vote — yes, a vote on the Internet where
anyone with an email could say yea or nay. Talk about a simpler era.

Yours truly can proudly say he voted against rec.music.menudo (what, you've never heard of the music
group Menudo? Neither has anyone else). Indeed, I recall some people observing that because a
nomination had to pass by a certain percentage, a no vote was much more powerful than a yes vote. So
there was a movement of people who felt too many groups were getting nominated and resolved to vote
no en bloc against all new groups, thus making it difficult for new groups to pass.

Talk about fighting over small stakes. As a couple quotes summarize:

> "Academic politics is the most vicious and bitter form of politics, because the stakes are so low."
> — Wallace Sayre
>
> "USENET: welcome to the next level." — anonymous, USENET

Eventually the alt hierarchy was founded where anyone could create a group, with the predictable
chaos, cancel wars, etc.

### Spam und Kooks

Now let's talk about spam. The term spam may have originated on USENET.

Two "green card lawyers" had the idea to post an ad in every single newsgroup, which was
unprecedented and extremely rude. This was followed by numerous others — the subject "Make Money
Fast" itself became a meme. A dedicated team of engineers came up with a way to target "cancel"
messages that would filter this spam. This problem is ancient.

There are a raft of USENET kooks that have been documented. These people posted endlessly and
intensely. […] Why do I say looney tunes? The whole gamut: UFOs, time cube stuff, conspiracy
theories, genocide denial, etc. My favorite was UFOlogist Robert E. McElwaine who wrote long screeds
and signed every one "UN-altered REPRODUCTION and DISSEMINATION of this IMPORTANT Information is
ENCOURAGED, ESPECIALLY to COMPUTER BULLETIN BOARDS."

**Serdar Argic** was another famous one and may be credited with the first spambot. Argic was a nut
who had some revisionist theories about the Armenian genocide. He wrote a bot that scanned all of
usenet for the mention of Turkey or Armenia. Any post containing the string "turkey" or "armenia"
would be auto-replied to with one of many randomly-chosen screeds. This was somewhat hilarious when
someone's discussion about their Thanksgiving recipes was interrupted by a foam-mouthed screecher
ranting about genocide.

This lead to a particular genius, James "Kibo" Perry [sic — recte Parry], realizing that one could,
in essence, summon Serdar's bot into any thread simply by including the word "turkey". Perry turned
this noxious behavior on its head by instead creating his own bot that notified him when anyone used
the word "kibo". He would then personally visit the thread and comment with a humorous one-liner. In
effect, he became the Internet's first deity, who could be summoned and would omnisciently reply. A
"religion" was formed around him and celebrated on — where else? — alt.religion.kibology.

Perry kept this going for a very long time. Quoting Wikipedia:

> "In 2006, Parry estimated that he had posted 'an average of 20 articles a week to
> alt.religion.kibology during the past 15 years, probably about 500 words of original content per
> article, that's… seven point eight mmmmillion [sic] words. Equivalent to about 100 books.'"

### The Original Scientology vs. the Internet Battlefield

Scientology's first war against the Internet was fought in alt.religion.scientology, an early
critical group that came under sustained assault by the church. In 1994, the "OT Levels" (with the
infamous "Xenu" material) was leaked on a.r.s and the Church went crazy. The Church started first
with legal threats and then with technical assaults, which naturally only caused the group to surge
in popularity.

The famous Penet anonymous remailer (anon.penet.fi, a domain I still remember nearly 30 years later)
was shut down due to the a.r.s wars, and there are individuals still paying settlements to the Church
of Scientology years later. For example, **Grady Ward** was sued, alleging he had anonymously posted
Church secrets to a.r.s. He was bombarded with over 1,000 legal filings and eventually settled with
the Church. He will pay $200 a month for the rest of his life. Crazy times!

### Private Groups?

Were there any private USENET groups? No — this was impossible. Well, almost. One could post
encrypted messages […]. PGP emerged in this era and that made everything feasible. But really,
private discussion groups of the era were done via private email — either mailservers or just a group
of people CCing each other.

I don't mean the way you'd CC your coworkers or people you know. There was a lively culture in email
groups which one could apply to and perhaps join. If you were accepted, you got a list of everyone's
email, and were expected to "blind carbon copy" all of them. "Blind to <group name>" was a common
expression.

### Google, Delphi, and Universities Ruined It All

[…] today is really the second era of USENET. What I've described above is the first era, which I'd
place at 1980 to the early 2000s.

The first era itself had a couple sub-phases. The first was a small, somewhat intimate community
because there weren't that many involved. It was mostly universities, research institutions, and
large companies. These users were generally sophisticated because they were mostly computer
professionals or related "super users".

> I bought this shirt circa 1994, which expressed the general sentiment of netizens regarding the
> influx of new users. These were sold by **Joel Furr**. *(Bildunterschrift im Original)*

Every September, a flood of new users joined — university students who'd just arrived at school and
been provisioned accounts. They generally barged in, breached netiquette, were swiftly corrected, and
then integrated into the community. People groaned about "September coming" but it was not a major
event.

However, once ISPs like AOL and Delphi and others opened up USENET to their users (circa 1993-94),
there were a flood of users and they began coming in droves, regardless of the time of year. This was
referred to as Eternal September and some feel it "blew up" the original USENET culture.

### End of an Era

But there were other reasons.

First, for people who were truly interested in focused conversations, the web was far easier to use.
The web also offered permanence — well, as much as anything on the web is, but compared to ephemeral
postings. It also moved the cost from everyone to those who wanted to provide the content. Finally,
you could do so much more with it: images, fonts, layouts, hyperlinks, and soon multimedia, etc. And
today we have social media. USENET was the social media of its day, but it's two full orders of
magnitude back in technology.

Second, pipes got bigger. People started wanting to share binary files. When 9600 baud modems
dominated the landscape, downloading 4MB of content took an hour. The text-only format of USENET was
a blessing when bandwidth was precious but a limitation once it became abundant.

Third, binaries took over. […] as the "casual readers" moved to different platforms, USENET became
dominated by people exchanging media. Eventually different ISPs began to wonder if they were really
providing something people wanted and began to shut down USENET, lather rinse repeat down the drain.

Finally, **Google screwed everyone**. In 1995 a very cool company called **DejaNews** began archiving
all USENET posts. I think they filtered binaries as I recall but otherwise it was a complete feed.
They published this archive as a web site and you could also use it as a newsreader, posting
articles, subscribing to groups, etc. There was a premium feature as I recall as well. It was
awesome. And it enabled nearly anyone who didn't want the hassle of running a USENET server to say
"we're closing ours, but look, you can go to DejaNews and it's awesome".

Speaking of awesome, the name "DejaNews" is one of my favorite company names ever. Perfectly fits
what it offered in a very elegant pun.

And then, Google bought it in 2001. Shortly thereafter, features began shutting down, and it was
subsumed into Google Groups. Google acted as if USENET was dead technology and everyone would
obviously want to use Google Groups instead. However, no one really wanted to use Google Groups.
Using the USENET interface was made a hassle and since a lot of ISPs were no longer providing USENET,
this was a pretty big body blow to the technology.

---

## Anmerkung zur Zuverlässigkeit

Der Text nennt den Kibo-Erfinder durchgehend **„James Perry"**, während das im selben Absatz zitierte
Wikipedia-Zitat **„Parry"** schreibt. Richtig ist James Parry. Ebenso schwankt der Name des
UFO-Kooks: im Fließtext „Robert E. McElwaine", in den Schlagworten des Artikels „thomas e. mcelwaine".
Beides zeigt den Charakter der Quelle: Erinnerung, nicht Recherche. Namen, Zahlen und Daten daraus
gehören vor jeder Verwendung eigenständig belegt.
