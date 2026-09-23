/** Audit the actual print artifacts, not just nominal scale settings. */
import { createHash } from 'node:crypto';
import { readFileSync, existsSync } from 'node:fs';
import { dirname, resolve, join, delimiter } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright-core';

const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const manifest=JSON.parse(readFileSync(join(root,'assets/pdf-figures/manifest.json'),'utf8'));
const tokenFile=JSON.parse(readFileSync(join(root,'assets/figure-tokens.json'),'utf8'));
const compositions=JSON.parse(readFileSync(join(root,'assets/figure-compositions.json'),'utf8'));
if(JSON.stringify(tokenFile)!==JSON.stringify(manifest.tokens))throw Error('Print tokens changed: rebuild figures.');
const expectedNames=Object.keys(JSON.parse(readFileSync(join(root,'assets/print-layouts.json'),'utf8'))).sort();
if(JSON.stringify(Object.keys(manifest.figures).sort())!==JSON.stringify(expectedNames))throw Error('Incomplete print figure inventory.');
const candidates=[process.env.CHROME_PATH,process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH,
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ...(process.env.PATH||'').split(delimiter).flatMap(p=>['google-chrome','google-chrome-stable','chromium','chromium-browser'].map(n=>join(p,n)))];
const executablePath=candidates.find(p=>p&&existsSync(p));
const browser=await chromium.launch({executablePath,headless:true});
const issues=[];let rowCount=0,textCount=0,geometryCount=0;
for(const [file,hash]of Object.entries(manifest.inputs||{})){
 const actual=createHash('sha256').update(readFileSync(join(root,file),'utf8').replace(/\r\n/g,'\n')).digest('hex');
 if(actual!==hash)issues.push(`${file}: changed layout input; regenerate print figures`);
}
const normalize=s=>s.replace(/\s+/g,' ').trim();
try{
 const page=await browser.newPage();
 for(const [name,figure]of Object.entries(manifest.figures)){
  const sourcePath=join(root,'assets/print',name);
  const source=readFileSync(sourcePath,'utf8').replace(/\r\n/g,'\n');
  if(createHash('sha1').update(source).digest('hex')!==figure.source_sha1)issues.push(`${name}: stale source hash`);
  await page.goto(pathToFileURL(sourcePath).href);
  const original=await page.evaluate(()=>{
   const elements=[...document.querySelectorAll('svg text,svg path,svg rect,svg line,svg polyline,svg polygon,svg circle,svg ellipse')].filter(e=>!e.closest('defs'));
   let ti=0;
   const keys=['d','points','x','y','x1','x2','y1','y2','width','height','cx','cy','r','rx','ry'];
   return elements.map((e,i)=>({i,tag:e.tagName,textIndex:e.tagName==='text'?++ti:null,text:e.textContent,
    shape:Object.fromEntries(keys.filter(k=>e.hasAttribute(k)).map(k=>[k,e.getAttribute(k)])),
    scripts:[...e.querySelectorAll('tspan[baseline-shift]')].map(t=>({shift:t.getAttribute('baseline-shift'),text:t.textContent.replace(/\s/g,'')}))}));
  });
  const texts=new Map(),scripts=new Map(),geometry=new Map();
  for(const row of figure.rows){
   rowCount++;
   const file=join(root,'assets/pdf-figures',row.file),svg=readFileSync(file,'utf8').replace(/\r\n/g,'\n');
   if(createHash('sha256').update(svg).digest('hex')!==row.sha256)issues.push(`${row.file}: edited generated artifact`);
   if(row.width>manifest.tokens['text-width-pt']+.01)issues.push(`${row.file}: wider than the text column`);
   await page.goto(pathToFileURL(file).href);await page.evaluate(()=>document.fonts.ready);
   const result=await page.evaluate(()=>{
    const svg=document.querySelector('svg'),v=svg.viewBox.baseVal,inv=svg.getScreenCTM().inverse();
    const box=e=>{const b=e.getBBox(),m=inv.multiply(e.getScreenCTM());const ps=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));return [Math.min(...ps.map(p=>p.x)),Math.min(...ps.map(p=>p.y)),Math.max(...ps.map(p=>p.x)),Math.max(...ps.map(p=>p.y))];};
    const texts=[...svg.querySelectorAll('text')].map(e=>({i:Number(e.dataset.sourceText),text:e.textContent,box:box(e),font:parseFloat(getComputedStyle(e).fontSize),
     sizes:[...e.querySelectorAll('tspan')].map(t=>parseFloat(getComputedStyle(t).fontSize)),
     scripts:[...e.querySelectorAll('tspan[baseline-shift]')].map(t=>({shift:t.getAttribute('baseline-shift'),text:t.textContent.replace(/\s/g,'')}))}));
    const keys=['d','points','x','y','x1','x2','y1','y2','width','height','cx','cy','r','rx','ry'];
    const geometry=[...svg.querySelectorAll('[data-source-geometry]')].map(e=>({i:Number(e.dataset.sourceGeometry),tag:e.tagName,box:box(e),
     shape:Object.fromEntries(keys.filter(k=>e.hasAttribute(k)).map(k=>[k,e.getAttribute(k)]))}));
    return {texts,geometry,width:v.width,height:v.height,ptWidth:svg.getAttribute('width'),ptHeight:svg.getAttribute('height')};
   });
   if(result.ptWidth!==`${row.width}pt`||result.ptHeight!==`${row.height}pt`)issues.push(`${row.file}: intrinsic print dimensions differ`);
   for(const t of result.texts){
    const list=texts.get(t.i)||[];list.push(t.text);texts.set(t.i,list);
    const ss=scripts.get(t.i)||[];ss.push(...t.scripts);scripts.set(t.i,ss);
    if(Math.min(t.font,...t.sizes)<manifest.tokens['figure-small-label-size']-.01)issues.push(`${row.file}: label ${t.i} below 9 pt`);
    if(t.box[0]<-.25||t.box[1]<-.25||t.box[2]>row.width+.25||t.box[3]>row.height+.25)issues.push(`${row.file}: clipped label ${t.i}: ${t.text}`);
   }
   for(let i=0;i<result.texts.length;i++)for(const b of result.texts.slice(i+1)){
    const a=result.texts[i],x=a.box,y=b.box;
    if(x[0]<y[2]-.5&&y[0]<x[2]-.5&&x[1]<y[3]-.5&&y[1]<x[3]-.5)issues.push(`${row.file}: overlapping labels ${a.i}/${b.i}`);
   }
   for(const ids of compositions[name]?.text_tables||[]){
    const cells=ids.map(id=>result.texts.find(t=>t.i===id));
    if(!cells.some(Boolean))continue;
    if(cells.some(t=>!t)){issues.push(`${row.file}: table cells split across rows`);continue;}
    // The reviewed jet-results table has four columns: h, v, t, x.
    for(let i=0;i<cells.length;i++){
     const a=cells[i].box,c=(a[0]+a[2])/2;
     if(i%4&&(!(c>(cells[i-1].box[0]+cells[i-1].box[2])/2)||Math.abs(a[1]-cells[i-1].box[1])>1))
      issues.push(`${row.file}: table column/row relationship lost at label ${ids[i]}`);
     if(i>=4&&(Math.abs(c-(cells[i-4].box[0]+cells[i-4].box[2])/2)>1||a[1]<=cells[i-4].box[3]))
      issues.push(`${row.file}: table value separated from its column ${ids[i]}`);
    }
   }
   for(const g of result.geometry){
    if(geometry.has(g.i))issues.push(`${row.file}: duplicated geometry ${g.i}`);geometry.set(g.i,g);
    if(g.box[0]<-.5||g.box[1]<-.5||g.box[2]>row.width+.5||g.box[3]>row.height+.5)issues.push(`${row.file}: clipped geometry ${g.i}`);
   }
  }
  const removed=new Set(figure.removed_decorations);
  const anchor=compositions[name]?.caption_anchor_panel??figure.panels.length-1;
  const anchorRow=figure.rows.findIndex(r=>r.panels.includes(anchor));
  if(anchorRow<0||figure.rows.some((r,i)=>r.keep_with_next!==(!r.panels.length||i>=anchorRow)))
   issues.push(`${name}: figure headings/legends are not bound to their diagram`);
  for(const e of original){
   if(e.tag==='text'){
    if(!normalize(e.text))continue;textCount++;
    if(normalize((texts.get(e.textIndex)||[]).join(' '))!==normalize(e.text))issues.push(`${name}: changed/missing text #${e.textIndex}`);
    for(const shift of ['sub','super']){
     const before=e.scripts.filter(s=>s.shift===shift).map(s=>s.text).join('');
     const after=(scripts.get(e.textIndex)||[]).filter(s=>s.shift===(shift==='sub'?'-2':'2')).map(s=>s.text).join('');
     if(before!==after)issues.push(`${name}: changed ${shift}script in #${e.textIndex}: ${before} / ${after}`);
    }
   }else if(!removed.has(e.i)){
    geometryCount++;const got=geometry.get(e.i);
    if(!got)issues.push(`${name}: missing physical geometry #${e.i}`);
    else for(const [k,value]of Object.entries(e.shape)){
     // Only the outline radius of the dimensional table is stylistic.
     if(k==='rx'&&name==='u14_fig_pi_buckingham.svg')continue;
     if(got.shape[k]!==value)issues.push(`${name}: changed geometric coordinate ${e.i}.${k}`);
    }
   }
  }
  for(const p of figure.panels)if(p.conflicts)issues.push(`${name}: unresolved composition conflict`);
 }
}finally{await browser.close();}
const oil=manifest.figures['u01_fig_gustoca_sr.svg'];
if(!oil.rows.some(r=>r.panels.includes(0)&&r.panels.includes(1)))issues.push('U01 oil/water comparison must share a horizontal row.');
if(issues.length){console.error(issues.join('\n'));process.exitCode=1;}
else console.log(`PASS: ${Object.keys(manifest.figures).length} print figures, ${rowCount} rows, ${textCount} unchanged labels, ${geometryCount} unchanged geometric elements; no overlaps or clipping, fonts >= 9 pt.`);
