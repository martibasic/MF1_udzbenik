-- HTML presentation of the shared component model; native math/figures remain Quarto objects.
if not FORMAT:match("html") then return {} end
local root=pandoc.path.directory(pandoc.path.directory(PANDOC_SCRIPT_FILE))
local function read_json(path)
  local file=assert(io.open(pandoc.path.join({root,path}),"r"))
  local data=pandoc.json.decode(file:read("*a"));file:close();return data
end
local components=dofile(pandoc.path.join({root,'filters/mf1-component-model.lua'}))(root)
local registry=components.registry
local model=read_json("assets/book-model.json")
local index=read_json("assets/content-index.json")
local collection=false
local function escape(value) return tostring(value):gsub('&','&amp;'):gsub('"','&quot;'):gsub('<','&lt;'):gsub('>','&gt;') end

local function catalog()
  local docs={};for _,doc in ipairs(model.documents) do docs[doc.id]=doc end
  local function role_path(role)
    for _,doc in ipairs(model.documents) do if doc.role==role then return doc.path:gsub('%.qmd$','.html') end end
    error('Missing document role: '..role)
  end
  local first=docs[model.parts[1].chapters[1]].path:gsub('%.qmd$','.html')
  local result={ '<nav class="mf1-print-toolbar" aria-label="Čitanje knjige"><a class="mf1-print-button primary" href="'..first..'">Počni s osnovama <span aria-hidden="true">→</span></a><a class="mf1-print-button secondary" href="downloads/'..model.book['output-file']..'.pdf">Preuzmi PDF</a></nav>',
    '<nav class="mf1-quick-links" aria-label="Brzi pristup"><a href="'..role_path('formulas')..'">Formule i oznake</a><a href="'..role_path('answers')..'">Rezultati zadataka</a><a href="jlite/lab/index.html">Numerički pokusi</a></nav>',
    '<nav class="mf1-book-catalog" aria-label="Sadržaj udžbenika">'}
  local function group(title,ids)
    table.insert(result,'<section><h2 class="mf1-section-title unnumbered">'..escape(title)..'</h2><div class="mf1-grid">')
    for _,id in ipairs(ids) do
      local doc=docs[id]
      table.insert(result,'<a class="mf1-card" href="'..escape(doc.path:gsub('%.qmd$','.html'))..'"><span class="mf1-card-code">'..doc.number..'</span><span class="mf1-card-title">'..escape(doc.catalog_title or doc.title)..'</span><span class="mf1-card-hint">'..(doc.description or '')..'</span></a>')
    end
    table.insert(result,'</div></section>')
  end
  local front,appendix={},{}
  for _,doc in ipairs(model.documents) do
    if doc.kind=='frontmatter' then table.insert(front,doc.id) end
    if doc.kind=='appendix' then table.insert(appendix,doc.id) end
  end
  group('Prije početka',front)
  for _,part in ipairs(model.parts) do group(part.title,part.chapters) end
  group('Dodaci',appendix);table.insert(result,'</nav>')
  return pandoc.RawBlock('html',table.concat(result,'\n'))
end

local function render_div(div)
  if div.classes:includes('mf1-book-catalog') then return catalog() end
  if div.classes:includes('mf1-component-title') then
    local output=pandoc.List({pandoc.RawBlock('html','<header class="mf1-component-title mf1-box-label">')})
    output:extend(div.content);output:insert(pandoc.RawBlock('html','</header>'))
    return output
  end
  local name=div.attributes['data-component'];local component=name and registry[name]
  if not component then return nil end
  if name=='Problem' then
    -- Task headings are local titles, excluded from the book TOC. Serialize
    -- them before Pandoc's section-div pass so an H3 cannot close the raw
    -- article boundary and leave the next article empty.
    div=div:walk({Header=function(header)
      return pandoc.RawBlock('html',pandoc.write(pandoc.Pandoc({header}),'html5',{section_divs=false}))
    end})
  end
  local tag=component.html or 'div'
  components.html_classes(name,div.classes)
  local attrs=' class="'..escape(table.concat(div.classes,' '))..'"'
  if component.role then attrs=attrs..' role="'..escape(component.role)..'"' end
  if div.identifier~='' then attrs=attrs..' id="'..escape(div.identifier)..'"' end
  for key,value in pairs(div.attributes) do attrs=attrs..' '..key..'="'..escape(value)..'"' end
  if not components.visible(name,'web') and not components.visible(name,'print') then attrs=attrs..' hidden' end
  local output=pandoc.List({pandoc.RawBlock('html','<'..tag..attrs..'>')})
  output:extend(div.content);output:insert(pandoc.RawBlock('html','</'..tag..'>'))
  return output
end

local function equation(span)
  local object=index.objects[span.identifier]
  if object and object.kind=='Equation' then
    span.attributes['data-component']='Equation'
    span.attributes['data-number']=object.number
    if collection then
      span=span:walk({Math=function(math)
        if math.mathtype=='DisplayMath' then
          local replaced,count=math.text:gsub('\\tag%{[^}]+%}', '\\tag{'..object.number..'}')
          math.text=count>0 and replaced or (math.text..'\\tag{'..object.number..'}')
        end
        return math
      end})
    end
    return span
  end
end
local function float_number(float)
  local object=index.objects[float.identifier]
  if collection and object then
    -- Quarto 1.9.37's HTML renderer formats arabic order values as text.
    -- A print collection uses the shared book number, not one counter over
    -- the concatenation. The native caption and its inline math stay intact.
    float.order={order=object.number}
    return float
  end
end
return {{Meta=function(meta) collection=meta['mf1-print-collection'] and pandoc.utils.stringify(meta['mf1-print-collection'])=='true' or false end},
        {Div=render_div,Span=equation,FloatRefTarget=float_number,Header=function(header)
          -- The book's native title block already supplies the home H1. Keep
          -- the source H1 for PDF and Quarto's pre-render chapter discovery.
          if header.classes:includes('mf1-home-title') then return {} end
        end}}
