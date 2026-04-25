#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const { performance } = require("perf_hooks");

const ROOT_DIR = path.resolve(__dirname, "..");
const INDEX_HTML = path.join(ROOT_DIR, "index.html");

const DEFAULT_OPTIONS = {
  generations: 4,
  populationSize: 16,
  matchesPerGeneration: 16,
  roundsPerMatch: 6,
  seatRotations: 1,
  finalMatches: 24,
  finalSeatRotations: 2,
  leaderboardSize: 8,
  drawSampleMax: 10,
};

function parseValue(value) {
  if (value === "true") return true;
  if (value === "false") return false;
  if (value !== "" && !Number.isNaN(Number(value))) return Number(value);
  return value;
}

function parseArgs(argv) {
  const options = { ...DEFAULT_OPTIONS };
  let outPath = null;
  let jsonOnly = false;

  argv.forEach((arg) => {
    if (arg === "--help" || arg === "-h") {
      printHelp();
      process.exit(0);
    }
    if (arg === "--accurate") {
      options.accurate = true;
      return;
    }
    if (arg === "--json") {
      jsonOnly = true;
      return;
    }
    if (arg.startsWith("--out=")) {
      outPath = path.resolve(ROOT_DIR, arg.slice("--out=".length));
      return;
    }
    if (!arg.startsWith("--")) return;

    const [rawKey, rawValue = "true"] = arg.slice(2).split("=");
    options[rawKey] = parseValue(rawValue);
  });

  return { options, outPath, jsonOnly };
}

function printHelp() {
  console.log(`
Usage:
  node scripts/ai-tuner.js [options]

Common options:
  --generations=8
  --populationSize=24
  --matchesPerGeneration=32
  --roundsPerMatch=8
  --seatRotations=2
  --finalMatches=64
  --drawSampleMax=10
  --accurate
  --out=ai-tuning-result.json
  --json

Fast example:
  node scripts/ai-tuner.js --generations=2 --populationSize=8 --matchesPerGeneration=4 --roundsPerMatch=4

Longer example:
  node scripts/ai-tuner.js --generations=8 --populationSize=24 --matchesPerGeneration=32 --roundsPerMatch=8 --finalMatches=64 --out=ai-tuning-result.json
`.trim());
}

function makeElementStub() {
  const noop = () => {};
  const element = {
    classList: {
      add: noop,
      remove: noop,
      toggle: noop,
      contains: () => false,
    },
    style: {
      setProperty: noop,
      removeProperty: noop,
    },
    dataset: {},
    children: [],
    appendChild: noop,
    querySelector: () => makeElementStub(),
    querySelectorAll: () => [],
    addEventListener: noop,
    removeEventListener: noop,
    setAttribute: noop,
    focus: noop,
    getBoundingClientRect: () => ({
      left: 0,
      top: 0,
      right: 0,
      bottom: 0,
      width: 100,
      height: 100,
    }),
  };

  return new Proxy(element, {
    get(target, property) {
      if (property in target) return target[property];
      if (
        property === "innerHTML" ||
        property === "textContent" ||
        property === "className" ||
        property === "ariaHidden" ||
        property === "disabled"
      ) {
        return "";
      }
      return noop;
    },
    set(target, property, value) {
      target[property] = value;
      return true;
    },
  });
}

function installHeadlessDom() {
  const element = makeElementStub();
  global.performance = performance;
  global.window = {
    AudioContext: null,
    webkitAudioContext: null,
    addEventListener: () => {},
    innerWidth: 1280,
    innerHeight: 900,
  };
  global.document = {
    body: element,
    documentElement: element,
    getElementById: () => element,
    createElement: () => makeElementStub(),
    querySelectorAll: () => [],
    addEventListener: () => {},
  };
  global.getComputedStyle = () => ({ getPropertyValue: () => "" });
  global.setTimeout = () => 0;
  global.clearTimeout = () => {};
}

function loadGameScript() {
  const html = fs.readFileSync(INDEX_HTML, "utf8");
  const scriptMatch = html.match(/<script>([\s\S]*)<\/script>/);
  if (!scriptMatch) {
    throw new Error(`Could not find inline script in ${INDEX_HTML}`);
  }
  new Function(scriptMatch[1])();
  if (typeof window.runAITuningTournament !== "function") {
    throw new Error("Game script did not expose window.runAITuningTournament");
  }
}

function printSummary(result) {
  console.log("");
  console.log(`Elapsed: ${(result.elapsedMs / 1000).toFixed(1)}s`);
  console.log(`Best: ${result.best.name} (${result.best.id})`);
  console.log(`Score/game: ${result.best.scorePerGame.toFixed(2)}`);
  console.log(`Match win rate: ${(result.best.matchWinRate * 100).toFixed(1)}%`);
  console.log(`Points/game: ${result.best.pointsPerGame.toFixed(2)}`);
  console.log(`Deal-ins/game: ${result.best.dealInsPerGame.toFixed(2)}`);
  console.log(`Chi take rate: ${(result.best.chiTakeRate * 100).toFixed(1)}%`);
  console.log("");
  console.log("Leaderboard:");
  console.table(result.leaderboard.map((entry) => ({
    id: entry.id,
    score: Number(entry.scorePerGame.toFixed(2)),
    winRate: `${(entry.matchWinRate * 100).toFixed(1)}%`,
    points: Number(entry.pointsPerGame.toFixed(2)),
    dealIns: Number(entry.dealInsPerGame.toFixed(2)),
    chi: `${(entry.chiTakeRate * 100).toFixed(1)}%`,
    windWin: `${(entry.windWinShare * 100).toFixed(1)}%`,
  })));
  console.log("Best overrides:");
  console.log(JSON.stringify(result.best.profile.overrides, null, 2));
}

function main() {
  const { options, outPath, jsonOnly } = parseArgs(process.argv.slice(2));
  installHeadlessDom();
  loadGameScript();

  const result = window.runAITuningTournament(options);
  if (outPath) {
    fs.writeFileSync(outPath, `${JSON.stringify(result, null, 2)}\n`);
  }

  if (jsonOnly) {
    console.log(JSON.stringify(result, null, 2));
    return;
  }

  printSummary(result);
  if (outPath) {
    console.log(`Saved full result to ${path.relative(ROOT_DIR, outPath)}`);
  }
}

main();
