// Short inline formulas share the text baseline. Only a formula wider than its
// containing paragraph gets a scroll region; italic ink is not an overflow test.
export async function enhanceMath(main) {
  if (document.readyState !== 'complete') {
    await new Promise(resolve => window.addEventListener('load', resolve, {once: true}));
  }
  await globalThis.MathJax?.startup?.promise;
  await document.fonts.ready;
  const formulas = [...main.querySelectorAll('.math.inline')].map(element => {
    let block = element.parentElement;
    while (block !== main && getComputedStyle(block).display === 'inline') {
      block = block.parentElement;
    }
    return {element, block};
  });
  // A numbered display formula reserves room for its number on both sides.
  // When it does not fit, the number moves below the formula (right-aligned)
  // instead of disappearing behind the scroll edge; MathML is unchanged.
  const tagged = [...main.querySelectorAll('.math.display')].map(element => {
    const parts = {
      container: element.querySelector('mjx-container'),
      mtable: element.querySelector('mjx-mtable'),
      table: element.querySelector('mjx-mtable > mjx-table'),
      labels: element.querySelector('mjx-mtable > mjx-labels'),
    };
    if (!parts.container || !parts.mtable || !parts.table || !parts.labels) return null;
    const original = {
      container: parts.container.style.minWidth,
      mtable: parts.mtable.style.minWidth,
      table: parts.table.style.margin,
      labels: parts.labels.style.width,
    };
    return {element, parts, original};
  }).filter(Boolean);
  const setCompact = ({element, parts, original}, compact) => {
    element.classList.toggle('mf1-math-compact', compact);
    parts.container.style.minWidth = compact ? '' : original.container;
    parts.mtable.style.minWidth = compact ? '' : original.mtable;
    parts.table.style.margin = compact ? '0' : original.table;
    parts.labels.style.width = compact ? '' : original.labels;
  };
  const updateTagged = () => {
    for (const item of tagged) setCompact(item, false);
    const overflowing = tagged.map(({element}) => element.scrollWidth > element.clientWidth + 1);
    tagged.forEach((item, index) => { if (overflowing[index]) setCompact(item, true); });
  };
  let pending = false;
  const update = () => {
    pending = false;
    updateTagged();
    // Read geometry first, then change classes to avoid repeated layout passes.
    const measured = formulas.map(({element, block}) => {
      const math = element.querySelector('mjx-container');
      const style = getComputedStyle(block);
      const available = block.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
      return {element, wide: available > 0 && math?.getBoundingClientRect().width > available + 1};
    });
    for (const {element, wide} of measured) {
      element.classList.toggle('mf1-wide-math', Boolean(wide));
      if (wide) {
        element.tabIndex = 0;
        element.setAttribute('role', 'region');
        element.setAttribute('aria-label', 'Duga jednadžba, vodoravni pomak');
      } else {
        element.removeAttribute('tabindex');
        element.removeAttribute('role');
        element.removeAttribute('aria-label');
      }
    }
    main.dataset.mf1MathReady = 'true';
  };
  const schedule = () => {
    if (!pending) {
      pending = true;
      requestAnimationFrame(update);
    }
  };
  new ResizeObserver(schedule).observe(main);
  document.fonts.addEventListener('loadingdone', schedule);
  main.addEventListener('shown.bs.collapse', schedule);
  update();
}
