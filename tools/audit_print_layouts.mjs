/** Verify print viewports against the actual SVG DOM, including transformed ink. */
import { createHash } from "node:crypto";
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { delimiter, dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright-core";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const layouts = JSON.parse(readFileSync(join(root, "assets/print-layouts.json"), "utf8"));
const sources = readdirSync(join(root, "source")).filter(n => n.endsWith(".md"))
  .map(n => readFileSync(join(root, "source", n), "utf8")).join("\n");
const used = new Set([...sources.matchAll(/\.\.\/assets\/print\/([^\s)]+)/g)].map(m => m[1]));
const names = process.platform === "win32" ? ["msedge.exe", "chrome.exe"]
  : ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"];
const candidates = [process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH, process.env.CHROME_PATH,
  "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
  "C:/Program Files/Google/Chrome/Application/chrome.exe",
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  ...(process.env.PATH || "").split(delimiter).flatMap(p => names.map(n => join(p, n)))];
const executablePath = candidates.find(p => p && existsSync(p));
if (!executablePath) throw new Error("Chromium/Chrome/Edge not found; set CHROME_PATH.");

const issues = [];
const contains = (p, b) => p[0] - 0.2 <= b[0] && p[1] - 0.2 <= b[1]
  && b[2] <= p[0] + p[2] + 0.2 && b[3] <= p[1] + p[3] + 0.2;
const cardStrokes = new Set(["#dce7f0", "#d4e3f0", "#cbd5e1", "#e2e8f0",
  "#c7d4dd", "#cbdce9", "#c8d6e4", "#cfd8df"]);
const nativeHeaders = new Set(["u02_fig_uvod_pregled.svg", "u04_fig_uvod_pregled.svg",
  "u09_fig_uvod_pregled.svg"]);
let textCount = 0, panelCount = 0;
const browser = await chromium.launch({executablePath, headless: true,
  args: process.platform === "linux" ? ["--disable-dev-shm-usage"] : []});
try {
  const page = await browser.newPage();
  for (const name of used) {
    const layout = layouts[name];
    if (!layout) { issues.push(`${name}: missing print layout`); continue; }
    const path = join(root, "assets/print", name);
    const source = readFileSync(path, "utf8").replace(/\r\n/g, "\n");
    if (createHash("sha1").update(source).digest("hex") !== layout.source_sha1)
      issues.push(`${name}: source changed; review viewports and note indices`);
    await page.goto(pathToFileURL(path).href);
    await page.evaluate(() => document.fonts.ready);
    const {width, height, ink} = await page.evaluate(() => {
      const svg = document.querySelector("svg"), v = svg.viewBox.baseVal;
      const inverse = svg.getScreenCTM().inverse();
      const elements = [...svg.querySelectorAll("text,path,rect,line,polyline,polygon,circle,ellipse")]
        .filter(e => !e.closest("defs"));
      return {width: v.width, height: v.height, ink: elements.map(e => {
        const b = e.getBBox(), m = inverse.multiply(e.getScreenCTM());
        // Windows resolves Segoe UI; Linux uses the declared Arial/sans-serif
        // fallback. Require room for both, even on a Windows developer machine.
        if (e.tagName === 'text') {
          const original = e.style.fontFamily;
          e.style.fontFamily = 'Arial, sans-serif';
          const fallback = e.getBBox();
          e.style.fontFamily = original;
          const right = Math.max(b.x + b.width, fallback.x + fallback.width);
          const bottom = Math.max(b.y + b.height, fallback.y + fallback.height);
          b.x = Math.min(b.x, fallback.x); b.y = Math.min(b.y, fallback.y);
          b.width = right - b.x; b.height = bottom - b.y;
        }
        const points = [[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]]
          .map(([x,y]) => new DOMPoint(x,y).matrixTransform(m));
        return {tag: e.tagName, id: e.id, text: e.textContent,
          font: parseFloat(getComputedStyle(e).fontSize),
          fill: e.getAttribute("fill"), stroke: e.getAttribute("stroke"),
          rx: Number(e.getAttribute("rx") || 0),
          box: [Math.min(...points.map(p=>p.x)),Math.min(...points.map(p=>p.y)),
            Math.max(...points.map(p=>p.x)),Math.max(...points.map(p=>p.y))]};
      })};
    });
    const noteIndices = [...(layout.before || []), ...(layout.after || [])];
    const notes = new Set(noteIndices);
    const texts = ink.filter(e => e.tag === "text");
    if (notes.size !== noteIndices.length || [...notes].some(i => !Number.isInteger(i) || i < 1 || i > texts.length))
      issues.push(`${name}: invalid or duplicate note index`);
    for (const p of layout.panels) {
      if (p.length < 4 || p.length > 7 || !p.every(Number.isFinite)
          || p[0] < 0 || p[1] < 0 || p[2] <= 0 || p[3] <= 0
          || p[0] + p[2] > width + 0.2 || p[1] + p[3] > height + 0.2
          || (p[4] !== undefined && ![0,90].includes(p[4]))
          || (p[6] !== undefined && (p[6] <= 0 || p[6] > (p[4] ? 640 : 510))))
        issues.push(`${name}: invalid viewport ${JSON.stringify(p)}`);
      panelCount++;
    }
    let index = 0;
    for (const e of ink) {
      const covered = layout.panels.filter(p => contains(p, e.box));
      if (e.tag === "text") {
        index++; textCount++;
        if (notes.has(index) || !e.text.trim()) continue;
        if (!covered.length) issues.push(`${name}: clipped text #${index}: ${e.text.trim()}`);
      } else if (!covered.length) {
        const b = e.box;
        const textInside = texts.map((t,i) => ({t, index:i+1}))
          .filter(({t}) => contains([b[0],b[1],b[2]-b[0],b[3]-b[1]],t.box));
        const noteCard = e.rx > 0 && textInside.length > 0
          && textInside.every(({index}) => notes.has(index));
        const canvasFrame = b[0] <= 20 && b[1] <= 20
          && b[2] >= width-20 && b[3] >= height-20;
        const background = e.tag === "rect" && ["white", "#ffffff", "#fff"].includes(e.fill)
          && (cardStrokes.has(e.stroke) || canvasFrame || noteCard);
        const divider = e.tag === "line" && cardStrokes.has(e.stroke);
        // Three dark header backgrounds are intentionally replaced by native
        // headings; their text is preserved through the indexed SVG notes.
        const header = nativeHeaders.has(name) && e.tag === "rect"
          && /^url\(#.*hdr\)$/.test(e.fill || "") && b[3] <= 54;
        if (!background && !divider && !header)
          issues.push(`${name}: clipped ${e.tag} ${e.id || JSON.stringify(b)}`);
      }
    }
  }
} finally { await browser.close(); }
for (const name of Object.keys(layouts)) if (!used.has(name)) issues.push(`${name}: unused print layout`);
if (issues.length) {
  console.error(issues.join("\n")); process.exitCode = 1;
} else {
  console.log(`PASS: ${used.size} canonical SVGs, ${panelCount} source viewports, ${textCount} text elements covered.`);
  await import('./audit_print_figures.mjs');
}
