import {enhanceMath} from './math.js';

(() => {
  "use strict";

  const enhanceCollapsibleCallouts = () => {
    const headers = document.querySelectorAll(
      '.callout-header[data-bs-toggle="collapse"]'
    );

    for (const header of headers) {
      if (header.dataset.mf1KeyboardReady === "true") continue;

      const titleCopy = header
        .querySelector(".callout-title-container")
        ?.cloneNode(true);
      titleCopy
        ?.querySelectorAll(".screen-reader-only")
        .forEach((element) => element.remove());
      const title = titleCopy?.textContent.replace(/\s+/g, " ").trim();
      header.setAttribute("role", "button");
      header.setAttribute("tabindex", "0");
      header.setAttribute(
        "aria-label",
        title
          ? `Prikaži ili sakrij odjeljak: ${title}`
          : "Prikaži ili sakrij odjeljak"
      );
      header.dataset.mf1KeyboardReady = "true";

      header.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" && event.key !== " ") return;
        event.preventDefault();
        header.click();
      });
    }
  };

  const enhanceReading = async () => {
    document.querySelectorAll("[data-mf1-print-button]").forEach(button => button.addEventListener("click", () => window.print()));
    const main = document.querySelector("main");
    if (!main) return;
    enhanceMath(main);

    main.querySelectorAll('figure img[src*="/print/"]').forEach((img) => {
      if (img.closest("a")) return;
      const figure = img.closest("figure");
      const link = document.createElement("a");
      link.className = "mf1-figure-link";
      link.href = img.src;
      link.target = "_blank";
      link.rel = "noopener";
      link.setAttribute("aria-label", `Povećaj skicu: ${img.alt} (nova kartica)`);
      img.before(link);
      link.append(img);
      const caption = figure.querySelector("figcaption");
      if (caption) {
        const action = link.cloneNode(false);
        action.className = "mf1-figure-expand";
        action.textContent = "Povećaj skicu ↗";
        caption.append(action);
      }
    });

    // A table keeps its native layout; its own region scrolls on narrow screens.
    main.querySelectorAll("table").forEach((table, index) => {
      const region = document.createElement("div");
      region.className = "mf1-table-scroll";
      region.setAttribute("role", "region");
      region.setAttribute("aria-label", table.caption?.textContent.trim() || `Tablica ${index + 1}`);
      table.before(region);
      region.append(table);
      const hint = document.createElement("p");
      hint.className = "mf1-table-hint";
      hint.textContent = "Tablicu možeš pomicati vodoravno.";
      hint.hidden = true;
      region.after(hint);
      const update = () => {
        const wide = region.scrollWidth > region.clientWidth + 1;
        hint.hidden = !wide;
        if (wide) region.tabIndex = 0;
        else region.removeAttribute("tabindex");
      };
      new ResizeObserver(update).observe(region);
      update();
    });

    // Separate print canvases retain their physical point sizes. The screen
    // illustration and its enlargement link remain the canonical original.
    main.querySelectorAll('img[data-mf1-print-layout]').forEach((img) => {
      const original = img.closest('.mf1-figure-link') || img;
      const rows = JSON.parse(img.dataset.mf1PrintLayout);
      const group = document.createElement('span');
      group.className = 'mf1-print-figure';
      group.dataset.figureKind = img.dataset.mf1FigureKind;
      group.setAttribute('aria-hidden', 'true');
      for (const row of rows) {
        const art = document.createElement('img');
        art.src = new URL('../pdf-figures/' + row.file, img.src).href;
        art.alt = '';
        art.style.width = row.width + 'pt';
        art.style.height = row.height + 'pt';
        art.loading = 'eager';
        if (row.keep_with_next) art.classList.add('mf1-keep-with-next');
        group.append(art);
      }
      original.classList.add('mf1-screen-figure');
      original.after(group);
    });

    // Links reuse existing destinations, including the generated answer key.
    const response = await fetch(new URL('../assets/book-model.json', import.meta.url));
    if (!response.ok) throw new Error('Book model could not be loaded.');
    const model = await response.json();
    const chapter = model.documents.find(doc => location.pathname.endsWith('/' + doc.path.replace(/\.qmd$/, '.html')));
    if (!chapter || chapter.kind !== 'chapter') return;
    const byRole = role => model.documents.find(doc => doc.role === role).path.split('/').pop().replace(/\.qmd$/, '.html');
    const exercises = main.querySelector(".mf1-vjezbe-list");
    // Empty spans preserve earlier URLs; the answer key uses the current heading.
    const firstTask = exercises?.querySelector('[data-component="Problem"] h3[id^="task-"]');
    const section = exercises?.closest("section[id]");
    const title = main.querySelector("#title-block-header");
    if (!firstTask || !section || !title) return;
    const nav = document.createElement("nav");
    nav.className = "mf1-chapter-tools";
    nav.setAttribute("aria-label", "Rad s poglavljem");
    for (const [label, href] of [
      ["Zadatci za vježbu", `#${section.id}`],
      ["Formule i oznake", byRole("formulas")],
      ["Kontrolni rezultati", `${byRole("answers")}#key-${firstTask.id}`],
    ]) {
      const link = document.createElement("a");
      link.textContent = label;
      link.href = href;
      nav.append(link);
    }
    title.after(nav);
  };

  if (document.readyState === "loading") {
    document.addEventListener(
      "DOMContentLoaded",
      () => {
        enhanceCollapsibleCallouts();
        enhanceReading();
      },
      { once: true }
    );
  } else {
    enhanceCollapsibleCallouts();
    enhanceReading();
  }
})();
