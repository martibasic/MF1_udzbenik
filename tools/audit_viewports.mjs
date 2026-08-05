/** Headless pregled kanonskih HTML stranica na 320, 768 i 1440 px. */

import { createRequire } from "node:module";
import { createServer } from "node:http";
import {
  accessSync,
  constants,
  existsSync,
  mkdirSync,
  readFileSync,
  statSync,
} from "node:fs";
import {
  delimiter,
  dirname,
  extname,
  join,
  normalize,
  resolve,
  sep,
} from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";

const require = createRequire(import.meta.url);
const axePath = require.resolve("axe-core/axe.min.js");
const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const cliArguments = process.argv.slice(2);
if (cliArguments.includes("--help")) {
  console.log(
    "Uporaba: node tools/audit_viewports.mjs [--jlite-only] [putanja-do-_site]",
  );
  process.exit(0);
}
const unknownOptions = cliArguments.filter(
  (argument) => argument.startsWith("--") && argument !== "--jlite-only",
);
if (unknownOptions.length) {
  throw new Error(`Nepoznata opcija: ${unknownOptions.join(", ")}`);
}
const positionalArguments = cliArguments.filter(
  (argument) => !argument.startsWith("--"),
);
if (positionalArguments.length > 1) {
  throw new Error("Dopuštena je najviše jedna putanja do renderiranog sitea.");
}
const jupyterLiteOnly = cliArguments.includes("--jlite-only");
const siteRoot = resolve(repoRoot, positionalArguments[0] || "_site");
const snapshotRoot = resolve(repoRoot, "tools", "tmp", "visual");

const canonicalPages = [
  "index.html",
  "chapters/u00_kako_koristiti_udzbenik.html",
  ...Array.from({ length: 15 }, (_, index) => {
    const code = String(index + 1).padStart(2, "0");
    const names = [
      "osnove_fluida_i_pascalov_zakon",
      "viskoznost_povrsinska_napetost_i_kapilarnost",
      "hidrostaticka_raspodjela_tlaka_i_manometrija",
      "relativno_mirovanje_fluida",
      "hidrostatske_sile_na_plohe",
      "uzgon_plivanje_i_stabilnost",
      "kinematika_kontrolni_volumen_i_kontinuitet",
      "energijska_jednadzba_i_bernoulli",
      "kompresibilni_idealni_tok",
      "kolicina_i_moment_kolicine_gibanja",
      "dimenzijska_analiza_i_slicnost",
      "diferencijalni_opis_realnog_toka",
      "gubici_cjevovodi_crpke_i_mreze",
      "turbostrojevi_i_propulzija",
      "otvoreni_tokovi",
    ];
    return `chapters/u${code}_${names[index]}.html`;
  }),
  ...Array.from({ length: 6 }, (_, index) => {
    const names = [
      "sazetak_formula_i_oznaka",
      "pojmovnik",
      "tipicne_pogreske_po_poglavljima",
      "numericka_mehanika_fluida",
      "literatura",
      "kljuc_kontrolnih_rezultata",
    ];
    const code = String(index + 1).padStart(2, "0");
    return `chapters/d${code}_${names[index]}.html`;
  }),
  "chapters/za_ispis.html",
];

const mime = {
  ".css": "text/css",
  ".gif": "image/gif",
  ".html": "text/html; charset=utf-8",
  ".ico": "image/x-icon",
  ".jpeg": "image/jpeg",
  ".jpg": "image/jpeg",
  ".js": "text/javascript",
  ".json": "application/json",
  ".mjs": "text/javascript",
  ".png": "image/png",
  ".pdf": "application/pdf",
  ".svg": "image/svg+xml",
  ".ttf": "font/ttf",
  ".wasm": "application/wasm",
  ".webp": "image/webp",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
  ".xml": "application/xml",
};

function environmentValue(name) {
  const key = Object.keys(process.env).find(
    (item) => item.toUpperCase() === name,
  );
  return key ? process.env[key] : undefined;
}

function browserExecutable() {
  const override = environmentValue("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH");
  const chromePath = environmentValue("CHROME_PATH");
  const pathDirectories = (environmentValue("PATH") || "")
    .split(delimiter)
    .map((item) => item.replace(/^"|"$/g, ""))
    .filter(Boolean);
  const executableNames =
    process.platform === "win32"
      ? ["msedge.exe", "chrome.exe", "chromium.exe"]
      : [
          "google-chrome",
          "google-chrome-stable",
          "chromium",
          "chromium-browser",
          "microsoft-edge",
        ];
  const pathCandidates = pathDirectories.flatMap((directory) =>
    executableNames.map((name) => join(directory, name)),
  );

  let platformCandidates;
  if (process.platform === "win32") {
    const programFiles =
      environmentValue("PROGRAMFILES") || "C:\\Program Files";
    const programFilesX86 =
      environmentValue("PROGRAMFILES(X86)") || "C:\\Program Files (x86)";
    const localAppData = environmentValue("LOCALAPPDATA");
    platformCandidates = [
      join(programFilesX86, "Microsoft", "Edge", "Application", "msedge.exe"),
      join(programFiles, "Microsoft", "Edge", "Application", "msedge.exe"),
      join(programFiles, "Google", "Chrome", "Application", "chrome.exe"),
      ...(localAppData
        ? [
            join(
              localAppData,
              "Microsoft",
              "Edge",
              "Application",
              "msedge.exe",
            ),
            join(localAppData, "Google", "Chrome", "Application", "chrome.exe"),
          ]
        : []),
    ];
  } else if (process.platform === "darwin") {
    platformCandidates = [
      "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
      "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ];
  } else {
    platformCandidates = [
      "/usr/bin/google-chrome",
      "/usr/bin/google-chrome-stable",
      "/usr/bin/chromium",
      "/usr/bin/chromium-browser",
      "/usr/bin/microsoft-edge",
      "/snap/bin/chromium",
    ];
  }

  const candidates = [
    ...new Set(
      [override, chromePath, ...platformCandidates, ...pathCandidates].filter(
        Boolean,
      ),
    ),
  ];
  const found = candidates.find((candidate) => {
    try {
      if (!statSync(candidate).isFile()) return false;
      accessSync(candidate, constants.X_OK);
      return true;
    } catch {
      return false;
    }
  });
  if (!found) {
    throw new Error(
      "Nije pronađen sistemski Chromium preglednik. Postavite " +
        "PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH ili instalirajte Chrome, Edge ili Chromium.",
    );
  }
  return found;
}

function staticServer() {
  return createServer((request, response) => {
    let requestPath;
    try {
      requestPath = decodeURIComponent(
        new URL(request.url || "/", "http://127.0.0.1").pathname,
      );
    } catch {
      response.writeHead(400).end("Bad request");
      return;
    }
    const relative =
      requestPath === "/" ? "index.html" : requestPath.replace(/^\/+/, "");
    let target = resolve(siteRoot, normalize(relative));
    if (!(target === siteRoot || target.startsWith(siteRoot + sep))) {
      response.writeHead(403).end("Forbidden");
      return;
    }
    if (existsSync(target) && statSync(target).isDirectory())
      target = join(target, "index.html");
    if (!existsSync(target) || !statSync(target).isFile()) {
      response.writeHead(404).end("Not found");
      return;
    }
    response.writeHead(200, {
      "Content-Type":
        mime[extname(target).toLowerCase()] || "application/octet-stream",
      "Cache-Control": "no-store",
    });
    response.end(readFileSync(target));
  });
}

async function settlePage(page) {
  const ready = await page.evaluate(async () => {
    const readiness = (async () => {
      if (document.fonts) await document.fonts.ready;
      const mathJaxReady = globalThis.MathJax?.startup?.promise;
      if (mathJaxReady) await mathJaxReady;
      return true;
    })();
    return Promise.race([
      readiness,
      new Promise((accept) => setTimeout(() => accept(false), 60_000)),
    ]);
  });
  if (!ready) throw new Error("Stranica se nije stabilizirala unutar 60 s.");
}

async function auditJupyterLiteRuntime(browser, baseUrl, issues) {
  const context = await browser.newContext({
    viewport: { width: 1280, height: 900 },
    locale: "hr-HR",
  });
  const page = await context.newPage();
  const pageErrors = [];
  page.on("pageerror", (error) => pageErrors.push(error.message));

  try {
    const notebookName = "u01_hidraulicna_presa.ipynb";
    let response;
    try {
      response = await page.goto(
        `${baseUrl}/jlite/lab/index.html?path=${encodeURIComponent(notebookName)}`,
        { waitUntil: "domcontentloaded", timeout: 60_000 },
      );
    } catch (error) {
      issues.push(`JupyterLite runtime se ne može otvoriti: ${error.message}`);
      return;
    }
    if (!response?.ok()) {
      issues.push(`JupyterLite runtime: HTTP ${response?.status()}`);
      return;
    }
    try {
      // Koristimo javno vidljivi statusni ugovor JupyterLaba, ne internu
      // strukturu widgeta: notebook mora biti otvoren, kernel imenovan i Idle.
      await page.waitForFunction(
        (expectedNotebook) => {
          const text = document.body?.innerText || "";
          return (
            text.includes(expectedNotebook) &&
            text.includes("Python (Pyodide)") &&
            /(^|\s)Idle($|\s)/m.test(text)
          );
        },
        notebookName,
        { polling: 500, timeout: 180_000 },
      );
      await page.waitForTimeout(1_000);
      mkdirSync(snapshotRoot, { recursive: true });
      await page.screenshot({
        path: join(snapshotRoot, "jlite-python-idle.png"),
        fullPage: false,
      });
    } catch (error) {
      const statusText = await page.evaluate(() =>
        (document.body?.innerText || "").replace(/\s+/g, " ").slice(-600),
      );
      issues.push(
        `JupyterLite runtime nije dosegao Python (Pyodide) | Idle: ${statusText || error.message}`,
      );
    }
  } finally {
    for (const message of pageErrors) {
      issues.push(`JupyterLite JavaScript page error: ${message}`);
    }
    await context.close();
  }
}

if (!existsSync(join(siteRoot, "index.html"))) {
  throw new Error(`Nema renderiranog sitea u ${siteRoot}`);
}
if (!existsSync(join(siteRoot, "jlite", "lab", "index.html"))) {
  throw new Error(`Nema JupyterLite aplikacije u ${join(siteRoot, "jlite")}`);
}
if (!jupyterLiteOnly) {
  for (const page of canonicalPages) {
    if (!existsSync(join(siteRoot, page))) throw new Error(`Nedostaje ${page}`);
  }
}

const server = staticServer();
await new Promise((accept) => server.listen(0, "127.0.0.1", accept));
const address = server.address();
const baseUrl = `http://127.0.0.1:${address.port}`;
const issues = [];
let checked = 0;
let browser;

try {
  browser = await chromium.launch({
    executablePath: browserExecutable(),
    headless: true,
    args: process.platform === "linux" ? ["--disable-dev-shm-usage"] : [],
  });
  if (!jupyterLiteOnly)
    for (const width of [320, 768, 1440]) {
      const context = await browser.newContext({
        viewport: { width, height: 900 },
        reducedMotion: "reduce",
        colorScheme: "light",
        locale: "hr-HR",
      });
      const page = await context.newPage();
      for (const relative of canonicalPages) {
        const response = await page.goto(`${baseUrl}/${relative}`, {
          waitUntil: "domcontentloaded",
          timeout: 60_000,
        });
        if (!response?.ok()) {
          issues.push(`${relative} @ ${width}px: HTTP ${response?.status()}`);
          continue;
        }
        await settlePage(page);
        const metrics = await page.evaluate(() => ({
          client: document.documentElement.clientWidth,
          scroll: document.documentElement.scrollWidth,
          motion: getComputedStyle(document.documentElement).scrollBehavior,
          uncontainedDisplayMath: [
            ...document.querySelectorAll(".math.display"),
          ].filter((element) => {
            const style = getComputedStyle(element);
            return (
              element.scrollWidth > element.clientWidth + 1 &&
              !["auto", "scroll"].includes(style.overflowX)
            );
          }).length,
        }));
        if (metrics.scroll > metrics.client + 1) {
          issues.push(
            `${relative} @ ${width}px: horizontalni overflow ${metrics.scroll - metrics.client}px`,
          );
        }
        if (metrics.motion !== "auto") {
          issues.push(
            `${relative}: prefers-reduced-motion ne isključuje smooth scroll`,
          );
        }
        if (metrics.uncontainedDisplayMath > 0) {
          issues.push(
            `${relative} @ ${width}px: ${metrics.uncontainedDisplayMath} širokih jednadžbi nema lokalni horizontalni pomak`,
          );
        }
        if (width === 1440) {
          await page.addScriptTag({ path: axePath });
          const result = await page.evaluate(async () =>
            window.axe.run(document, {
              runOnly: {
                type: "tag",
                values: [
                  "wcag2a",
                  "wcag2aa",
                  "wcag21a",
                  "wcag21aa",
                  "wcag22aa",
                ],
              },
            }),
          );
          for (const violation of result.violations) {
            const targets = violation.nodes
              .slice(0, 3)
              .map((node) => node.target.join(" "))
              .join("; ");
            issues.push(
              `${relative}: axe ${violation.id} (${violation.nodes.length} čvorova; ${targets})`,
            );
          }
          await page.keyboard.press("Tab");
          const focus = await page.evaluate(() => {
            const active = document.activeElement;
            const style = active ? getComputedStyle(active) : null;
            const rectangle = active?.getBoundingClientRect();
            return {
              tag: active?.tagName || "",
              outline: style?.outlineStyle || "none",
              width: parseFloat(style?.outlineWidth || "0"),
              shadow: style?.boxShadow || "none",
              visible: Boolean(
                rectangle &&
                  rectangle.width > 0 &&
                  rectangle.height > 0 &&
                  rectangle.bottom > 0 &&
                  rectangle.right > 0 &&
                  rectangle.top < innerHeight &&
                  rectangle.left < innerWidth &&
                  style?.visibility !== "hidden" &&
                  style?.display !== "none",
              ),
            };
          });
          const hasIndicator =
            (focus.outline !== "none" && focus.width >= 2) ||
            focus.shadow !== "none";
          if (
            !focus.visible ||
            !focus.tag ||
            focus.tag === "BODY" ||
            !hasIndicator
          ) {
            issues.push(
              `${relative}: prvi tipkovnički fokus nije jasno vidljiv`,
            );
          }
        }
        checked += 1;
      }

      await page.goto(
        `${baseUrl}/chapters/u13_gubici_cjevovodi_crpke_i_mreze.html`,
        {
          waitUntil: "domcontentloaded",
          timeout: 60_000,
        },
      );
      await settlePage(page);
      const calloutHeader = page
        .locator('.callout-header[data-bs-toggle="collapse"]')
        .first();
      if (await calloutHeader.count()) {
        const role = await calloutHeader.getAttribute("role");
        const tabIndex = await calloutHeader.getAttribute("tabindex");
        const initial = await calloutHeader.getAttribute("aria-expanded");
        await calloutHeader.focus();
        await page.keyboard.press("Enter");
        await page.waitForTimeout(250);
        const afterEnter = await calloutHeader.getAttribute("aria-expanded");
        await page.keyboard.press("Space");
        await page.waitForTimeout(250);
        const afterSpace = await calloutHeader.getAttribute("aria-expanded");
        if (
          role !== "button" ||
          tabIndex !== "0" ||
          afterEnter === initial ||
          afterSpace !== initial
        ) {
          issues.push(
            `U13 @ ${width}px: sklopivi callout nije potpuno dostupan tipkovnicom`,
          );
        }
      }
      mkdirSync(snapshotRoot, { recursive: true });
      await page.screenshot({
        path: join(snapshotRoot, `u13-${width}.png`),
        fullPage: false,
      });
      await context.close();
    }

  if (!jupyterLiteOnly) {
    const printContext = await browser.newContext({
      viewport: { width: 794, height: 1123 },
    });
    const printPage = await printContext.newPage();
    // Reprezentativna stranica s jednadžbama, slikama, zadatcima i sklopivim
    // rješenjima daje isti A4 CSS ugovor bez učitavanja svih 104 slika iz
    // cjelokupnog pregledničkog ispisa u jedan Chromium proces.
    await printPage.goto(
      `${baseUrl}/chapters/u13_gubici_cjevovodi_crpke_i_mreze.html`,
      {
      waitUntil: "domcontentloaded",
      timeout: 60_000,
      },
    );
    await printPage.emulateMedia({ media: "print", reducedMotion: "reduce" });
    await settlePage(printPage);
    const exposedTaskHelp = await printPage.locator(
      '[data-hint-key="true"]:visible, [data-answer-key="true"]:visible',
    ).count();
    if (exposedTaskHelp > 0) {
      issues.push(
        `A4 ispis: ${exposedTaskHelp} naputaka ili rezultata ostalo je uz zadatak`,
      );
    }
    mkdirSync(snapshotRoot, { recursive: true });
    await printPage.screenshot({
      path: join(snapshotRoot, "knjiga-a4-print.png"),
      fullPage: false,
      timeout: 60_000,
    });
    await printContext.close();
  }

  await auditJupyterLiteRuntime(browser, baseUrl, issues);
} finally {
  if (browser) await browser.close();
  await new Promise((accept) => server.close(accept));
}

if (issues.length) {
  console.error("Viewport/WCAG audit FAIL:");
  for (const issue of [...new Set(issues)]) console.error(`  - ${issue}`);
  process.exitCode = 1;
} else {
  const visualSummary = jupyterLiteOnly
    ? ""
    : `${checked} prikaza + A4 print, širine 320/768/1440 px; `;
  console.log(
    `Viewport/WCAG audit PASS: ${visualSummary}JupyterLite Python=Idle`,
  );
}
