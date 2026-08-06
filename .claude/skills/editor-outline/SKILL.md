---
name: editor-outline
description: Erstellt das Inhalts-Skelett eines Abschnitts, bevor Prosa entsteht - reine Fakten mit Kontext, nach festem Schema. Nutzen, wenn ein Abschnitt neu geschrieben oder inhaltlich neu aufgesetzt wird. Liefert keinen Fließtext.
---

# Outline

Erste Stufe des Schreibens. Ergebnis ist eine Liste von Fakten und der rote Faden, nichts
Formuliertes.

## Vorbereitung

- `memory/fakten.md` nach dem Thema durchsuchen. Was dort steht, gilt gegen Modellwissen.
- Die Nachbarabschnitte in `chapters/` lesen: was sie schon erzählen, worauf der Abschnitt hinauslaufen
  muss, welche Begriffe dort bereits eine Bedeutung haben.
- Umfang festlegen. Ein Abschnitt neben vier gleichrangigen trägt 400 bis 500 Wörter. Also auswählen,
  nicht alles aufnehmen, was zum Thema existiert.

## Regeln

1. **Keine Rhetorik.** Keine Adjektive wie „spektakulär", „überraschend", „bahnbrechend".
2. **Kontext steht im Fakt selbst.** Nicht „ARPA", sondern „ARPA = Forschungsagentur des
   US-Verteidigungsministeriums". Nicht „Ostküste", sondern „US-Ostküste".
3. **Chronologisch oder als Ursache-Wirkung-Kette sortieren.**
4. **Belegstatus mitschreiben.** Recherchiertes mit Quelle in Klammern, Ergänzungen aus Modellwissen
   mit `(ungeprüft)`. Was ungeprüft bleibt, kommt in `notes/<NN>_issues.md`.

## Schema

```
### 1. Ausgangslage & Problem
* [Fakt/Kontext]

### 2. Die Auslöser & Handlungen (Was passiert ist)
* [Fakt/Kontext]
* [Wichtige Namen, Daten, Fachbegriffe inklusive Erklärung]

### 3. Konflikt & Wendepunkt (Unerwartete Eigendynamik)
* [Fakt/Kontext]

### 4. Ergebnisse & Konsequenzen
* [Fakt/Kontext]
```

Liegt zu einem Abschnitt nichts vor, steht dort `[Keine Angaben]`.

## Übergabe

Die Outline geht an Oli, bevor formuliert wird. Sie ist in einer Minute geprüft; ein falscher Aufbau
kostet sonst einen ganzen Text. Danach `editor-write`.
