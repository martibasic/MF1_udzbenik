-- Native Typst rendering for the MF1 authoring blocks.
--
-- The canonical sources deliberately keep HTML-oriented labels such as
-- <p class="mf1-box-label">...</p>.  Pandoc drops that raw HTML in a Typst
-- target, so this filter extracts the label and places the block in a native,
-- breakable Typst component.  Other output formats are left untouched.

if not FORMAT:match("typst") then
  return {}
end

local root = pandoc.path.directory(pandoc.path.directory(PANDOC_SCRIPT_FILE))
local function read_json(path)
  local file = assert(io.open(pandoc.path.join({root, path}), "r"))
  local data = pandoc.json.decode(file:read("*a")); file:close(); return data
end
local components = dofile(pandoc.path.join({root, 'filters/mf1-component-model.lua'}))(root)
local registry = components.registry
local tokens = read_json("design-system/tokens.json").web
local block_styles = {}
for _, component in pairs(registry) do
  if component.pdf_mode then
    for _, class in ipairs(component.classes or {}) do
      block_styles[class] = {accent=tokens[component.accent], mode=component.pdf_mode, label=component.label}
    end
  end
end

-- Kratke strukturne oznake u primjerima i završnim okvirima nisu obična
-- podebljana rečenica.  U PDF-u ih pretvaramo u male, ljepljive podnaslove s
-- dovoljno bjeline prije i poslije.  HTML zadržava postojeći CSS prikaz.
local minor_heading_labels = {
  ["Kontekst"] = true,
  ["Zadano"] = true,
  ["Traženo"] = true,
  ["Pretpostavke i model"] = true,
  ["Rješenje"] = true,
  ["Provjera i komentar"] = true,
  ["Predznanje koje se pretpostavlja"] = true,
  ["Ishodi učenja"] = true,
  ["Sažeta provjera prije računa"] = true,
  ["Najčešća pogreška"] = true,
  ["Česta pogreška"] = true,
  ["Što provjeriti"] = true,
  ["Nakon ovoga poglavlja mora biti moguće"] = true,
  ["U tehnici to znači"] = true,
  ["Granica modela"] = true,
  ["Kamo dalje nakon MF1"] = true,
}
for _, component in pairs(registry) do
  for _, label in ipairs(component.labels or {}) do minor_heading_labels[label] = true end
end

local function style_for(div)
  for _, class_name in ipairs(div.classes) do
    local style = block_styles[class_name]
    if style ~= nil then
      return style
    end
  end
  return nil
end

local function is_label_open(block)
  return block.t == "RawBlock"
    and tostring(block.format) == "html"
    and block.text:match("<p%s+[^>]-class=[\"'][^\"']*mf1%-box%-label[^\"']*[\"'][^>]*>") ~= nil
end

local function is_label_close(block)
  return block.t == "RawBlock"
    and tostring(block.format) == "html"
    and block.text:match("</p%s*>") ~= nil
end

local function extract_label(content, fallback)
  if content[1] and content[1].t == "Div" and content[1].classes:includes("mf1-component-title") then
    return content:remove(1).content[1]
  end
  if #content >= 3 and is_label_open(content[1]) and is_label_close(content[3]) then
    local label = content[2]
    content:remove(3)
    content:remove(2)
    content:remove(1)
    return label
  end

  return pandoc.Plain({ pandoc.Str(fallback) })
end

local function render_author_block(div)
  if not components.visible(components.kind(div), 'pdf') then return pandoc.List() end
  if div.identifier == "refs" then
    return pandoc.RawBlock("typst", '#bibliography("references.bib", title: none) <refs>')
  end
  if div.classes:includes("mf1-interaktivno-akcija") then
    -- Raw HTML links/images disappear in Typst. Reparse just this HTML
    -- fragment with Pandoc's HTML reader to retain native links and QR art.
    local html = pandoc.write(pandoc.Pandoc(div.content), "html")
    local parsed = pandoc.read(html, "html")
    local links = pandoc.List()
    local images = pandoc.List()
    parsed:walk({ Link = function(link)
      links:insert(pandoc.Para({link}))
    end, Image = function(img)
      img.src = img.src:gsub("^%.%./assets/", "assets/")
      img.attributes.width = "28mm"
      images:insert(pandoc.Plain({img}))
    end })
    local result = pandoc.List({pandoc.RawBlock("typst", "#grid(columns: (1fr, 28mm), column-gutter: 4mm, align: horizon, [")})
    result:extend(links)
    result:insert(pandoc.RawBlock("typst", "], ["))
    result:extend(images)
    result:insert(pandoc.RawBlock("typst", "])"))
    return result
  end

  if div.classes:includes("mf1-decision-step") then
    local content = pandoc.List(div.content)
    local index = pandoc.utils.stringify(content:remove(1))
    local label = extract_label(content, "Korak")
    local result = pandoc.List({pandoc.RawBlock("typst", "#block(breakable: false)[#mf1-minor-heading([")})
    local title = pandoc.List({pandoc.Str(index .. "."), pandoc.Space()})
    title:extend(label.content)
    result:insert(pandoc.Plain(title))
    result:insert(pandoc.RawBlock("typst", "])"))
    result:extend(content)
    result:insert(pandoc.RawBlock("typst", "]"))
    return result
  end

  if div.classes:includes("mf1-vjezbe-list") or div.classes:includes("mf1-problem") then
    -- Keep the small level label with the task's last visible paragraph.
    -- HTML-only hints/results may occur between that paragraph and the label.
    local content = pandoc.List()
    for _, block in ipairs(div.content) do
      local footer = block.t == "Para" and #block.content == 1
        and block.content[1].t == "Span"
        and block.content[1].classes:includes("mf1-task-level")
      local previous = #content
      if footer then
        while previous > 0 and content[previous].t ~= "Para"
          and content[previous].t ~= "Plain" and content[previous].t ~= "Header" do
          previous = previous - 1
        end
      end
      if footer and previous > 0
        and (content[previous].t == "Para" or content[previous].t == "Plain") then
        content:insert(previous, pandoc.RawBlock("typst", "#block(width: 100%, breakable: false)["))
        content:insert(block)
        content:insert(pandoc.RawBlock("typst", "]"))
      else
        content:insert(block)
      end
    end
    div.content = content
    return div
  end

  if div.classes:includes("mf1-example-field") then return div end
  if div.classes:includes("mf1-minor-title") then
    if div.content[1] and div.content[1].t == "RawBlock" and tostring(div.content[1].format) == "typst" then
      if div.identifier ~= "" then div.content:insert(pandoc.RawBlock("typst", '#label(' .. pandoc.json.encode(div.identifier) .. ')')) end
      return div.content
    end
    local title = div.content[1]
    if title and title.content[1] and title.content[1].t == "Strong" then title = pandoc.Plain(title.content[1].content) end
    local anchor = div.identifier ~= "" and (' #label(' .. pandoc.json.encode(div.identifier) .. ')') or ""
    return {pandoc.RawBlock("typst", "#mf1-minor-heading(["), title, pandoc.RawBlock("typst", "])" .. anchor)}
  end
  local style = style_for(div)
  if style == nil then
    return nil
  end

  local content = pandoc.List(div.content)
  local label = extract_label(content, style.label)
  if div.classes:includes("mf1-zavrsni-okvir") then
    label = pandoc.Plain({ pandoc.Str("Sažetak") })
  end
  local result = pandoc.List()

  local keep_together = div.classes:includes("mf1-interaktivno")
  -- Only the compact numerical note may contain a QR grid. A solved
  -- example can contain that note and still needs normal page breaks.
  if div.classes:includes("mf1-numerika") then
    div:walk({ Image = function(img)
      if img.src:match("assets/qr/") then keep_together = true end
    end })
  end
  if keep_together then
    result:insert(pandoc.RawBlock("typst", "#block(breakable: false)["))
  end

  result:insert(pandoc.RawBlock(
    "typst",
    '#mf1-author-block(accent: rgb("' .. style.accent .. '"), mode: "' .. style.mode .. '", title: ['
  ))
  result:insert(label)
  -- Typst's trailing content argument must touch the closing parenthesis.
  result:insert(pandoc.RawBlock("typst", "])["))

  for _, block in ipairs(content) do
    result:insert(block)
  end

  result:insert(pandoc.RawBlock("typst", "]"))
  if keep_together then
    result:insert(pandoc.RawBlock("typst", "]"))
  end
  if div.identifier ~= "" then
    result:insert(pandoc.RawBlock("typst", '#label(' .. pandoc.json.encode(div.identifier) .. ')'))
  end
  return result
end

local function render_span(span)
  if span.classes:includes("mf1-task-level") then
    local result = pandoc.List({ pandoc.RawInline("typst", "#mf1-task-level([") })
    result:extend(span.content)
    result:insert(pandoc.RawInline("typst", "])"))
    return pandoc.Span(result, span.attr)
  end

  -- HTML separates the chapter code and title with CSS; PDF needs an actual
  -- space so references do not collapse to e.g. "pog. 10Količina gibanja".
  if span.classes:includes("mf1-ch-ref") then
    local content = pandoc.List()
    for _, inline in ipairs(span.content) do
      if inline.t == "Span" and inline.classes:includes("mf1-ch-title") then
        content:insert(pandoc.Space())
      end
      content:insert(inline)
    end
    return pandoc.Span(content, span.attr)
  end

  if not span.classes:includes("mf1-level") then
    return nil
  end

  local result = pandoc.List()
  result:insert(pandoc.RawInline("typst", "#h(0.45em)#mf1-level(["))
  for _, inline in ipairs(span.content) do
    result:insert(inline)
  end
  result:insert(pandoc.RawInline("typst", "])"))
  return result
end

local function render_minor_heading(para)
  if #para.content == 0 or para.content[1].t ~= "Strong" then
    return nil
  end

  local first = para.content[1]
  local label = pandoc.utils.stringify(first):gsub("%s*:%s*$", "")
  if not minor_heading_labels[label] then
    return nil
  end

  local result = pandoc.List()
  result:insert(pandoc.RawBlock("typst", "#mf1-minor-heading(["))
  result:insert(pandoc.Plain(first.content))
  result:insert(pandoc.RawBlock("typst", "])"))

  local remainder = pandoc.List(para.content)
  remainder:remove(1)
  while #remainder > 0
    and (remainder[1].t == "Space" or remainder[1].t == "SoftBreak" or remainder[1].t == "LineBreak") do
    remainder:remove(1)
  end
  if #remainder > 0 then
    result:insert(pandoc.Para(remainder))
  end
  return result
end

local function render_step_heading(header)
  if pandoc.utils.stringify(header.content):match("Razrada koraka") then
    header.content = { pandoc.Str("Postupak"), pandoc.Space(), pandoc.Str("rješenja") }
    return header
  end

  if not header.classes:includes("mf1-step") then
    return nil
  end
  local identifier = header.identifier:gsub("\\", "\\\\"):gsub('"', '\\"')
  local anchor = identifier ~= "" and (' #label("' .. identifier .. '")') or ""
  return {
    pandoc.RawBlock("typst", "#mf1-minor-heading(["),
    pandoc.Plain(header.content),
    pandoc.RawBlock("typst", "])" .. anchor),
  }
end

local function configure_document(doc)
  -- This block is emitted inside orange-book's body, after its own paragraph
  -- defaults, so it intentionally wins without forking Quarto's template.
  -- Pandoc renders \boxed as a box containing another math.equation. Keep
  -- the outer equation's number, but prevent nested equations from inheriting
  -- orange-book's numbering (which otherwise doubles numbers and counters).
  doc.blocks:insert(1, pandoc.RawBlock(
    "typst",
    [[#show: mf1-reading
#show math.equation: it => {
  set math.equation(numbering: none)
  it
}]]
  ))
  return doc
end

local function render_math(expression)
  -- Pandoc bundled with Quarto 1.9.37 writes TeX's negative thin space (\!)
  -- as #h(-1em), which can reorder or overlap adjacent symbols. Keep Typst's
  -- normal math spacing instead; the canonical expression stays unchanged.
  expression.text = expression.text:gsub("\\!", "")
  return expression
end

local print_layout_file = assert(io.open("assets/pdf-figures/manifest.json", "r"))
local print_layouts = pandoc.json.decode(print_layout_file:read("*a")).figures
print_layout_file:close()

local function render_print_image(img)
  local name = img.src:match("/assets/print/([^/]+)$")
  local layout = name and print_layouts[name]
  if not layout then return nil end
  local source = assert(io.open(img.src, "r"))
  local svg = source:read("*a")
  source:close()
  assert(not layout.source_sha1 or pandoc.utils.sha1(svg:gsub("\r\n", "\n")) == layout.source_sha1,
    "SVG changed: rebuild and review print derivatives for " .. name)
  local rows = {}
  for _, row in ipairs(layout.rows) do
    table.insert(rows, "(" .. pandoc.json.encode("/assets/pdf-figures/" .. row.file)
      .. ", " .. tostring(row.width) .. ", " .. tostring(row.keep_with_next) .. ")")
  end
  return pandoc.RawInline("typst", '#mf1-print-rows((' .. table.concat(rows, ", ") .. ',))')
end

return {
  { Math = render_math },
  { Image = render_print_image },
  { Span = render_span },
  { Header = render_step_heading },
  { Para = render_minor_heading },
  { Div = render_author_block },
  { Pandoc = configure_document },
}
