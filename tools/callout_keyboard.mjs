/** Assert completed keyboard toggles, including the actual panel and focus. */
export async function checkCalloutKeyboard(page, header) {
  const initial = await header.getAttribute('aria-expanded');
  const selector = await header.getAttribute('data-bs-target');
  if (await header.getAttribute('role') !== 'button' ||
      await header.getAttribute('tabindex') !== '0' ||
      !['true', 'false'].includes(initial) || !selector ||
      await page.locator(selector).count() !== 1) {
    throw new Error('Missing callout button semantics or unique target panel');
  }
  const button = await header.elementHandle();
  try {
    await header.focus();
    for (const [key, expanded] of [['Enter', initial !== 'true'], ['Space', initial === 'true']]) {
      await page.keyboard.press(key);
      // Bootstrap updates aria-expanded before the height transition ends;
      // another toggle during that transition is intentionally ignored.
      await page.waitForFunction(({button, selector, expanded}) => {
        const panel = document.querySelector(selector);
        return button.getAttribute('aria-expanded') === String(expanded) &&
          document.activeElement === button && panel &&
          !panel.classList.contains('collapsing') &&
          panel.classList.contains('show') === expanded &&
          (panel.getBoundingClientRect().height > 0) === expanded;
      }, {button, selector, expanded}, {timeout: 10000});
    }
  } catch (error) {
    const state = await header.evaluate(button => {
      const panel = document.querySelector(button.getAttribute('data-bs-target'));
      return {expanded:button.getAttribute('aria-expanded'), focused:document.activeElement === button,
        panelClass:panel?.className, height:panel?.getBoundingClientRect().height};
    });
    throw new Error(`Keyboard toggle did not finish: ${JSON.stringify(state)}; ${error.message}`);
  } finally {
    await button.dispose();
  }
}
