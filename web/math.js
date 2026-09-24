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
  let pending = false;
  const update = () => {
    pending = false;
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
