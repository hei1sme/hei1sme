// Requires Playwright in your tooling environment. PROFILE_PLAYWRIGHT may point
// to an existing installation; no application runtime or dependency is shipped.
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require(process.env.PROFILE_PLAYWRIGHT || 'playwright');
const root = path.resolve(__dirname, '..');
(async () => {
  const browser = await chromium.launch({ headless: true, ...(process.env.PROFILE_BROWSER_CHANNEL ? { channel: process.env.PROFILE_BROWSER_CHANNEL } : {}) });
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 480 }, deviceScaleFactor: 2 });
    const svg = fs.readFileSync(path.join(root, 'assets/profile-hero.svg'), 'utf8');
    await page.setContent(`<html><head><meta charset="utf-8"/><style>html,body{margin:0;width:1280px;height:480px;background:transparent}svg{display:block}</style></head><body>${svg}</body></html>`);
    await page.evaluate(async () => {
      await document.fonts.load('550 66px ProfileManrope');
      await document.fonts.ready;
      await Promise.all([...document.querySelectorAll('image')].map(image => new Promise((resolve, reject) => {
        const asset = new Image();
        asset.onload = resolve; asset.onerror = reject;
        asset.src = image.getAttribute('href');
      })));
    });
    await page.screenshot({ path: path.join(root, 'assets/profile-hero.png'), omitBackground: true });
    process.stdout.write('Rendered assets/profile-hero.png at 2x\n');
  } finally { await browser.close(); }
})().catch(error => { process.stderr.write(`${error.stack}\n`); process.exitCode = 1; });
