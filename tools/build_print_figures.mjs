/** Print-only composition. Canonical SVGs and their physical geometry are immutable. */
import { createHash } from 'node:crypto';
import { existsSync, readFileSync, writeFileSync, mkdirSync, readdirSync, unlinkSync } from 'node:fs';
import { delimiter, dirname, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright-core';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const layouts = JSON.parse(readFileSync(join(root, 'assets/print-layouts.json'), 'utf8'));
const tokens = JSON.parse(readFileSync(join(root, 'assets/figure-tokens.json'), 'utf8'));
const compositions = JSON.parse(readFileSync(join(root, 'assets/figure-compositions.json'), 'utf8'));
const out = join(root, 'assets/pdf-figures');
mkdirSync(out, { recursive: true });
const candidates = [process.env.CHROME_PATH, process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH,
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ...(process.env.PATH || '').split(delimiter).flatMap(p =>
    ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser'].map(n => join(p,n)))];
const executablePath = candidates.find(p => p && existsSync(p));
if (!executablePath) throw Error('Chrome/Edge required; set CHROME_PATH.');
const browser = await chromium.launch({ executablePath, headless: true });
const inputs=['tools/build_print_figures.mjs','assets/figure-tokens.json','assets/figure-compositions.json','assets/print-layouts.json'];
const manifest = { version: 2, inputs:Object.fromEntries(inputs.map(file=>[file,createHash('sha256').update(readFileSync(join(root,file),'utf8').replace(/\r\n/g,'\n')).digest('hex')])),tokens, figures: {} };
try {
  const page = await browser.newPage();
  for (const [name, layout] of Object.entries(layouts)) {
    if (process.argv[2] && !name.includes(process.argv[2])) continue;
    const sourcePath = join(root, 'assets/print', name);
    const source = readFileSync(sourcePath, 'utf8').replace(/\r\n/g, '\n');
    const sourceHash = createHash('sha1').update(source).digest('hex');
    if (sourceHash !== layout.source_sha1) throw Error(`${name}: review source panel mapping first`);
    await page.goto(pathToFileURL(sourcePath).href);
    await page.evaluate(() => document.fonts.ready);
    const result = await page.evaluate(({ layout, tokens, name, recipe }) => {
      const ns = 'http://www.w3.org/2000/svg';
      const sourceSvg = document.querySelector('svg');
      const inv = sourceSvg.getScreenCTM().inverse();
      const view = sourceSvg.viewBox.baseVal;
      const esc = s => String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
      const round = n => Math.round(n*1000)/1000;
      const contains = (a,b,pad=0.5) => a[0]-pad<=b[0] && a[1]-pad<=b[1] && a[2]+pad>=b[2] && a[3]+pad>=b[3];
      const bounds = list => list.length ? [Math.min(...list.map(e=>e.box[0])), Math.min(...list.map(e=>e.box[1])),
        Math.max(...list.map(e=>e.box[2])), Math.max(...list.map(e=>e.box[3]))] : [0,0,0,0];
      let textIndex=0;
      const ink = [...sourceSvg.querySelectorAll('text,path,rect,line,polyline,polygon,circle,ellipse')]
        .filter(e=>!e.closest('defs')).map((e,i)=>{
          const b=e.getBBox(), m=inv.multiply(e.getScreenCTM()), c=getComputedStyle(e);
          const points=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]]
            .map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));
          const p=new DOMPoint(parseFloat(e.getAttribute('x')||0),parseFloat(e.getAttribute('y')||0)).matrixTransform(m);
          return {e, index:i, textIndex:e.tagName==='text'?++textIndex:null, tag:e.tagName,
            text:e.textContent.replace(/\s+/g,' ').trim(), font:parseFloat(c.fontSize), weight:c.fontWeight,
            fill:c.fill, stroke:c.stroke, strokeWidth:parseFloat(c.strokeWidth), anchor:c.textAnchor,
            rx:Number(e.getAttribute('rx')||0), matrix:[m.a,m.b,m.c,m.d,m.e,m.f], origin:[p.x,p.y],
            box:[Math.min(...points.map(p=>p.x)),Math.min(...points.map(p=>p.y)),Math.max(...points.map(p=>p.x)),Math.max(...points.map(p=>p.y))]};
        });
      const neutral=new Set(['#dce7f0','#d4e3f0','#cbd5e1','#e2e8f0','#c7d4dd','#cbdce9','#c8d6e4','#cfd8df']);
      const noteFills=new Set(['#fde8e8','#fdf2e9','#f5f1fa','#fef9e7','#fdf6ec']);
      const decorations=new Set();
      for(const e of ink){
        if(e.e.getAttribute('data-mf1-role')==='physical')continue;
        const b=e.box,w=b[2]-b[0],h=b[3]-b[1], raw=e.e.getAttribute('stroke');
        const canvas=e.tag==='rect' && b[0]<=20 && b[1]<=20 && b[2]>=view.width-20 && b[3]>=view.height-20;
        const card=e.tag==='rect' && ((neutral.has(raw) && (e.rx>0 || w>200))
          || (e.rx>=4&&noteFills.has(e.e.getAttribute('fill')))
          || (e.rx>=4 && (['white','#fff','#ffffff'].includes(e.e.getAttribute('fill'))
            || Number(e.e.getAttribute('stroke-opacity')||1)<.8)));
        const header=e.tag==='rect' && h<=54 && w>200 && (['white','#fff','#ffffff'].includes(e.e.getAttribute('fill')) || /hdr/.test(e.e.getAttribute('fill')||''));
        const divider=e.tag==='line' && neutral.has(raw);
        const rail=e.tag==='rect' && e.rx>=2 && w<=6 && h>=28;
        if(canvas||card||header||divider||rail) decorations.add(e.index);
      }
      // Notes/badges have no physical ink inside. Never remove vessel walls,
      // fluid fills, axes, dimension lines, or a connected flowchart node.
      for(const e of ink){
        if(decorations.has(e.index) || e.e.getAttribute('data-mf1-role')==='physical' || !['rect','circle'].includes(e.tag))continue;
        const inside=ink.filter(t=>t.index!==e.index && contains(e.box,t.box,1));
        const texts=inside.filter(t=>t.tag==='text' && t.text);
        const physical=inside.filter(t=>t.tag!=='text'&&!decorations.has(t.index));
        const embedded=ink.some(parent=>parent.index!==e.index&&!decorations.has(parent.index)&&parent.tag!=='text'
          &&['rect','polygon','path'].includes(parent.tag)&&contains(parent.box,e.box)
          && (parent.box[2]-parent.box[0])*(parent.box[3]-parent.box[1])>(e.box[2]-e.box[0])*(e.box[3]-e.box[1])*1.1);
        if(texts.length && !physical.length && !embedded && (e.rx>0 || (e.tag==='circle'&&texts.every(t=>/^Z[1-6]$/.test(t.text)))))
          decorations.add(e.index);
      }
      for(const box of ink.filter(e=>e.tag==='rect'&&decorations.has(e.index))){
        const inside=ink.filter(e=>e.index!==box.index&&e.tag!=='text'&&!decorations.has(e.index)&&contains(box.box,e.box));
        if(inside.length&&inside.every(e=>e.tag==='line'&&Math.abs(e.box[2]-e.box[0])<2))
          inside.forEach(e=>decorations.add(e.index));
      }
      // Matrix grid lines carry mathematical relationships, unlike card rules.
      // They and their cell labels must retain the common affine transform.
      const tableInk=new Set();
      if(recipe.preserve_table){
        for(const e of ink)if(e.box[0]>=59&&e.box[2]<=841&&e.box[1]>=77&&e.box[3]<=239){
          decorations.delete(e.index);tableInk.add(e.index);
        }
      }
      const notes=new Set([...(layout.before||[]),...(layout.after||[])]);
      const defs=[...sourceSvg.querySelectorAll('defs')].map(e=>e.innerHTML).join('\n');
      const W=tokens['text-width-pt'], gap=tokens['figure-gap'], pad=tokens['figure-padding'];
      const font=tokens['figure-label-size'], small=tokens['figure-small-label-size'], lh=tokens['figure-line-height'];
      const canvas=document.createElementNS('http://www.w3.org/1999/xhtml','canvas'),ctx=canvas.getContext('2d');
      function measure(s, size, bold=false){ctx.font=`${bold?'600':'400'} ${size}px Arial`; return ctx.measureText(s).width;}
      function wrap(s,max,size,bold=false){
        const words=s.split(/\s+/), lines=[];let line='';
        for(const word of words){if(line && measure(line+' '+word,size,bold)>max){lines.push(line);line=word;}else line+=(line?' ':'')+word;}
        if(line)lines.push(line);return lines;
      }
      const rgbWhite = c => /^(white|#fff(?:fff)?|rgb\(255, 255, 255\))$/.test(c);
      const probe=document.createElementNS(ns,'g');probe.setAttribute('font-family',tokens['figure-font-family']);sourceSvg.append(probe);
      const labelCache=new Map();
      function label(e,x,y,width,align='middle', size=font){
        const bold=Number(e.weight)>=600, lines=wrap(e.text,width,size,bold);
        const fill=rgbWhite(e.fill)?'#3a4a56':e.fill;
        const key=JSON.stringify([e.textIndex,size,align,lines]);
        if(!labelCache.has(key)){
          // Carry each mathematical run through line wrapping. In particular,
          // p_A, g_eff, powers and vector weight/italic must not become plain text.
          const chars=[];
          const walk=(node,attrs='')=>{
            if(node.nodeType===3){
              for(const ch of node.textContent){const c=/\s/.test(ch)?' ':ch;if(c===' '&&(!chars.length||chars.at(-1).c===' '))continue;chars.push({c,attrs});}
            }else{
              let next=attrs;
              if(node.tagName==='tspan'){
                const c=getComputedStyle(node),shift=node.getAttribute('baseline-shift');
                next=` font-size="${small}" font-weight="${c.fontWeight}" font-style="${c.fontStyle}" fill="${esc(rgbWhite(c.fill)?'#3a4a56':c.fill)}"`;
                if(shift==='sub'||shift==='super')next+=` baseline-shift="${shift==='sub'?-2:2}"`;
              }
              for(const child of node.childNodes)walk(child,next);
            }
          };
          walk(e.e);if(chars.at(-1)?.c===' ')chars.pop();
          let offset=0;
          let base=lines.map((line,i)=>{
            const range=chars.slice(offset,offset+line.length);offset+=line.length+1;
            let html='';for(let j=0;j<range.length;){let k=j+1;while(k<range.length&&range[k].attrs===range[j].attrs)k++;
              const value=esc(range.slice(j,k).map(c=>c.c).join(''));html+=range[j].attrs?`<tspan${range[j].attrs}>${value}</tspan>`:value;j=k;}
            return `<text data-source-text="${e.textIndex}" x="0" y="${i*lh}" text-anchor="${align}" font-size="${size}" font-weight="${bold?600:400}" fill="${esc(fill)}">${html}</text>`;
          }).join('\n');
          const angle=Math.atan2(e.matrix[1],e.matrix[0])*180/Math.PI;
          if(Math.abs(angle)>.01)base=`<g transform="rotate(${round(angle)})">${base}</g>`;
          probe.innerHTML=base;const b=probe.getBBox();
          labelCache.set(key,{base,box:[b.x,b.y,b.x+b.width,b.y+b.height],height:Math.max(lines.length*lh,b.height)});
        }
        const cached=labelCache.get(key);
        return {xml:`<g transform="translate(${round(x)} ${round(y)})">${cached.base}</g>`,
          box:[cached.box[0]+x,cached.box[1]+y,cached.box[2]+x,cached.box[3]+y],height:cached.height};
      }
      const assignments=layout.panels.map(()=>[]),globalNotes=[];
      for(const e of ink){
        if(decorations.has(e.index) || (e.tag==='text'&&!e.text))continue;
        if(notes.has(e.textIndex)){globalNotes.push(e);continue;}
        const choices=layout.panels.map((p,i)=>({i,p,inside:contains([p[0],p[1],p[0]+p[2],p[1]+p[3]],e.box,2)})).filter(p=>p.inside);
        if(!choices.length)throw Error(`${name}: unassigned ${e.tag} ${e.text||e.index}`);
        assignments[choices[0].i].push(e);
      }
      for(const items of assignments){
        const shapes=items.filter(e=>e.tag!=='text');
        const rail=e=>(e.tag==='line'||e.tag==='rect')&&e.box[2]-e.box[0]<=6&&e.box[3]-e.box[1]>=20
          &&!e.e.hasAttribute('marker-end')&&!e.e.hasAttribute('marker-start');
        if(shapes.length&&shapes.every(rail)){
          shapes.forEach(e=>decorations.add(e.index));
          for(let i=items.length-1;i>=0;i--)if(decorations.has(items[i].index))items.splice(i,1);
        }
      }
      function compose(elements, width, index){
        const geometries=elements.filter(e=>e.tag!=='text'), texts=elements.filter(e=>e.tag==='text');
        const gb=bounds(geometries), hasGeometry=geometries.length>0;
        const tops=[], bottoms=[], spatial=[];
        for(const t of texts){
          // Labels over separate vessels and ticks under an axis are spatial
          // content. Preserve their association instead of turning them into a
          // stack of headings/footnotes simply because they lie outside the ink.
          const peer=texts.some(other=>other!==t&&Math.abs(other.origin[1]-t.origin[1])<4
            &&Math.abs(other.origin[0]-t.origin[0])>(gb[2]-gb[0])*.15
            &&!/^Z[1-6]$/.test(other.text)&&!/^Z[1-6]$/.test(t.text));
          if(recipe.spatial_text?.includes(t.textIndex))spatial.push(t);
          else if(recipe.header_text?.includes(t.textIndex))tops.push(t);
          else if(recipe.footer_text?.includes(t.textIndex))bottoms.push(t);
          else if(tableInk.has(t.index)||(hasGeometry&&peer))spatial.push(t);
          else if(!hasGeometry || t.box[3]<gb[1]+1)tops.push(t);
          else if(t.box[1]>gb[3]-1)bottoms.push(t);
          else if(t.text.split(/\s+/).length>=9 && t.box[1]>(gb[1]+gb[3])/2)bottoms.push(t);
          else spatial.push(t);
        }
        const sort=(a,b)=>Math.abs(a.box[1]-b.box[1])<5?a.box[0]-b.box[0]:a.box[1]-b.box[1];
        tops.sort(sort);bottoms.sort(sort);
        // Join adjacent badge and heading; keep the original words and order.
        let y=pad,xml='', placed=[], conflicts=0;
        for(let i=0;i<tops.length;i++){
          let t=tops[i];
          // A table is a relation between rows and columns, not a list of labels.
          const table=recipe.text_tables?.find(ids=>ids.includes(t.textIndex));
          if(table){
            const cells=tops.filter(e=>table.includes(e.textIndex));
            if(t!==cells[0])continue;
            const xs=[...new Set(cells.map(e=>e.origin[0]))].sort((a,b)=>a-b);
            const ys=[...new Set(cells.map(e=>e.origin[1]))].sort((a,b)=>a-b);
            const cw=(width-2*pad)/xs.length;
            for(const sy of ys){
              let height=lh;
              for(const cell of cells.filter(e=>e.origin[1]===sy)){
                const l=label(cell,pad+(xs.indexOf(cell.origin[0])+.5)*cw,y+font,cw-4,'middle');
                xml+=l.xml;placed.push(l);height=Math.max(height,l.height);
              }
              y+=height+3;
            }
            continue;
          }
          if(/^Z[1-6]$/.test(t.text)&&tops[i+1]&&Math.abs(t.box[1]-tops[i+1].box[1])<6){
            const b=tops[++i]; const a=label(t,pad,y+font,24,'start'); const l=label(b,28,y+font,width-32,'start');
            xml+=a.xml+l.xml;placed.push(a,l);y+=Math.max(a.height,l.height)+3;continue;
          }
          const l=label(t,width/2,y+font,width-2*pad,'middle',t.font<=11?small:font);
          xml+=l.xml;placed.push(l);y+=l.height+3;
        }
        if(hasGeometry){
          const all=bounds([...geometries,...spatial]);
          const inset=recipe.canvas_insets_pt?.[String(index)]||{};
          const left=inset.left||0,right=inset.right||0;
          const scale=Math.min(.9,(width-2*pad-left-right)/(all[2]-all[0]));
          const gx=left+(width-left-right-scale*(all[2]-all[0]))/2-scale*all[0];
          const gy=y+(inset.top||0)-scale*all[1];
          for(const g of geometries){
            const clone=g.e.cloneNode(true);clone.removeAttribute('transform');clone.removeAttribute('id');
            for(const prop of ['fill','stroke','stroke-width','stroke-linecap','stroke-linejoin','stroke-dasharray','fill-opacity','stroke-opacity','opacity','marker-start','marker-mid','marker-end']){
              let value=getComputedStyle(g.e).getPropertyValue(prop).replace(/url\(["']?[^)#]*#([^)'" ]+)["']?\)/g,'url(#$1)');
              if(value)clone.setAttribute(prop,value);
            }
            // Thin ink gets a physical print weight; structural wide strokes
            // (pipe bodies, white masks) retain their exact proportions.
            const physicalScale=scale*Math.hypot(g.matrix[0],g.matrix[1]);
            if(g.strokeWidth>0&&g.strokeWidth<=3&&g.stroke!=='none')clone.setAttribute('stroke-width',round(Math.max(.5,tokens['figure-stroke']*g.strokeWidth/1.2)/physicalScale));
            if(tableInk.has(g.index)&&g.tag==='rect'){clone.setAttribute('rx','0');clone.setAttribute('fill','none');}
            for(const attr of ['marker-start','marker-mid','marker-end']){
              const id=clone.getAttribute(attr)?.match(/url\(#([^)]*)\)/)?.[1];
              const original=id&&sourceSvg.querySelector(`[id="${id}"]`);
              if(!original)continue;
              const marker=original.cloneNode(true),id2=`${id}-print-${index}-${g.index}-${attr}`;
              const mw=Number(marker.getAttribute('markerWidth')||3),mh=Number(marker.getAttribute('markerHeight')||3);
              if(!marker.hasAttribute('viewBox'))marker.setAttribute('viewBox',`0 0 ${mw} ${mh}`);
              marker.setAttribute('id',id2);marker.setAttribute('markerUnits','userSpaceOnUse');
              marker.setAttribute('markerWidth',round(tokens['figure-arrow-size']*mw/Math.max(mw,mh)/physicalScale));
              marker.setAttribute('markerHeight',round(tokens['figure-arrow-size']*mh/Math.max(mw,mh)/physicalScale));
              clone.setAttribute(attr,`url(#${id2})`);xml+=`<defs>${marker.outerHTML}</defs>`;
            }
            clone.setAttribute('data-source-geometry',g.index);
            xml+=`<g transform="translate(${round(gx)} ${round(gy)}) scale(${round(scale)})"><g transform="matrix(${g.matrix.map(round).join(' ')})">${clone.outerHTML}</g></g>`;
          }
          let bottom=gy+all[3]*scale+(inset.bottom||0);
          for(const t of spatial.sort((a,b)=>a.box[1]-b.box[1])){
            let x=gx+t.origin[0]*scale, yy=gy+t.origin[1]*scale;
            const anchor=['start','middle','end'].includes(t.anchor)?t.anchor:'start';
            // Give spatial labels their original centre, with a consistent
            // physical font independent of the geometry's scale.
            if(Math.abs(t.matrix[1])<.001){
              if(anchor==='start')x=gx+t.box[0]*scale;
              if(anchor==='end')x=gx+t.box[2]*scale;
            }
            const offset=recipe.text_offsets_pt?.[String(t.textIndex)]||[0,0];x+=offset[0];yy+=offset[1];
            const size=t.font<=11?small:font;
            // Short symbols and dimensions stay intact; notes may wrap.
            const available=t.text.length<24?width-2*pad:Math.max(65,anchor==='middle'?2*Math.min(x-pad,width-pad-x):anchor==='start'?width-pad-x:x-pad);
            let l=label(t,x,yy,available,anchor,size);
            if(l.box[0]<pad)x+=pad-l.box[0];
            if(l.box[2]>width-pad)x-=l.box[2]-(width-pad);
            l=label(t,x,yy,available,anchor,size);
            const overlaps=(a,b)=>a[0]<b[2]+1&&b[0]<a[2]+1&&a[1]<b[3]+1&&b[1]<a[3]+1;
            const good=l=>l.box[0]>=0&&l.box[2]<=width&&!placed.some(p=>overlaps(l.box,p.box));
            if(!good(l)&&!tableInk.has(t.index)){
              const candidates=[];
              for(const dy of [0,-3,3,-6,6,-9,9,-12,12])for(const dx of [0,-3,3,-6,6,-9,9,-12,12])
                candidates.push({dx,dy,cost:Math.abs(dx)+Math.abs(dy)*1.1});
              candidates.sort((a,b)=>a.cost-b.cost);
              const fit=candidates.map(d=>({...d,l:label(t,x+d.dx,yy+d.dy,available,anchor,size)})).find(d=>good(d.l)&&d.l.box[1]>=y-1);
              if(fit)l=fit.l;else conflicts++;
            }
            xml+=l.xml;placed.push({text:t.text,...l,source:t.textIndex});bottom=Math.max(bottom,l.box[3]);
          }
          y=bottom+7;
        }
        for(let i=0;i<bottoms.length;i++){
          const t=bottoms[i],next=bottoms[i+1];
          if(next&&Math.abs(t.box[1]-next.box[1])<4){
            const a=label(t,width/4,y+font,width/2-2*pad,'middle',small);
            const b=label(next,3*width/4,y+font,width/2-2*pad,'middle',small);
            xml+=a.xml+b.xml;y+=Math.max(a.height,b.height)+3;i++;
          }else{const l=label(t,width/2,y+font,width-2*pad,'middle',small);xml+=l.xml;y+=l.height+3;}
        }
        return {width,height:y+pad,xml,placed,conflicts,kind:width<=W*.4?'mini':width<W*.55?'subfigure':width<=W*.7?'standard':'wide',geometry:geometries.map(e=>e.index),texts:texts.map(e=>e.textIndex),panel:index};
      }
      // Related original panels form a single logical composite. A two-column
      // grid is the default; each cell is independently typeset at 9–9.5 pt.
      const panels=[];
      const rows=[];
      const noteRows=where=>{
        const wanted=new Set(layout[where]||[]),items=globalNotes.filter(e=>wanted.has(e.textIndex));
        if(items.length)rows.push(compose(items,W,-1));
      };
      noteRows('before');
      // Three related overview panels need not occupy two tall rows. Try a
      // horizontal triptych at the same physical label size, accepting it only
      // when all spatial labels fit without conflicts.
      const triptych=assignments.length===3&&!recipe.rows
        ?assignments.map((items,i)=>compose(items,(W-2*gap)/3,i)):null;
      if(triptych?.every(p=>!p.conflicts)){
        let xx=0,xml='';for(const cell of triptych){xml+=`<g transform="translate(${round(xx)} 0)">${cell.xml}</g>`;xx+=cell.width+gap;panels.push(cell);}
        rows.push({width:W,height:Math.max(...triptych.map(c=>c.height)),xml,panels:[0,1,2]});
      }
      for(let i=panels.length?assignments.length:0;i<assignments.length;){
        const single=width=>compose(assignments[i],width,i);
        let pair=null;
        if(recipe.rows){
          for(const row of recipe.rows){
            const cells=row.map(kind=>compose(assignments[i],W*tokens[`figure-${kind}-width`],i++));
            let xx=0,xml='';for(const cell of cells){xml+=`<g transform="translate(${round(xx)} 0)">${cell.xml}</g>`;xx+=cell.width+gap;panels.push(cell);}
            rows.push({width:xx-gap,height:Math.max(...cells.map(c=>c.height)),xml,panels:cells.map(c=>c.panel)});
          }
          break;
        }
        if(i+1<assignments.length){
          const mini=W*tokens['figure-mini-width'],standard=W*tokens['figure-standard-width'];
          for(const widths of [[(W-gap)/2,(W-gap)/2],[standard,mini],[mini,standard]]){
            const a=single(widths[0]),b=compose(assignments[i+1],widths[1],i+1);
            if(a.conflicts+b.conflicts===0){pair=[a,b];break;}
          }
        }
        if(pair){const[a,b]=pair;panels.push(a,b);rows.push({width:a.width+gap+b.width,height:Math.max(a.height,b.height),xml:a.xml+`<g transform="translate(${round(a.width+gap)} 0)">${b.xml}</g>`,panels:[i,i+1]});i+=2;}
        else{
          const choices=[W*tokens['figure-mini-width'],W*tokens['figure-standard-width'],W*tokens['figure-wide-width']].map(single);
          // Mini is reserved for genuinely simple diagrams. Dense or broad
          // systems get a standard/wide canvas without shrinking their labels.
          const a=choices.find((p,j)=>!p.conflicts&&(j>0||(p.geometry.length<=15&&p.texts.length<=10)))||choices[2];
          panels.push(a);rows.push({...a,panels:[i]});i++;
        }
      }
      noteRows('after');
      const captionPanel=recipe.caption_anchor_panel??assignments.length-1;
      const captionRow=rows.findIndex(r=>r.panels?.includes(captionPanel));
      const svgRows=rows.map((r,i)=>({width:round(r.width),height:round(r.height),panels:r.panels||[],
        keep_with_next:!r.panels?.length||i>=captionRow,
        svg:`<svg xmlns="${ns}" width="${round(r.width)}pt" height="${round(r.height)}pt" viewBox="0 0 ${round(r.width)} ${round(r.height)}" role="img"><title>${esc(sourceSvg.querySelector('title')?.textContent||name)}</title><defs>${defs}</defs><g font-family="${tokens['figure-font-family']}">${r.xml}</g></svg>\n`}));
      return {rows:svgRows,kind:panels.length>1?'composite':panels[0].kind,
        triptych_conflicts:triptych?.map(p=>p.conflicts)||null,
        source_text_count:ink.filter(e=>e.tag==='text'&&e.text).length,
        source_geometry_count:ink.filter(e=>e.tag!=='text').length,
        removed_decorations:[...decorations],panels:panels.map(p=>({width:p.width,height:p.height,kind:p.kind,conflicts:p.conflicts,geometry:p.geometry,texts:p.texts}))};
    }, { layout, tokens, name, recipe:compositions[name]||{} });
    const rows=result.rows.map((r,i)=>{
      r.svg=r.svg.replace(/[ \t]+$/gm,'');
      const file=name.replace('.svg',`--${i+1}.svg`);writeFileSync(join(out,file),r.svg);
      return {file,width:r.width,height:r.height,panels:r.panels,keep_with_next:r.keep_with_next,sha256:createHash('sha256').update(r.svg).digest('hex')};
    });
    manifest.figures[name]={...result,rows,source_sha1:sourceHash};
    console.log(`${name}: ${result.kind}, ${rows.length} rows, ${rows.reduce((s,r)=>s+r.height,0).toFixed(0)} pt`);
  }
}finally{await browser.close();}
writeFileSync(join(out, process.argv[2]?'preview-manifest.json':'manifest.json'),JSON.stringify(manifest,null,2)+'\n');
if(!process.argv[2]){
  if(existsSync(join(out,'preview-manifest.json')))unlinkSync(join(out,'preview-manifest.json'));
  const current=new Set(Object.values(manifest.figures).flatMap(f=>f.rows.map(r=>r.file)));
  for(const file of readdirSync(out))if(/--\d+\.svg$/.test(file)&&!current.has(file))unlinkSync(join(out,file));
  const css=Object.entries(tokens).filter(([key])=>key.startsWith('figure-')).map(([key,value])=>{
    const rendered=key.endsWith('-width')?`${Math.round(value*100)}%`:typeof value==='number'?`${value}pt`:value;
    return `    --${key}: ${rendered};`;
  }).join('\n');
  writeFileSync(join(out,'tokens.css'),`/* Generated from assets/figure-tokens.json. */\n@media print {\n  :root {\n${css}\n  }\n}\n`);
}
