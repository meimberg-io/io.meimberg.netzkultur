---
rolle: regel
liest: editor-images
wann: vor der Bildsuche
modus: ganz
agentensichtbar: ja
---

# Bilder: Metadaten, Rechte, Fallstricke

Bilder werden mit `scripts/bild-einziehen.py` eingezogen. Das Skript lädt die Datei und schreibt
die Metadaten, die Lightroom Classic im Panel anzeigt. Welches Feld auf welches XMP-Tag geht,
steht im Docstring des Skripts. Hier steht, was dort **nicht** steht: die Entscheidungen und die
Fallen, die beim Aufbau Zeit gekostet haben.

## Rechte

**Ohne Lizenzzusage gilt Bildzitat.** Bei Quellen, die keine Lizenz einräumen (Demozoo,
Screenshots geschützter Werke), hat Oli am 2026-07-30 entschieden: Bild nehmen, `Bildzitat
§ 51 UrhG` als Rechtenutzung eintragen, Quelle und Rechteinhaber immer mitschreiben. Auf Zuruf
des Rechteinhabers kommt das Bild runter.

Die Abwägung dahinter ist getroffen und muss nicht erneut aufgemacht werden: bei einer Demogruppe
von 1993, die als Entität kaum noch existiert, ist das Risiko gering, und eine große kommerzielle
Verwertung findet nicht statt. Das Risiko trägt Oli bewusst.

**Das Flag `--zitat` setzt diesen Wortlaut, und es wird nicht automatisch gesetzt.** Ohne das Flag
schreibt das Skript den Marker `Rechte ungeklärt - vor Veröffentlichung klären` in die Datei. Das
ist Absicht: das Bildzitat soll eine bewusste Entscheidung pro Lauf bleiben und kein Default, in
den man hineinrutscht. Wer ein Bild ohne gefundene Lizenz einzieht, lässt das Flag weg und legt
die Entscheidung Oli vor.

Keine Lizenz erfinden, wenn die Quelle keine nennt. Herkunft nie weglassen.

## Drei Fallen

**`xmp:Label` ist nicht die Bildunterschrift.** Es ist Lightrooms Farb-Label („Beschriftung
festlegen" → Rot/Gelb/…). Die Unterschrift gehört nach `dc:description` plus
`IPTC:Caption-Abstract`, der Alt-Text nach `iptcCore:AltTextAccessibility`. Im Panel erscheint
`dc:description` als „Bildunterschrift", sichtbar erst nach „Anpassen…" → „IPTC-Inhalt".

**`IPTC:Source` und `IPTC:Credit` schneiden nach 32 Zeichen ab, still.** Der alte IIM-Block kappt
jede Quell-URL ohne Fehlermeldung. Deshalb ausschließlich die XMP-Varianten
`XMP-photoshop:Source` und `XMP-photoshop:Credit` schreiben. `XMP-photoshop:URL` gibt es nicht;
`Photoshop:URL` liegt im IRB und funktioniert nur in JPEG und TIFF, nicht in PNG.

**Lightrooms Katalog gewinnt gegen die Datei.** Wird eine Datei nachträglich von außen geändert,
muss in Lightroom „Metadaten aus Datei importieren" laufen. Sonst überschreibt Lightroom die
Änderung beim nächsten eigenen Schreibvorgang wieder.

## Was recherchiert wird und was nicht

Titel, Beschreibung und Alt-Text sind **immer redaktionell**, nie aus der Quelle übernommen.
Urheber, Lizenz und Lizenz-URL sind **immer recherchiert**, nie geschätzt. Wikimedia Commons
liefert beides maschinenlesbar über die API, Demozoo liefert Gruppe, Titel und Datum, aber keine
Lizenz.

Für die Suche nach Bildern samt Lizenzstatus gibt es den Agenten `editor-images`.
