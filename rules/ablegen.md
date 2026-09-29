---
role: rule
readers: claude
when: vor jeder Antwort im Chat
mode: full
agent-visible: no
---

# Ablegen

Vor der Antwort im Chat, ohne Aufforderung:

| Was | Wohin |
|---|---|
| Bestätigter Sachverhalt gegen das Modellwissen | `knowledge/fakten.md`, mit Datum |
| Befund, den Oli abgelehnt hat | `state/decisions.md`, mit Datum |
| Offener Punkt zu einem bestimmten Kapitel | `state/issues-<NN>.md` |
| Offener Punkt über mehrere Kapitel hinweg | `state/issues.md` |
| Stoff, der noch keinen Platz hat | `material/kandidaten.md` |

Behobene Punkte streichen, nicht abhaken. Keine dieser Dateien ist ein Logbuch.
