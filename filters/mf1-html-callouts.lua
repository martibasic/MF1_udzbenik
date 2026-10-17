-- Collapsible callouts carry Croatian button semantics in the HTML itself,
-- not only after web/reading.js runs. Quarto renders callouts to Bootstrap
-- divs in its render phase, so this filter runs at post-render.
if not FORMAT:match("html") then return {} end

local function title_of(header)
  local title = ""
  header:walk({Div = function(div)
    if div.classes:includes("callout-title-container") then
      local copy = div:walk({Span = function(span)
        if span.classes:includes("screen-reader-only") then return {} end
      end})
      title = pandoc.utils.stringify(copy):gsub("%s+", " "):gsub("^ ", ""):gsub(" $", "")
    end
  end})
  return title
end

return {{Div = function(div)
  if not div.classes:includes("callout-header") or div.attributes["bs-toggle"] ~= "collapse" then
    return nil
  end
  local title = title_of(div)
  div.attributes["role"] = "button"
  div.attributes["tabindex"] = "0"
  div.attributes["aria-label"] = title ~= "" and ("Prikaži ili sakrij odjeljak: " .. title)
    or "Prikaži ili sakrij odjeljak"
  return div
end}}
