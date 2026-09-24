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

const bookModel = JSON.parse(readFileSync(join(repoRoot, "assets/book-model.json"), "utf8"));
const canonicalPages = ["index.html", ...bookModel.documents.map(doc => doc.path.replace(/\.qmd$/, ".html")), "chapters/za_ispis.html"];

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
  await page.waitForFunction(() => !document.querySelector('main') ||
    document.querySelector('main').dataset.mf1MathReady === 'true', null, {timeout: 60_000});
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
          unnecessaryMathScrollers: [...document.querySelectorAll('.math.inline')]
            .filter(element => {
              const width = element.querySelector('mjx-container')?.getBoundingClientRect().width;
              const available = element.parentElement.getBoundingClientRect().width;
              return width > 0 && width < available - 2 &&
                ['auto', 'scroll'].includes(getComputedStyle(element).overflowX) &&
                element.scrollWidth > element.clientWidth;
            }).length,
          inaccessibleWideMath: [...document.querySelectorAll('.mf1-wide-math')]
            .filter(element => element.tabIndex !== 0 || !element.getAttribute('aria-label')).length,
          misplacedNotes: [...document.querySelectorAll('main [data-component][role="note"]')]
            .filter(element => element.getBoundingClientRect().width > 0 &&
              element.getBoundingClientRect().width < document.querySelector('main').getBoundingClientRect().width * 0.65).length,
          uncontainedDisplayMath: [
            ...document.querySelectorAll(".math.display"),
          ].filter((element) => {
            const style = getComputedStyle(element);
            return (
              element.scrollWidth > element.clientWidth + 1 &&
              !["auto", "scroll"].includes(style.overflowX)
            );
          }).length,
          inaccessibleWideTables: [...document.querySelectorAll("main table")]
            .filter((table) => {
              const region = table.closest(".mf1-table-scroll");
              return region && region.scrollWidth > region.clientWidth + 1 &&
                (region.tabIndex !== 0 || !region.getAttribute("aria-label"));
            }).length,
          chapterTools: document.querySelector("main .mf1-vjezbe-list") &&
            /\/u\d{2}_[^/]+\.html$/.test(location.pathname)
            ? [...document.querySelectorAll(".mf1-chapter-tools a")].map(a => a.href)
            : null,
          unexpandableSketches: [...document.querySelectorAll('main figure img[src*="/print/"]')]
            .filter((img) => {
              const link = img.closest("a");
              return !link || link.href !== img.src || link.target !== "_blank" ||
                !link.rel.split(/\s+/).includes("noopener") || !link.getAttribute("aria-label");
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
        if (metrics.inaccessibleWideTables > 0) {
          issues.push(`${relative} @ ${width}px: široka tablica nema imenovano područje dostupno tipkovnicom`);
        }
        if (metrics.unexpandableSketches > 0) {
          issues.push(`${relative} @ ${width}px: skica nema pristupačnu poveznicu za povećanje`);
        }
        if (metrics.chapterTools) {
          if (metrics.chapterTools.length !== 3) {
            issues.push(`${relative} @ ${width}px: nedostaju poveznice za rad s poglavljem`);
          }
          for (const href of metrics.chapterTools) {
            const url = new URL(href);
            const target = join(siteRoot, decodeURIComponent(url.pathname));
            const anchor = decodeURIComponent(url.hash.slice(1));
            if (!existsSync(target) ||
                (anchor && !readFileSync(target, "utf8").includes(`id="${anchor}"`))) {
              issues.push(`${relative}: nepostojeće odredište poveznice ${url.pathname}${url.hash}`);
            }
          }
        }
        if (width === 1440) {
          await page.addScriptTag({ path: axePath });
          // axe builds a virtual tree for the whole DOM even with an include
          // context. Temporarily detach unrelated chapters while auditing
          // each collection chapter in its original shell and styles. Restore
          // the exact nodes afterwards. Full-page geometry was checked above;
          // IDs, heading structure and links are also checked on the complete
          // document by audit_rendered_site.py and audit_rendered_model.py.
          const isCollection = relative === 'chapters/za_ispis.html';
          const chapterScopes = bookModel.documents.map(doc => [`#print-${doc.id}`]);
          const scopes = isCollection
            ? [null, ...chapterScopes.map(selector => ({include: [selector]}))]
            : [null];
          if (isCollection) {
            await page.evaluate(selectors => {
              window.mf1AuditChapters = selectors.map(([selector]) => {
                const node = document.querySelector(selector);
                if (!node) throw new Error(`Missing collection chapter ${selector}`);
                const slot = document.createComment(`audit ${selector}`);
                node.replaceWith(slot);
                return {node, slot};
              });
            }, chapterScopes);
          }
          const violations = [];
          for (const [scopeIndex, scope] of scopes.entries()) {
            if (isCollection && scopeIndex > 0) {
              await page.evaluate(index => {
                const {node, slot} = window.mf1AuditChapters[index];
                slot.replaceWith(node);
              }, scopeIndex - 1);
            }
            const result = await page.evaluate(async scope => window.axe.run(scope || document, {
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
            }), scope);
            violations.push(...result.violations);
            if (isCollection && scopeIndex > 0) {
              await page.evaluate(index => {
                const {node, slot} = window.mf1AuditChapters[index];
                node.replaceWith(slot);
              }, scopeIndex - 1);
            }
            if (scopes.length > 1) console.log(`Print accessibility scope ${scopeIndex + 1}/${scopes.length}`);
          }
          if (isCollection) {
            await page.evaluate(() => {
              for (const {node, slot} of window.mf1AuditChapters) slot.replaceWith(node);
              delete window.mf1AuditChapters;
            });
          }
          for (const violation of violations) {
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
        if (width === 1440 && !relative.endsWith('za_ispis.html')) {
          const chapterName = relative.split('/').pop().replace('.html', '');
          mkdirSync(snapshotRoot, { recursive: true });
          await page.screenshot({path: join(snapshotRoot, `${chapterName}-desktop.png`)});
          for (const [name, selector] of [['example', '[data-component="Example"]'], ['figure', '[data-component="Figure"]']]) {
            const component = page.locator(selector).first();
            if (await component.count()) {
              await component.scrollIntoViewIfNeeded();
              await page.screenshot({path: join(snapshotRoot, `${chapterName}-${name}.png`)});
            }
          }
        }
        if (metrics.unnecessaryMathScrollers > 0) {
          issues.push(`${relative} @ ${width}px: ${metrics.unnecessaryMathScrollers} kratkih formula ima nepotreban klizač`);
        }
        if (metrics.inaccessibleWideMath > 0) {
          issues.push(`${relative} @ ${width}px: duga jednadžba nije dostupna tipkovnicom`);
        }
        if (width === 320 && relative === 'chapters/u01_osnove_fluida_i_pascalov_zakon.html') {
          const longFormula = page.locator('.mf1-wide-math').first();
          await longFormula.focus();
          await longFormula.press('ArrowRight');
          await page.waitForFunction(() => document.querySelector('.mf1-wide-math')?.scrollLeft > 0);
          await page.setViewportSize({width:1440, height:900});
          await page.waitForFunction(() => !document.querySelector('.mf1-wide-math'));
          await page.setViewportSize({width:320, height:900});
          await page.waitForFunction(() => document.querySelector('.mf1-wide-math'));
        }
        if (width === 320 && (relative.endsWith('d06_kljuc_kontrolnih_rezultata.html') ||
                             relative.endsWith('za_ispis.html'))) {
          // Reproduce the Linux MathJax/font-size boundary on every platform.
          // The hidden MathML of this long formula used to widen the page by
          // 3–4 px, although the visible formula itself fitted the paragraph.
          const sizing = await page.addStyleTag({content:'mjx-container {font-size:117% !important}'});
          await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
          const assistive = await page.evaluate(() => {
            const formula = document.querySelector('#key-task-izlaz-lopatice-iz-izmjerene-sile');
            const nodes = [...formula.querySelectorAll('mjx-assistive-mml')];
            return {
              scroll: document.documentElement.scrollWidth,
              client: document.documentElement.clientWidth,
              readable: nodes.length > 0 && nodes.every(node => {
                const style = getComputedStyle(node);
                return node.querySelector('math') && style.display !== 'none' &&
                  style.visibility !== 'hidden' && !node.closest('[aria-hidden="true"]');
              }),
            };
          });
          if (assistive.scroll > assistive.client + 1 || !assistive.readable) {
            issues.push(`${relative}: MathML za čitače zaslona nije očuvan unutar stranice pri uvećanju jednadžbi`);
          }
          await sizing.evaluate(element => element.remove());
          await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
        }
        if (metrics.misplacedNotes > 0) {
          issues.push(`${relative} @ ${width}px: ${metrics.misplacedNotes} sadržajnih napomena premješteno je u usku marginu`);
        }
        checked += 1;
        console.log(`Checked ${relative} @ ${width}px (${checked})`);
      }

      await page.goto(
        `${baseUrl}/chapters/u13_gubici_cjevovodi_crpke_i_mreze.html`,
        {
          waitUntil: "domcontentloaded",
          timeout: 60_000,
        },
      );
      await settlePage(page);
      // Skrivena samoprovjera također sadrži calloute, ali ne prima fokus.
      const calloutHeader = page
        .locator('.callout-header[data-bs-toggle="collapse"]:visible')
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
      } else {
        issues.push(
          `U13 @ ${width}px: nema vidljivog sklopivog callouta za provjeru tipkovnice`,
        );
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
