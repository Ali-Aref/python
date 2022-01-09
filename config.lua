--[[
lvim is the global options object

Linters should be
filled in as strings with either
a global executable or a path to
an executable
]]
-- THESE ARE EXAMPLE CONFIGS FEEL FREE TO CHANGE TO WHATEVER YOU WANT

-- general
lvim.log.level = "warn"
lvim.format_on_save = false
lvim.colorscheme = "sonokai"

-- keymappings [view all the defaults by pressing <leader>Lk]
lvim.leader = "space"
-- add your own keymapping
lvim.keys.normal_mode["<C-s>"] = ":w<cr>"
lvim.keys.insert_mode.jj = "<ESC>"
lvim.keys.normal_mode["<A-h>"] = "<C-w>h"
lvim.keys.normal_mode["<A-l>"] = "<C-w>l"
lvim.keys.normal_mode["<A-j>"] = "<C-w>j"
lvim.keys.normal_mode["<A-k>"] = "<C-w>k"
-- lvim.keys.normal_mode["<F5>"] = ":! node %<cr>"
lvim.keys.normal_mode["<F5>"] = ":! python %<cr>"

-- unmap a default keymapping
-- lvim.keys.normal_mode["<C-Up>"] = ""
-- edit a default keymapping
-- lvim.keys.normal_mode["<C-q>"] = ":q<cr>"

-- Change Telescope navigation to use j and k for navigation and n and p for history in both input and normal mode.
-- we use protected-mode (pcall) just in case the plugin wasn't loaded yet.
-- local _, actions = pcall(require, "telescope.actions")
-- lvim.builtin.telescope.defaults.mappings = {
--   -- for input mode
--   i = {
--     ["<C-j>"] = actions.move_selection_next,
--     ["<C-k>"] = actions.move_selection_previous,
--     ["<C-n>"] = actions.cycle_history_next,
--     ["<C-p>"] = actions.cycle_history_prev,
--   },
--   -- for normal mode
--   n = {
--     ["<C-j>"] = actions.move_selection_next,
--     ["<C-k>"] = actions.move_selection_previous,
--   },
-- }

-- Use which-key to add extra bindings with the leader-key prefix
-- lvim.builtin.which_key.mappings["P"] = { "<cmd>Telescope projects<CR>", "Projects" }
lvim.builtin.which_key.mappings["t"] = {
  name = "+Trouble",
  r = { "<cmd>Trouble lsp_references<cr>", "References" },
  f = { "<cmd>Trouble lsp_definitions<cr>", "Definitions" },
  d = { "<cmd>Trouble lsp_document_diagnostics<cr>", "Diagnostics" },
  q = { "<cmd>Trouble quickfix<cr>", "QuickFix" },
  l = { "<cmd>Trouble loclist<cr>", "LocationList" },
  w = { "<cmd>Trouble lsp_workspace_diagnostics<cr>", "Diagnostics" },
}
lvim.builtin.which_key.mappings["j"] = {
  name = "+Jump",
  w = { "<cmd>HopWord<cr>", "Word" },
  c = { "<cmd>HopChar1<cr>", "Char1" },
  C = { "<cmd>HopChar2<cr>", "Char2" },
  l = { "<cmd>HopLine<cr>", "Line" },
  L = { "<cmd>HopLineStart<cr>", "Line Start" },
  p = { "<cmd>HopPattern<cr>", "Pattern" },
  a = { "<cmd>HopLineStartAC<cr>", "After Cursor" },
  b = { "<cmd>HopLineStartBC<cr>", "Before Cursor" },
}
lvim.builtin.which_key.vmappings["j"] = {
  name = "+Jump",
  w = { "<cmd>HopWord<cr>", "Word" },
  c = { "<cmd>HopChar1<cr>", "Char1" },
  C = { "<cmd>HopChar2<cr>", "Char2" },
  l = { "<cmd>HopLine<cr>", "Line" },
  L = { "<cmd>HopLineStart<cr>", "Line Start" },
  p = { "<cmd>HopPattern<cr>", "Pattern" },
  a = { "<cmd>HopLineStartAC<cr>", "After Cursor" },
  b = { "<cmd>HopLineStartBC<cr>", "Before Cursor" },
}
lvim.builtin.which_key.mappings["E"] = {"<cmd>NvimTreeRefresh<cr>", "Refresh explorer"}

-- TODO: User Config for predefined plugins
-- After changing plugin config exit and reopen LunarVim, Run :PackerInstall :PackerCompile
lvim.builtin.dashboard.active = false
lvim.builtin.terminal.active = true
lvim.builtin.nvimtree.setup.view.side = "left"
lvim.builtin.nvimtree.show_icons.git = 1

-- if you don't want all the parsers change this to a table of the ones you want
lvim.builtin.treesitter.ensure_installed = {
  "bash",
  "c",
  "javascript",
  "json",
  "lua",
  "python",
  "typescript",
  "css",
  "rust",
  "java",
  "yaml",
}

lvim.builtin.treesitter.ignore_install = { "haskell" }
lvim.builtin.treesitter.highlight.enabled = true

-- generic LSP settings

-- ---@usage disable automatic installation of servers
lvim.lsp.automatic_servers_installation = false

-- ---@usage Select which servers should be configured manually. Requires `:LvimCacheRest` to take effect.
-- See the full default list `:lua print(vim.inspect(lvim.lsp.override))`
-- vim.list_extend(lvim.lsp.override, { "pyright" })

-- ---@usage setup a server -- see: https://www.lunarvim.org/languages/#overriding-the-default-configuration
-- local opts = {} -- check the lspconfig documentation for a list of all possible options
-- require("lvim.lsp.manager").setup("pylsp", opts)

-- you can set a custom on_attach function that will be used for all the language servers
-- See <https://github.com/neovim/nvim-lspconfig#keybindings-and-completion>
-- lvim.lsp.on_attach_callback = function(client, bufnr)
--   local function buf_set_option(...)
--     vim.api.nvim_buf_set_option(bufnr, ...)
--   end
--   --Enable completion triggered by <c-x><c-o>
--   buf_set_option("omnifunc", "v:lua.vim.lsp.omnifunc")
-- end
-- you can overwrite the null_ls setup table (useful for setting the root_dir function)
-- lvim.lsp.null_ls.setup = {
--   root_dir = require("lspconfig").util.root_pattern("Makefile", ".git", "node_modules"),
-- }
-- or if you need something more advanced
-- lvim.lsp.null_ls.setup.root_dir = function(fname)
--   if vim.bo.filetype == "javascript" then
--     return require("lspconfig/util").root_pattern("Makefile", ".git", "node_modules")(fname)
--       or require("lspconfig/util").path.dirname(fname)
--   elseif vim.bo.filetype == "php" then
--     return require("lspconfig/util").root_pattern("Makefile", ".git", "composer.json")(fname) or vim.fn.getcwd()
--   else
--     return require("lspconfig/util").root_pattern("Makefile", ".git")(fname) or require("lspconfig/util").path.dirname(fname)
--   end
-- end

-- -- set a formatter, this will override the language server formatting capabilities (if it exists)
local formatters = require "lvim.lsp.null-ls.formatters"
formatters.setup {
  { exe = "black", args = {"--line-length", "80"} },
  {
    exe = "prettier",
    args = {},
    ---@usage specify which filetypes to enable. By default a providers will attach to all the filetypes it supports.
    filetypes = { "typescript", "typescriptreact", "javascript", "javascriptreact"  },
  },
  -- { exe = "prettier", filetypes = {"html", "htmldjango"}, args = {"--print-width=160"} },
}

-- -- set additional linters
local linters = require "lvim.lsp.null-ls.linters"
linters.setup {
  { exe = "flake8",
    args = {
      "--max-line-length=80",
      "--ignore=E203,W503",
    } 
  },
  {
    exe = "eslint_d",
    ---@usage specify which filetypes to enable. By default a providers will attach to all the filetypes it supports.
    filetypes = { "javascript", "javascriptreact", "typescript", "typescriptreact" },
  },
}

-- Additional Plugins
lvim.plugins = {
    {"folke/tokyonight.nvim"},
    {"Shatur/neovim-ayu"},
    {"sainnhe/sonokai"},
    {
      "folke/trouble.nvim",
      cmd = "TroubleToggle",
    },
    {
      "norcalli/nvim-colorizer.lua",
        config = function()
          require("colorizer").setup({ "*" }, {
              RGB = true, -- #RGB hex codes
              RRGGBB = true, -- #RRGGBB hex codes
              RRGGBBAA = true, -- #RRGGBBAA hex codes
              rgb_fn = true, -- CSS rgb() and rgba() functions
              hsl_fn = true, -- CSS hsl() and hsla() functions
              css = true, -- Enable all CSS features: rgb_fn, hsl_fn, names, RGB, RRGGBB
              css_fn = true, -- Enable all CSS *functions*: rgb_fn, hsl_fn
              })
      end,
    },
    {
      -- jump anywhere in the file
      "phaazon/hop.nvim",
      event = "BufRead",
      config = function()
        require("hop").setup()
        vim.api.nvim_set_keymap("n", "s", ":HopChar2<cr>", { silent = true })
        vim.api.nvim_set_keymap("n", "S", ":HopWord<cr>", { silent = true })
      end,
    },
    -- flutter plugins
  {'akinsho/flutter-tools.nvim', requires = 'nvim-lua/plenary.nvim'}
}

-- Autocommands (https://neovim.io/doc/user/autocmd.html)
-- lvim.autocommands.custom_groups = {
--   { "BufWinEnter", "*.lua", "setlocal ts=8 sw=8" },
-- }

-- ~ Add-ons AA
vim.opt.spell = false
vim.opt.cmdheight = 1 -- default is 2
vim.opt.timeoutlen = 250
vim.opt.relativenumber = false
vim.opt.cursorline = true -- highlight the current line

lvim.transparent_window = false
lvim.lsp.diagnostics.virtual_text = false -- disable line shown errors
lvim.builtin.project.manual_mode = true -- disable changing root directory
lvim.builtin.lualine.options.theme = "auto"
lvim.builtin.telescope.defaults.file_ignore_patterns = { "node_modules", ".gitignore" }
lvim.builtin.nvimtree.show_icons.git = 0

require'luasnip'.filetype_extend("python", {"django"})

-- themes options
vim.cmd("let g:sonokai_style = 'andromeda'") -- values: `'default'`, `'atlantis'`, `'andromeda'`, `'shusia'`, `'maia'`, `'espresso'`

-- lsp configurations
require'lspconfig'.tsserver.setup{
  cmd = { "typescript-language-server", "--stdio" },
  filetypes = { "javascript", "javascriptreact", "javascript.jsx", "typescript", "typescriptreact", "typescript.tsx" },
  on_attach = function(client, bufnr)
      -- we use null-ls formatter
      client.resolved_capabilities.document_formatting = false
  end,  
}

require("flutter-tools").setup{}


 
-- lvim.builtin.nvimtree.setup.filters.custom = { ".git", "node_modules", ".cache" }
lvim.builtin.nvimtree.setup.filters.custom = { ".git", "node_modules", ".cache", "__pycache__", ".gitignore" }
require("nvim-web-devicons").set_icon {
  ["sqlite3"] = {
    icon = "",
    color = "#ff9e03",
    cterm_color = "65",
    name = "sqlite3"
  },
}

