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
    -- The chapter summary takes its heading from the "## Sažetak" section;
    -- a box without its own label is shown without a title.
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
    if block.t == "Header" and block.identifier:sub(1,5) ~= "task-" then
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
    elseif (block.t == "Div" and block.classes:includes("content-visible"))
      or (block.t == "Para" and #block.content == 1 and block.content[1].t == "Span"
        and block.content[1].classes:includes("mf1-task-level")) then
      -- Hints, answers and the level label belong to the problem, not Required.
      current=nil
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
          if is_html and object.level then
            -- Same level chip beside the title as in solved examples; the
            -- separate "Razina" line remains the PDF presentation (registry).
            block.content:insert(pandoc.Space())
            block.content:insert(pandoc.Span({pandoc.Str(object.level)},pandoc.Attr("",{"mf1-level"})))
          end
        end
        result:insert(current)
      end
      if current then current.content:insert(block) else result:insert(block) end
    end
    for _,problem in ipairs(result) do
      if problem.t=="Div" and problem.classes:includes("mf1-problem") then
        example_fields(problem)
      end
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

-- "pog. 5" never breaks between the abbreviation and its number.
local function chapter_link(doc)
  return pandoc.Link({pandoc.Str("pog.\u{00A0}"..doc.number.." "..doc.title)},"/"..doc.path,"",pandoc.Attr("",{"mf1-ch-ref"}))
end

-- Inline and raw-HTML components follow the same registry visibility policy
-- as block components; no adapter keeps its own list of hidden classes.
local function governed(name)
  return name and registry[name] and registry[name].visibility ~= nil
end
local function raw_component(raw)
  if tostring(raw.format)~="html" then return nil end
  local tag,attrs=raw.text:match("^%s*<(%w+)([^>]*)>")
  local class=attrs and (attrs:match('class%s*=%s*"([^"]*)"') or attrs:match("class%s*=%s*'([^']*)'"))
  if not class then return nil end
  local classes=pandoc.List()
  for item in class:gmatch("%S+") do classes:insert(item) end
  local name=kind({attributes={},classes=classes})
  if governed(name) then return name,tag end
end
local function mark_raw_html(raw,name)
  local extra=pandoc.List()
  components.html_classes(name,extra)
  if #extra==0 then return raw end
  raw.text=raw.text:gsub("(class%s*=%s*[\"'])","%1"..table.concat(extra," ").." ",1)
  return raw
end
local function adapt_raw_inline(raw)
  local name=raw_component(raw)
  if not name then return nil end
  if is_html then return mark_raw_html(raw,name) end
  if not components.visible(name,'pdf') then return {} end
end
local function inline_visibility(span)
  local name=kind(span)
  if not governed(name) then return nil end
  if is_html then
    components.html_classes(name,span.classes)
    if not components.visible(name,'web') and not components.visible(name,'print') then span.attributes.hidden="" end
    return span
  end
  if not components.visible(name,'pdf') then return {} end
  return span
end

local function adapt_span(span)
  local governed_span=inline_visibility(span)
  if governed_span then return governed_span end
  if span.classes:includes("mf1-book-meta") then
    local key=span.attributes.key
    local value=key=='full-title' and (model.book.title..' — '..model.book.subtitle) or model.book[key]
    assert(value,'Unknown book metadata: '..(key or ''))
    return pandoc.Span({pandoc.Str(value)})
  end
  if span.classes:includes("mf1-chapter-ref") then
    local doc=documents[span.attributes.target]
    assert(doc,"Unknown chapter reference: "..(span.attributes.target or ""))
    return chapter_link(doc)
  end
  if span.classes:includes("mf1-ch-ref") then
    local title
    for _,item in ipairs(span.content) do
      if item.t=="Span" and item.classes:includes("mf1-ch-title") then title=text(item) end
    end
    local doc=titles[title]
    if doc then return chapter_link(doc) end
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
  if object and (collection or object.kind=="Example" or object.kind=="Problem") then
    -- [-@id] ispisuje samo broj, pa tekst sam sklanja imenicu:
    -- "u primjeru [-@ex-...]", "prema jednadžbi [-@eq-...]".
    if cite.citations[1].mode=="SuppressAuthor" then
      return reference(object.id,{pandoc.Str(object.number)})
    end
    return reference(object.id)
  end
end

local function pdf_document_link(link)
  if not FORMAT:match('typst') or link.target:match('^%a[%w+.-]*:') then return nil end
  local path, fragment = link.target:match('^([^#]+)#?(.*)$')
  local filename = path and path:match('([^/]+)%.qmd$')
  if not filename then return nil end
  for id, doc in pairs(documents) do
    if doc.path:match('([^/]+)%.qmd$') == filename then
      -- A standalone PDF must navigate within itself, including appendices.
      -- The first canonical section is stable even when a title is renamed.
      local section = index.documents[id].sections[1]
      assert(fragment ~= '' or section, 'No PDF destination for '..doc.path)
      link.target = '#'..(fragment ~= '' and fragment or section.id)
      return link
    end
  end
end

local function blank_inlines(inlines)
  for _,item in ipairs(inlines) do
    if item.t~="Space" and item.t~="SoftBreak" and item.t~="LineBreak" then return false end
  end
  return true
end

local function adapt_blocks(blocks)
  local result=pandoc.List()
  local skip_tag=nil
  for i,block in ipairs(blocks) do
    -- A raw HTML element hidden in this output (e.g. <p class="...">)
    -- is removed together with the Markdown blocks between its tags.
    if skip_tag then
      if block.t=="RawBlock" and block.text:match("^%s*</"..skip_tag.."%s*>") then skip_tag=nil end
      goto continue
    end
    if block.t=="RawBlock" then
      local name,tag=raw_component(block)
      if name and is_html then
        block=mark_raw_html(block,name)
      elseif name and not components.visible(name,'pdf') then
        if not block.text:match("</"..tag.."%s*>") then skip_tag=tag end
        goto continue
      end
    end
    -- A paragraph that only held hidden inline components disappears.
    if not is_html and (block.t=="Para" or block.t=="Plain") and #block.content>0 and blank_inlines(block.content) then
      goto continue
    end
    do
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
    ::continue::
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
  {Blocks=adapt_blocks,Span=adapt_span,RawInline=adapt_raw_inline,Cite=adapt_cite,Table=adapt_table,Figure=adapt_figure,FloatRefTarget=adapt_float,Callout=adapt_callout},
  {Link=pdf_document_link},
  {Pandoc=collection_headers},
}
