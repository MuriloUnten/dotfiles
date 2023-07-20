local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"

if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

local plugins = {
    require("config.plugins.telescope"),

    { "nvim-treesitter/nvim-treesitter", run = {":TSUpdate"}, },

    {
        'VonHeikemen/lsp-zero.nvim',
        branch = 'v2.x',
        dependencies = {
            -- LSP Support
            {'neovim/nvim-lspconfig'},             -- Required
            {                                      -- Optional
                'williamboman/mason.nvim',
                build = function()
                    pcall(vim.cmd, 'MasonUpdate')
                end,
            },
            {'williamboman/mason-lspconfig.nvim'}, -- Optional

            -- Autocompletion
            {'hrsh7th/nvim-cmp'},     -- Required
            {'hrsh7th/cmp-nvim-lsp'}, -- Required
            {'L3MON4D3/LuaSnip'},     -- Required
        }
    },

    { 'windwp/nvim-autopairs', event = "InsertEnter" },

    { 'numToStr/Comment.nvim', },

    {
        "nvim-tree/nvim-tree.lua",
        version = "*",
        lazy = false,
        dependencies = {
            "nvim-tree/nvim-web-devicons",
        },
    },

    {'akinsho/bufferline.nvim', version = "*", dependencies = 'nvim-tree/nvim-web-devicons'},

    {"lunarvim/colorschemes"},

    { "ellisonleao/gruvbox.nvim", priority = 1000 },

    { 'nvim-lualine/lualine.nvim', dependencies = 'nvim-tree/nvim-web-devicons' },

    {
        'goolord/alpha-nvim',
        event = "VimEnter",
        dependencies = { 'nvim-tree/nvim-web-devicons' },
    }
}
local opts = {}

require("lazy").setup(plugins, opts)
require("config.plugins.treesitter")
require("config.plugins.lsp")
require("config.plugins.autopairs")
require("config.plugins.comment")
require("config.plugins.nvimtree")
require("config.plugins.bufferline")
require("config.plugins.lualine")
require("config.plugins.alpha")
