-- Neutralni naslovi za zajednički HTML i Typst izlaz.
-- Izvor zadržava postojeću strukturu zadataka, a javni prikaz rabi
-- sadržajno orijentirane oznake bez didaktičkoga metasloja.

local function normalized_text(inlines)
  return pandoc.utils.stringify(inlines):gsub("%s+", " "):gsub("^%s+", ""):gsub("%s+$", "")
end

local function replacement_title(title)
  local text = normalized_text(title)
  if text == "Naputak" then
    return { pandoc.Str("Smjernica") }
  end
  -- Identifikator zaglavlja ostaje isti radi postojećih poveznica.
  if text:match("Zadaci za vježbu$") or text:match("Zadaci za samostalan rad$") then
    -- Post-quarto zaglavlje može već sadržavati broj odjeljka u Spanu.
    for _, inline in ipairs(title) do
      if inline.t == "Str" and inline.text == "Zadaci" then
        inline.text = "Zadatci"
      end
    end
    return title
  end
  if text:find("Razrada koraka", 1, true) then
    return { pandoc.Str("Postupak"), pandoc.Space(), pandoc.Str("rješenja") }
  end
  return nil
end

function Header(header)
  local replacement = replacement_title(header.content)
  if replacement then
    header.content = replacement
    return header
  end

  return nil
end

function Callout(callout)
  if not callout.title then
    return nil
  end

  local replacement = replacement_title(callout.title)
  if replacement then
    callout.title = replacement
    return callout
  end

  return nil
end

return {
  { Header = Header, Callout = Callout },
}
