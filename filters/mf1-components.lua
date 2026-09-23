-- Shared semantic adapter. It accepts the established authoring syntax and
-- typed components; presentation is handled later by HTML and Typst adapters.
local root = pandoc.path.directory(pandoc.path.directory(PANDOC_SCRIPT_FILE))
local function read_json(path)
  local file = assert(io.open(pandoc.path.join({root, path}), "r"))
  local data = pandoc.json.decode(file:read("*a")); file:close(); return data
end
local components = dofile(pandoc.path.join({root, 'filters/mf1-component-model.lua'}))(root)
local registry = components.registry
local model = read_json("assets/book-model.json")
local index = read_json("assets/content-index.json")
local labels, documents, titles = {}, {}, {}
for name, component in pairs(registry) do
  for _, label in ipairs(component.labels or {}) do labels[label] = name end
end
for _, doc in ipairs(model.documents) do
  documents[doc.id] = doc; titles[doc.title] = doc
  for _, alias in ipairs(doc.title_aliases or {}) do titles[alias] = doc end
end
local is_html = FORMAT:match("html") ~= nil
local collection=false
local function text(node) return pandoc.utils.stringify(node) end
local kind = components.kind
local function decorate(div, name)
  div.attributes["data-component"] = name
  local component = registry[name]
  if component and component.pdf_mode then div.attributes["data-print-mode"] = component.pdf_mode end
  if component and component.accent then div.attributes["data-accent"] = component.accent end
  return div
end

local function extract_legacy_title(div)
  local content = div.content
  if #content >= 3 and content[1].t == "RawBlock" and content[1].text:find("mf1%-box%-label")
      and content[3].t == "RawBlock" and content[3].text:match("</p%s*>") then
    local label = content[2]
    content:remove(3);content:remove(2);content:remove(1)
    if div.classes:includes("mf1-zavrsni-okvir") then label=pandoc.Para({pandoc.Str("Sažetak")}) end
    content:insert(1,pandoc.Div({label},pandoc.Attr("",{"mf1-component-title","mf1-box-label"})))
  elseif div.attributes.title then
    local title=pandoc.Inlines({pandoc.Str(div.attributes.title)})
    if div.attributes.level then
      title:insert(pandoc.Space())
      title:insert(pandoc.Span({pandoc.Str(div.attributes.level)},pandoc.Attr("",{"mf1-level"})))
    end
    content:insert(1,pandoc.Div({pandoc.Para(title)},pandoc.Attr("",{"mf1-component-title","mf1-box-label"})))
  end
end

local function numbered_title(content, label)
  if content[1] and content[1].t=="Str" and content[1].text:match("^[PZ]%d+%.") then
    content[1].text=content[1].text:gsub("^[PZ]%d+%.%s*","")
    if content[1].text=="" then content:remove(1) end
    while content[1] and content[1].t=="Space" do content:remove(1) end
  end
  content:insert(1,pandoc.Space());content:insert(1,pandoc.Str(label.."."))
end
local adapt_table

local function example_fields(div)
  local result, current = pandoc.List(), nil
  for _, block in ipairs(div.content) do
    -- Solution steps describe a local algorithm, not subsections of the book.
    if block.t == "Header" then
      local attr=block.attr
      attr.classes:insert("mf1-minor-title")
      block=pandoc.Div({pandoc.Para({pandoc.Strong(block.content)})},attr)
    end
    local field
    if block.t == "Para" and block.content[1] and block.content[1].t == "Strong" then
      field=labels[text(block.content[1]):gsub("[:.]%s*$", "")]
    end
    if field then
      current=decorate(pandoc.Div({},pandoc.Attr("",{"mf1-example-field"})),field)
      result:insert(current)
    end
    if current then current.content:insert(block) else result:insert(block) end
  end
  div.content=result
end

local function adapt_div(div)
  if div.classes:includes('mf1-glossary') then
    div=div:walk({Table=function(table) return adapt_table(table,true) end})
  end
  local name=kind(div)
  if name then
    decorate(div,name);extract_legacy_title(div)
    local object=index.objects[div.identifier]
    if name=="Example" then
      if object then
        div.attributes["data-number"]=object.number
        div.attributes["data-level"]=object.level or ""
        local title=div.content[1]
        if title and title.t=="Div" and title.classes:includes("mf1-component-title") then
          title=title.content[1]
          if title then numbered_title(title.content,object.label) end
        end
      end
      example_fields(div)
    end
  end
  if div.classes:includes("mf1-vjezbe-list") then
    local result,current=pandoc.List(),nil
    for _,block in ipairs(div.content) do
      if block.t=="Header" and block.identifier:sub(1,5)=="task-" then
        local object=index.objects[block.identifier]
        current=decorate(pandoc.Div({},pandoc.Attr("",{"mf1-problem"})),"Problem")
        current.attributes["data-object-id"]=block.identifier
        if object then
          current.attributes["data-level"]=object.level or ""
          current.attributes["data-number"]=object.number
          numbered_title(block.content,object.label)
        end
        result:insert(current)
      end
      if current then current.content:insert(block) else result:insert(block) end
    end
    div.content=result
  end
  return div
end

local function reference(target, content)
  local object=index.objects[target]
  if not object then error("Unknown MF1 object reference: "..target) end
  local doc=documents[object.document]
  if not content or #content==0 then
    local names={Example="primjer",Problem="zadatak",Equation="jednadžba",Figure="slika",Table="tablica"}
    content={pandoc.Str((names[object.kind] or object.kind).." "..object.number)}
  end
  local href=FORMAT:match('typst') and ('#'..target) or ('/'..doc.path..'#'..target)
  return pandoc.Link(content,href,"",pandoc.Attr("",{"mf1-reference"}))
end

local function adapt_span(span)
  if span.classes:includes("mf1-book-meta") then
    local key=span.attributes.key
    local value=key=='full-title' and (model.book.title..' — '..model.book.subtitle) or model.book[key]
    assert(value,'Unknown book metadata: '..(key or ''))
    return pandoc.Span({pandoc.Str(value)})
  end
  if span.classes:includes("mf1-chapter-ref") then
    local doc=documents[span.attributes.target]
    assert(doc,"Unknown chapter reference: "..(span.attributes.target or ""))
    return pandoc.Link({pandoc.Str("pog. "..doc.number.." "..doc.title)},"/"..doc.path,"",pandoc.Attr("",{"mf1-ch-ref"}))
  end
  if span.classes:includes("mf1-ch-ref") then
    local title
    for _,item in ipairs(span.content) do
      if item.t=="Span" and item.classes:includes("mf1-ch-title") then title=text(item) end
    end
    local doc=titles[title]
    if doc then return pandoc.Link({pandoc.Str("pog. "..doc.number.." "..doc.title)},"/"..doc.path,"",pandoc.Attr("",{"mf1-ch-ref"})) end
  end
  if span.classes:includes("mf1-reference") then return reference(span.attributes.target or "",span.content) end
  if span.classes:includes("mf1-term") then
    local query=(span.attributes.term or text(span)):lower()
    for id,term in pairs(index.terms) do
      if id==query or term.term:lower()==query then
        local doc=documents[term.document]
        return pandoc.Link(span.content,"/"..doc.path.."#"..id,"",pandoc.Attr("",{"mf1-term-link"}))
      end
    end
    error("Unknown glossary term: "..query)
  end
end

local function adapt_cite(cite)
  if #cite.citations~=1 then return nil end
  local object=index.objects[cite.citations[1].id]
  if object and (collection or object.kind=="Example" or object.kind=="Problem") then return reference(object.id) end
end

local function adapt_blocks(blocks)
  local result=pandoc.List()
  for i,block in ipairs(blocks) do
    local following=blocks[i+1]
    local next_kind=following and following.t=="Div" and kind(following)
    local hidden=next_kind and (is_html
      and not components.visible(next_kind,'web') and not components.visible(next_kind,'print')
      or not is_html and not components.visible(next_kind,'pdf'))
    if block.t=="Header" and hidden then
      result:insert(pandoc.Plain({pandoc.Span({},pandoc.Attr(block.identifier))}))
    elseif block.t=="Header" and block.classes:includes("mf1-step") then
      result:insert(pandoc.Div({pandoc.Para({pandoc.Strong(block.content)})},pandoc.Attr(block.identifier,{"mf1-minor-title","mf1-step"})))
    else
      if is_html and block.t=='Header' and next_kind then components.html_classes(next_kind,block.classes) end
      result:insert(block)
    end
  end
  return result
end

adapt_table=function(table, glossary)
  table.attributes["data-component"]="Table"
  if #table.colspecs>=4 then table.classes:insert("mf1-wide-table") end
  -- Terms are anchored in their existing cells, preserving table semantics.
  for _,body in ipairs(glossary and table.bodies or {}) do
    for _,row in ipairs(body.body) do
      local cell=row.cells[1]
      local label=cell and text(cell.contents)
      for id,term in pairs(index.terms) do
        if label==term.term and cell.contents[1] and cell.contents[1].content then
          local first=cell.contents[1]
          first.content={pandoc.Span(first.content,pandoc.Attr(id,{"mf1-glossary-term"}))}
          break
        end
      end
    end
  end
  return table
end

local function adapt_figure(figure)
  local object=index.objects[figure.identifier]
  if object then
    figure.attributes["data-component"]="Figure"
    figure.attributes["data-figure-type"]=object.type
    figure.attributes["data-number"]=object.number
    if collection and is_html then
      local body=pandoc.List({pandoc.RawBlock('html','<figure id="'..figure.identifier..'" data-component="Figure" data-number="'..object.number..'">')})
      body:extend(figure.content)
      body:insert(pandoc.RawBlock('html','<figcaption>Slika '..object.number..' — '))
      body:extend(figure.caption.long)
      body:insert(pandoc.RawBlock('html','</figcaption></figure>'))
      return body
    end
  end
  return figure
end

local function adapt_float(float)
  local object=index.objects[float.identifier]
  if object then
    float.attributes['data-component']=object.kind
    float.attributes['data-number']=object.number
    if object.type then float.attributes['data-figure-type']=object.type end
  end
  return float
end

local function adapt_callout(callout)
  -- A heading inside a note describes that note's local procedure. Quarto
  -- already extracted its title; remaining headings must not advance TOC.
  callout.content=pandoc.Div(callout.content):walk({Header=function(header)
    local attr=header.attr
    attr.classes:insert('mf1-minor-title')
    return pandoc.Div({pandoc.Para({pandoc.Strong(header.content)})},attr)
  end}).content
  return callout
end

local function collection_headers(doc)
  if not collection then return nil end
  local current,cursor=nil,0
  doc=doc:walk({Header=function(header)
    if header.classes:includes('mf1-collection-chapter') then
      current=index.documents[header.attributes['data-document']];cursor=0
      header.content:insert(1,pandoc.Space());header.content:insert(1,pandoc.Str(current.number..'.'))
    elseif current and not header.classes:includes('unnumbered') then
      for i=cursor+1,#current.sections do
        local section=current.sections[i]
        if section.title==text(header.content) and section.level==header.level and type(section.number)=='string' then
          cursor=i
          header.content:insert(1,pandoc.Space())
          header.content:insert(1,pandoc.Span({pandoc.Str(section.number)},pandoc.Attr('',{'header-section-number'})))
          header.attributes['data-number']=section.number
          break
        end
      end
    end
    return header
  end})
  return doc
end

return {
  {Meta=function(meta) collection=meta['mf1-print-collection'] and text(meta['mf1-print-collection'])=='true' or false end},
  {Div=adapt_div},
  {Blocks=adapt_blocks,Span=adapt_span,Cite=adapt_cite,Table=adapt_table,Figure=adapt_figure,FloatRefTarget=adapt_float,Callout=adapt_callout},
  {Pandoc=collection_headers},
}
