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
    {import = "config.plugins"},
    {import = "config.plugins.lsp"},
}

local opts = {
    install = {
        colorscheme = {"onedark"},
    },
    checker = {
        enabled = true,
        notify = false,
    },
    rocks = {
        hererocks = true,
    },
}

require("lazy").setup(plugins, opts)
