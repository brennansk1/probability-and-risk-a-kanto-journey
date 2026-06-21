-- workbook.lua — Pandoc Lua filter for the reMarkable WORKBOOK build.
-- After every problem inside a ::: problem-set div, inject a dot-grid work area
-- sized to that problem (sidecar workbook/workspace_sizes.json, else by tier).
-- The ::: answer-key div is left untouched. Run only for `make workbook`.

local sizes = {}          -- problem id -> "sm"|"md"|"lg"|"xl"
local default_by_tier = { route = "sm", gym = "md", elite = "lg", mock = "lg" }

-- ---- load the sidecar size map (best-effort; tier defaults if absent) ----
local function load_sizes()
  local f = io.open("workbook/workspace_sizes.json", "r")
  if not f then return end
  local s = f:read("*a"); f:close()
  -- tiny JSON-ish scan: "C5.3":"md"  (values restricted to sm/md/lg/xl)
  for id, sz in s:gmatch('"([Cc]%d+%.%d+)"%s*:%s*"(%a%a)"') do
    sizes[id:upper()] = sz:lower()
  end
end
load_sizes()

-- problem label like **C5.3.** -> "C5.3"
local function problem_id(para)
  local first = para.content[1]
  if not first or first.t ~= "Strong" then return nil end
  local txt = pandoc.utils.stringify(first)
  return txt:match("^(C%d+%.%d+)%.")
end

-- classify the current tier from the most recent H3 heading text
local function tier_of(headtext)
  local h = (headtext or ""):lower()
  if h:find("route") then return "route"
  elseif h:find("elite") then return "elite"
  elseif h:find("gym") then return "gym"
  elseif h:find("mock") then return "mock" end
  return "gym"  -- safe middle default
end

local function workspace_html(id, size)
  return string.format(
    '<div class="workspace ws-%s" data-label="%s"></div>', size, id)
end

-- Walk problem-set divs; insert a workspace block after each problem paragraph.
function Div(el)
  local is_problemset = false
  for _, c in ipairs(el.classes) do if c == "problem-set" then is_problemset = true end end
  if not is_problemset then return nil end

  local out = pandoc.List()
  local cur_tier = "gym"
  for _, blk in ipairs(el.content) do
    out:insert(blk)
    if blk.t == "Header" and blk.level == 3 then
      cur_tier = tier_of(pandoc.utils.stringify(blk))
    elseif blk.t == "Para" then
      local id = problem_id(blk)
      if id then
        local size = sizes[id] or default_by_tier[cur_tier] or "md"
        out:insert(pandoc.RawBlock("html", workspace_html(id, size)))
      end
    end
  end
  el.content = out
  return el
end
