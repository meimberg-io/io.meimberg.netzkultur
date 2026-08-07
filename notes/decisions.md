---
rolle: stand
liest: claude
wann: nach einem Prüflauf, als Filter vor der Übergabe an Oli
modus: abfrage
agentensichtbar: nein
---

# Abgelehnte Befunde

Stellen, an denen eine Prüfung etwas gemeldet hat und Oli entschieden hat, dass es so bleibt.

**Diese Datei wird nur nach einem Prüflauf gelesen, nie beim Schreiben.** Sie ist ein Filter: Claude
gleicht jeden Befund hier ab und legt Oli nur vor, was noch offen ist. Wer sie beim Formulieren im
Kopf hat, schreibt um vierzehn alte Einwände herum, statt zur Sache hin. Die Prüf-Agenten sehen sie
ohnehin nicht, sonst wird aus dem frischen Blick eine Abhakliste.

Abgeglichen wird über die **Stelle**, nicht über die Formulierung des Befunds: Derselbe Fall kommt
beim nächsten Lauf oft anders benannt.

**Kein Logbuch.** Hier steht nur, was ein Lektorat am **aktuellen** Text wieder bemängeln würde. Was
nicht mehr im Text ist, wird gelöscht.

Was hier **nicht** hingehört:

- **Konventionen der Reihe** → [konventionen.md](konventionen.md), die werden beim Schreiben gelesen.
- **Aufgaben und offene Punkte** → [`<NN>_issues.md`](01_issues.md) pro Kapitel, [issues.md](issues.md)
  für Werkweites.
- **Bestätigte Sachverhalte** → [memory/fakten.md](../memory/fakten.md). Dort liegen auch die beiden
  entschiedenen Quellenkonflikte, die Btx-Endsumme und das AOL-Gateway-Datum.
- **Tonalität** → [memory/ton.md](../memory/ton.md).

---

| Stelle | Befund | Warum abgelehnt | Datum |
|---|---|---|---|
| Second Life: „eine Plattform, die kein Spiel sein wollte" gegen „im Spiel als Reporter" | Widerspruch zur eigenen Abgrenzung | Second Life war tatsächlich etwas dazwischen, die Unschärfe ist sachlich richtig | 2026-07-30 |
| „Eine App konnte nun eine private Couch zur Hotelsuite erklären" und die spätere Airbnb/Uber-Passage | Dopplung, zweimal dasselbe Phänomen | Nicht störend | 2026-07-30 |
| K1, Überschrift „Der Sysop war König in seinem Wohnzimmer" | Kündigt an, was erst im dritten Absatz kommt | Der Abschnitt läuft auf diese Szene zu; eine Überschrift darf das Ziel benennen statt den Einstieg | 2026-07-31 |
| K1, „Die Cyberpunk-Utopie" als eigene H2 | Kleinster Gliederungspunkt, Gewicht passt nicht zu den anderen H2 | Ohne Kapitelnummerierung wiegt ein kleineres Hauptkapitel nicht schwer | 2026-07-31 |
| K1, Sternchen in `comp.*` | Nie erklärt, liest sich im deutschen Satz zuerst als Fußnotenmarke | Wird nicht erklärt | 2026-07-31 |
| K1, Einwahlgeräusch an drei Stellen | Redundanz, die dritte Stelle verliert ihre Pointe | So belassen | 2026-07-31 |
| K1, Hausrecht des Sysops an drei Stellen | Redundanz über Distanz | So belassen | 2026-07-31 |
| K1, Avatar („was Jahre später einen Namen bekam") | Erstheit ohne Datum, anders als sonst im Kapitel | So belassen | 2026-07-31 |
| K1, „Cracker und die Demoszene" als ein Abschnitt | Behandelt zwei Gegenstände, die Demoszene bräuchte ein eigenes H3 | Cracken, Cracktro und Demoszene sind eine Entwicklungslinie und bleiben zusammen | 2026-07-31 |
| K1 und K2, AOL und IRC je zweimal aufgelöst | Über die Kapitelgrenze zweimal als neu eingeführt | In Ordnung | 2026-07-31 |
| K1, „Das Usenet" als eigene H2 neben „Die Netze der Universitäten" | Usenet gehört technisch in die Uni-Welt, die eigene Ebene doppelt die Gliederung | Es lief über gewöhnliche Telefonleitungen und gehört in beide Welten. Als Unterpunkt wog es dreimal so viel wie seine Nachbar-H3 | 2026-07-31 |
| K1, Reihenfolge der H2: Netzkunst und Hackerkultur stehen hinter den Netz-Abschnitten | Unterbricht die Chronologie, die Kunst wächst aus dem Wohnzimmer und müsste dort stehen | Der Kapitelbau nimmt erst die Infrastruktur (Wohnzimmer, Universitäten, Usenet), dann die Szenen (Kunst, Hacker), dann das Gemeinsame (Umgang, Utopie). Innerhalb dieser Folge gilt kein Zeitstrahl | 2026-07-31 |
| K1, Morris-Wurm unter „Die Hackerkultur" | Morris war kein Mitglied der Szene, der Wurm war ein Messversuch | Der H2 handelt vom Vertrauensverlust, der in die Kriminalisierung führt; der Wurm ist dort die Zäsur, nicht eine Szene-Tat | 2026-07-31 |
| K1, § 202a und Operation Sundevil in einem H3 | Springt zwischen Deutschland 1986 und den USA 1990 | Der Abschnitt zeigt dieselbe Bewegung auf beiden Seiten, deshalb steht sie zusammen | 2026-07-31 |
