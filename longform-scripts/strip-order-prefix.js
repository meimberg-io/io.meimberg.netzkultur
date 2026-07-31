/*
 * Longform-Compile-Step: Ordnungspräfix aus Überschriften entfernen.
 *
 * Hintergrund: Die Szenendateien tragen ein Ordnungspräfix im Dateinamen
 * ("1.3 - Das Usenet.md"), damit sie im Dateisystem sortiert sind und auch
 * ausserhalb von Obsidian navigierbar bleiben. Weil "Prepend Title" den
 * Dateinamen zur Überschrift macht, landet das Präfix sonst im Manuskript.
 * Dieser Step schneidet es dort wieder ab.
 *
 * Reihenfolge im Workflow: MUSS nach "Prepend Title" laufen.
 *
 * Zusätzlich prüft der Step, ob die Präfixe in der Reihenfolge des Projekts
 * aufsteigend sind, und meldet Abweichungen. Das ist der Preis der Redundanz:
 * die Nummern im Dateinamen sind eine Behauptung, die Szenenreihenfolge in
 * Index.md ist die Wahrheit. Der Step sagt Bescheid, wenn beides auseinanderfaellt.
 */

const DEFAULT_PATTERN = "^(#{1,6}\\s+)\\d+(?:\\.\\d+)*\\s*[-–—]\\s*";

/** Liest das fuehrende Nummernpraefix eines Namens als Tupel, z. B. "1.3 - X" -> [1, 3]. */
function orderTuple(name) {
  const match = /^(\d+(?:\.\d+)*)\s*[-–—]\s*/.exec(name);
  return match ? match[1].split(".").map(Number) : null;
}

/** Vergleicht zwei Tupel elementweise; das kuerzere sortiert zuerst ([1] < [1,1] < [2]). */
function compareTuples(a, b) {
  const length = Math.max(a.length, b.length);
  for (let i = 0; i < length; i++) {
    const left = a[i] === undefined ? -1 : a[i];
    const right = b[i] === undefined ? -1 : b[i];
    if (left !== right) return left - right;
  }
  return 0;
}

/** Meldet als Obsidian-Notice, faellt auf die Konsole zurueck. */
function report(message) {
  console.warn(`[Longform] ${message}`);
  try {
    const { Notice } = require("obsidian");
    new Notice(message, 10000);
  } catch (e) {
    // Notice nicht verfuegbar, Konsolenausgabe genuegt.
  }
}

/** Prueft, ob die Praefixe in Projektreihenfolge aufsteigen. */
function checkOrder(scenes) {
  const numbered = [];
  const unnumbered = [];

  for (const scene of scenes) {
    const tuple = orderTuple(scene.name);
    if (tuple) numbered.push({ name: scene.name, tuple });
    else unnumbered.push(scene.name);
  }

  const problems = [];
  for (let i = 1; i < numbered.length; i++) {
    if (compareTuples(numbered[i - 1].tuple, numbered[i].tuple) >= 0) {
      problems.push(`"${numbered[i - 1].name}" vor "${numbered[i].name}"`);
    }
  }

  if (problems.length > 0) {
    report(`Ordnungspräfixe nicht aufsteigend: ${problems.join("; ")}`);
  }
  if (unnumbered.length > 0) {
    report(`Ohne Ordnungspräfix: ${unnumbered.join("; ")}`);
  }
}

module.exports = {
  description: {
    name: "Ordnungspräfix entfernen",
    description:
      'Entfernt ein Nummernpräfix wie "1.3 - " aus den Überschriften. Muss nach "Prepend Title" laufen.',
    availableKinds: ["Scene", "Manuscript"],
    options: [
      {
        id: "pattern",
        name: "Regulärer Ausdruck",
        description:
          "Wird zeilenweise angewandt; der Treffer wird durch die erste Gruppe ersetzt. Standard trifft Überschriften mit Nummernpräfix.",
        type: "Text",
        default: DEFAULT_PATTERN,
      },
      {
        id: "check-order",
        name: "Reihenfolge prüfen",
        description:
          "Meldet, wenn die Nummern nicht aufsteigen oder eine Szene keine Nummer hat. Nur bei Kind 'Scene'.",
        type: "Boolean",
        default: true,
      },
    ],
  },

  compile: (input, context) => {
    const pattern = String(context.optionValues["pattern"] || DEFAULT_PATTERN);

    let expression;
    try {
      expression = new RegExp(pattern, "gm");
    } catch (e) {
      throw new Error(`Ungültiger regulärer Ausdruck "${pattern}": ${e.message}`);
    }

    const strip = (contents) =>
      contents.replace(expression, (...groups) => groups[1] || "");

    if (context.kind === "Manuscript") {
      return Object.assign({}, input, { contents: strip(input.contents) });
    }

    if (context.optionValues["check-order"] === true) {
      checkOrder(input);
    }

    return input.map((scene) => Object.assign({}, scene, { contents: strip(scene.contents) }));
  },
};
