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
  local style = style_for(div)
  if style == nil then
    return nil
  end

  local content = pandoc.List(div.content)
  local label = extract_label(content, style.label)
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

local function render_level(span)
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

local function configure_document(doc)
  -- This block is emitted inside orange-book's body, after its own paragraph
  -- defaults, so it intentionally wins without forking Quarto's template.
  doc.blocks:insert(1, pandoc.RawBlock(
    "typst",
    "#set par(first-line-indent: 0pt, spacing: 0.72em)"
  ))
  return doc
end

return {
  { Span = render_level },
  { Para = render_minor_heading },
  { Div = render_author_block },
  { Pandoc = configure_document },
}
