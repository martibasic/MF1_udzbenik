/** Run the actual notebook controls in the distributed Pyodide application. */
import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFileSync, existsSync, statSync, mkdirSync} from 'node:fs';
import {resolve, join, extname, delimiter, sep} from 'node:path';
import {chromium} from 'playwright-core';

const site = resolve(process.argv[2] || '_site');
const snapshots = resolve('tools/tmp/interactive-labs');
mkdirSync(snapshots, {recursive:true});
const types = {'.html':'text/html; charset=utf-8','.js':'application/javascript',
 '.css':'text/css','.json':'application/json','.svg':'image/svg+xml',
 '.wasm':'application/wasm','.woff2':'font/woff2','.png':'image/png'};
const server = createServer((req,res) => {
 try {
  let file=resolve(site,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
  if (!(file===site || file.startsWith(site+sep))) {res.writeHead(403).end();return;}
  if (existsSync(file) && statSync(file).isDirectory()) file=join(file,'index.html');
  const data=readFileSync(file);
  res.writeHead(200,{'Content-Type':types[extname(file)]||'application/octet-stream',
                    'Cache-Control':'no-store'}).end(data);
 } catch {res.writeHead(404).end();}
});
await new Promise(ok=>server.listen(0,'127.0.0.1',ok));
const candidates=[process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH,process.env.CHROME_PATH,
 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
 'C:/Program Files/Google/Chrome/Application/chrome.exe',
 '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
 ...(process.env.PATH||'').split(delimiter).flatMap(p=>['google-chrome','google-chrome-stable',
    'chromium','chromium-browser','msedge.exe'].map(n=>join(p,n)))];
const executablePath=candidates.find(p=>p&&existsSync(p));
assert(executablePath,'Install Chromium or set PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH.');
const browser=await chromium.launch({executablePath,headless:true});
const labs=[
 {id:'rotation',name:'u04_paraboloidna_povrsina.ipynb',slider:0},
 {id:'venturi',name:'u09_venturi.ipynb',slider:1},
 {id:'poiseuille',name:'u12_poiseuille_konvergencija.ipynb',slider:3},
];
const issues=[];
const errorSelector='.jp-OutputArea-error,[data-mime-type="application/vnd.jupyter.error"]';
try {
 for (const lab of labs) {
  const context=await browser.newContext({viewport:{width:1280,height:1000},reducedMotion:'reduce'});
  const page=await context.newPage();
  page.setDefaultTimeout(30000);
  const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  try {
   await page.goto(`http://127.0.0.1:${server.address().port}/jlite/lab/index.html?path=${lab.name}`);
   await page.waitForFunction(()=>/Python \(Pyodide\)[\s\S]*\bIdle\b/.test(document.body.innerText),
                             null,{timeout:180000});
   await page.getByRole('menuitem',{name:'Run',exact:true}).click();
   await page.getByRole('menuitem',{name:'Run All Cells',exact:true}).click();
   console.log(`${lab.id}: executing notebook in Pyodide`);
   await page.locator('.jp-WindowedPanel-outer').evaluateAll(items=>items.forEach(e=>e.scrollTop=0));
   await page.waitForFunction(()=>document.querySelector('.mf1-lab') ||
       document.querySelector('[data-mime-type="application/vnd.jupyter.error"]'),null,{timeout:180000});
   assert.equal(await page.locator(errorSelector).count(),0,
       await page.locator(errorSelector).allTextContents());
   const root=page.locator('.mf1-lab-'+lab.id).first();
   await root.waitFor({state:'visible',timeout:180000});
   const status=root.locator('.mf1-lab-status');
   await status.waitFor({timeout:180000});
   await page.waitForFunction(()=>/Python \(Pyodide\)[\s\S]*\bIdle\b/.test(document.body.innerText),
                             null,{timeout:180000});
   assert.equal(await page.locator(errorSelector).count(),0,'Notebook execution error');
   assert.equal(await status.getAttribute('data-state'),'ok');
   const initial=await status.innerText();
   await root.getByRole('button',{name:'Spremi A',exact:true}).click();
   await root.getByText(/^A:/).waitFor();
   const slider=root.getByRole('slider').nth(lab.slider);
   await slider.focus();
   let revision=await status.getAttribute('data-revision');
   await slider.press('ArrowRight');
   await page.waitForFunction(({id,revision})=>document.querySelector(`.mf1-lab-${id} .mf1-lab-status`)
       ?.dataset.revision!==revision,{id:lab.id,revision});
   assert.notEqual(await status.innerText(),initial,'Slider did not change the physical result');
   await root.getByRole('tab',{name:'Provjeri',exact:true}).click();
   assert((await root.locator('table:visible').count())>=2,'Missing diagnostic table');
   await root.getByRole('tab',{name:'Pogledaj kod',exact:true}).click();
   assert((await root.locator('pre:visible').innerText()).includes('def '),'Missing actual model code');
   await root.getByRole('button',{name:'Početno stanje',exact:true}).click();
   await page.waitForFunction(({id,text})=>document.querySelector(`.mf1-lab-${id} .mf1-lab-status`)
       ?.innerText===text,{id:lab.id,text:initial});
   assert.equal(await root.getByText(/^A:/).count(),0,'Reset kept a stale comparison');
   await root.getByRole('tab',{name:'Istraži',exact:true}).click();
   await page.waitForFunction(()=>document.body.innerText.includes('Python (Pyodide) | Idle'));
   await root.scrollIntoViewIfNeeded();
   await page.screenshot({path:join(snapshots,lab.id+'-desktop.png')});
   // The notebook introduction explains this standard JupyterLab mobile action.
   await page.locator('.lm-TabBar-tab[data-id="filebrowser"]').click();
   for (const width of [768,320]) {
    await page.setViewportSize({width,height:1000});
    await root.scrollIntoViewIfNeeded();
    const geometry=await root.evaluate(element=>({width:element.clientWidth,scroll:element.scrollWidth,
      truncatedTabs:[...element.querySelectorAll('.lm-TabBar-tabLabel')]
        .filter(e=>e.scrollWidth>e.clientWidth+2 || e.scrollHeight>e.clientHeight+2).map(e=>e.textContent),
      clipped:[...element.querySelectorAll('button,input,select,[role="slider"],[role="tab"]')]
       .filter(e=>e.getBoundingClientRect().width>0 && e.getBoundingClientRect().right>
         element.getBoundingClientRect().right+2).map(e=>e.textContent)}));
    assert(geometry.scroll<=geometry.width+2,`Lab overflow at ${width}px: ${JSON.stringify(geometry)}`);
    assert.equal(geometry.clipped.length,0,`Clipped controls at ${width}px`);
    assert.deepEqual(geometry.truncatedTabs,[],`Truncated tab labels at ${width}px`);
    await page.screenshot({path:join(snapshots,`${lab.id}-${width}.png`)});
   }
   assert.deepEqual(errors,[],'Browser JavaScript errors');
   console.log(`PASS ${lab.name}: execute, keyboard, physical response, comparison, reset, diagnostics, code, 320/768/1280px`);
  } catch(error) {
   issues.push(`${lab.name}: ${error.message}`);
   await page.screenshot({path:join(snapshots,lab.id+'-failure.png')}).catch(()=>{});
   console.error(issues.at(-1));
   console.error((await page.locator('body').innerText()).slice(-2200));
  } finally {await context.close();}
 }
} finally {await browser.close();await new Promise(ok=>server.close(ok));}
if(issues.length) {console.error(issues.join('\n'));process.exitCode=1;}
else console.log('Interactive laboratory audit PASS: 3 actual Pyodide notebooks and 9 layouts.');
