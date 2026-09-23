/** Verify screen/print separation and unscaled, fully loaded print canvases. */
import {createServer} from 'node:http';
import {readFileSync,existsSync,readdirSync,statSync} from 'node:fs';
import {resolve,join,extname,delimiter} from 'node:path';
import {chromium} from 'playwright-core';
const site=resolve(process.argv[2]||'_site');
const types={'.html':'text/html','.css':'text/css','.js':'application/javascript','.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2'};
const server=createServer((req,res)=>{
 const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
 const file=resolve(site,'.'+pathname);
 if(!file.startsWith(site)||!existsSync(file)||!statSync(file).isFile()){res.writeHead(404);res.end();return;}
 res.setHeader('Content-Type',types[extname(file)]||'application/octet-stream');res.end(readFileSync(file));
});
await new Promise(ok=>server.listen(0,'127.0.0.1',ok));
const candidates=[process.env.CHROME_PATH,process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH,
 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
 '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
 ...(process.env.PATH||'').split(delimiter).flatMap(p=>['google-chrome','google-chrome-stable','chromium','chromium-browser'].map(n=>join(p,n)))];
const browser=await chromium.launch({executablePath:candidates.find(p=>p&&existsSync(p)),headless:true});
const issues=[];let figures=0,rows=0;
try{
 const page=await browser.newPage({viewport:{width:794,height:1123}});
 for(const file of readdirSync(join(site,'chapters')).filter(n=>n.endsWith('.html'))){
  await page.emulateMedia({media:'screen'});
  await page.goto(`http://127.0.0.1:${server.address().port}/chapters/${file}`,{waitUntil:'networkidle'});
  const screen=await page.evaluate(()=>{
   const images=[...document.querySelectorAll('img[data-mf1-print-layout]')];
   const missing=[...document.querySelectorAll('main figure img[src*="/print/"]')].some(i=>!i.dataset.mf1PrintLayout);
   return {count:images.length,bad:missing||images.some(i=>!i.getClientRects().length),printVisible:[...document.querySelectorAll('.mf1-print-figure')].some(e=>e.getClientRects().length)};
  });
  figures+=screen.count;
  if(screen.bad||screen.printVisible)issues.push(`${file}: print assets changed the screen view`);
  await page.emulateMedia({media:'print'});
  const print=await page.evaluate(()=>{
   const issues=[],originals=[...document.querySelectorAll('img[data-mf1-print-layout]')];let rows=0;
   for(const original of originals){
    if(original.getClientRects().length)issues.push('canonical screen SVG still printed');
    const group=(original.closest('.mf1-figure-link')||original).nextElementSibling;
    if(!group?.classList.contains('mf1-print-figure')){issues.push('missing print group');continue;}
    const expected=JSON.parse(original.dataset.mf1PrintLayout),images=[...group.querySelectorAll('img')];
    if(images.length!==expected.length)issues.push('wrong print row count');
    images.forEach((image,i)=>{rows++;const b=image.getBoundingClientRect(),r=expected[i];
     if(image.classList.contains('mf1-keep-with-next')!==r.keep_with_next)issues.push('missing print pagination constraint '+image.src);
     if(!image.complete||!image.naturalWidth)issues.push('missing print asset '+image.src);
     if(Math.abs(b.width*72/96-r.width)>.1||Math.abs(b.height*72/96-r.height)>.1)issues.push('print labels scaled by CSS '+image.src);
     if(b.left<-.5||b.right>innerWidth+.5)issues.push('print row overflows page '+image.src);
    });
   }return {issues,rows};
  });
  rows+=print.rows;issues.push(...print.issues.map(s=>`${file}: ${s}`));
 }
}finally{await browser.close();server.close();}
if(figures<94)issues.push(`Only ${figures} screen figures found`);
if(issues.length){console.error(issues.join('\n'));process.exitCode=1;}
else console.log(`PASS: ${figures} unchanged screen figures; ${rows} loaded print rows at intrinsic point sizes.`);
