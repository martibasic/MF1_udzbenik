-- Shared component identity and visibility policy for every presentation.
-- Quarto's dofile wrapper changes PANDOC_SCRIPT_FILE to its own main.lua.
-- The calling adapter passes the already resolved project root explicitly.
return function(root)
local file = assert(io.open(pandoc.path.join({root, 'components/registry.json'}), 'r'))
local registry = pandoc.json.decode(file:read('*a')).components
file:close()
local classes = {}
for name, component in pairs(registry) do
  for _, class in ipairs(component.classes or {}) do classes[class] = name end
  if component.visibility ~= nil then
    assert(type(component.visibility) == 'table', 'visibility must be an array: '..name)
    for _, target in ipairs(component.visibility) do
      assert(target == 'web' or target == 'pdf' or target == 'print', 'Unknown visibility target: '..tostring(target))
    end
  end
end
local function kind(div)
  if div.attributes['data-component'] then return div.attributes['data-component'] end
  for _, class in ipairs(div.classes) do if classes[class] then return classes[class] end end
end
local function visible(name, target)
  local component = name and registry[name]
  if not component or component.visibility == nil then return true end
  for _, allowed in ipairs(component.visibility) do if allowed == target then return true end end
  return false
end
local function html_classes(name, classes)
  for _, target in ipairs({'web', 'print'}) do
    local class = 'mf1-hidden-'..target
    if not visible(name, target) and not classes:includes(class) then classes:insert(class) end
  end
end
return {registry=registry, kind=kind, visible=visible, html_classes=html_classes}
end
