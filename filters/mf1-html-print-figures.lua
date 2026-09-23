-- The screen image stays unchanged. Only @media print reveals these derivatives.
if not FORMAT:match("html") then return {} end
local root = pandoc.path.directory(PANDOC_SCRIPT_FILE) .. "/.."
local file = assert(io.open(root .. "/assets/pdf-figures/manifest.json", "r"))
local figures = pandoc.json.decode(file:read("*a")).figures
file:close()
return {{ Image = function(img)
  local name = img.src:match("/assets/print/([^/]+)$")
  local figure = name and figures[name]
  if figure then
    local rows = {}
    for _, row in ipairs(figure.rows) do
      table.insert(rows, {file = row.file, width = row.width, height = row.height,
        keep_with_next = row.keep_with_next})
    end
    img.attributes["data-mf1-print-layout"] = pandoc.json.encode(rows)
    img.attributes["data-mf1-figure-kind"] = figure.kind
  end
  return img
end }}
