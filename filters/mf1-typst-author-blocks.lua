-- Native Typst rendering for the MF1 authoring blocks.
--
-- The canonical sources deliberately keep HTML-oriented labels such as
-- <p class="mf1-box-label">...</p>.  Pandoc drops that raw HTML in a Typst
-- target, so this filter extracts the label and places the block in a native,
-- breakable Typst component.  Other output formats are left untouched.

if not FORMAT:match("typst") then
  return {}
end

local block_styles = {
  ["mf1-we"] =                     { accent = "#2c6e2e", mode = "example", label = "Riješeni primjer" },
  ["mf1-gp"] =                     { accent = "#1b5fa8", mode = "example", label = "Vođeni primjer" },
  ["mf1-po"] =                     { accent = "#6e4a35", mode = "example", label = "Primjer odluke" },
  ["mf1-ch"] =                     { accent = "#7c2e92", mode = "example", label = "Cjeloviti zadatak" },
  ["mf1-temelj"] =                 { accent = "#4f735b", mode = "rail",  label = "Temelj" },
  ["mf1-izvod"] =                  { accent = "#536577", mode = "rail",  label = "Izvod" },
  ["mf1-fizikalno-znacenje"] =     { accent = "#14747b", mode = "rail",  label = "Fizikalno značenje" },
  ["mf1-granica-modela"] =         { accent = "#9a4b2b", mode = "rail",  label = "Granica modela" },
  ["mf1-numerika"] =               { accent = "#765b91", mode = "rail",  label = "Numerički pokus" },
  ["mf1-dublje"] =                 { accent = "#6f5a86", mode = "rail",  label = "Dublje" },
  ["mf1-application"] =            { accent = "#8e4519", mode = "rail",  label = "Inženjerski kontekst" },
  ["mf1-interaktivno"] =           { accent = "#765b91", mode = "rail",  label = "Numerički pokus" },
  ["mf1-warning"] =                { accent = "#9a4b2b", mode = "alert", label = "Oprez" },
  ["mf1-priprema"] =               { accent = "#69727b", mode = "panel", label = "Prije čitanja poglavlja" },
  ["mf1-samoprovjera"] =           { accent = "#69727b", mode = "panel", label = "Konceptualna provjera" },
  ["mf1-zavrsni-okvir"] =          { accent = "#4f735b", mode = "panel", label = "Sažeta mapa modela" },
  ["mf1-checklist"] =              { accent = "#69727b", mode = "panel", label = "Provjera" },
  ["mf1-mini-summary"] =           { accent = "#4f735b", mode = "panel", label = "Sažetak" },
  ["mf1-print-note"] =             { accent = "#69727b", mode = "panel", label = "Napomena" },
}

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
  ["Nakon ovoga poglavlja mora biti moguće"] = true,
  ["U tehnici to znači"] = true,
  ["Granica modela"] = true,
}

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
  if div.classes:includes("mf1-vjezbe-list") then
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

  -- Pripremni i samoprovjerni sadržaj namijenjeni su mrežnom radu.
  -- Numerički mostovi ostaju u PDF-u kao prijelaz prema CFD-u.
  if div.classes:includes("mf1-priprema")
    or div.classes:includes("mf1-samoprovjera") then
    return pandoc.List()
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
    [[#set par(first-line-indent: 0pt, spacing: 0.72em)
#show math.equation: it => {
  set math.equation(numbering: none)
  it
}]]
  ))
  return doc
end

return {
  { Span = render_span },
  { Header = render_step_heading },
  { Para = render_minor_heading },
  { Div = render_author_block },
  { Pandoc = configure_document },
}
