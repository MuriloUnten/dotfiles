require"nvim-treesitter.configs".setup {
    ensure_installed = { "c", "cpp", "javascript", "python", "lua", "vim", "vimdoc", "query", "latex", "yaml"},

    -- Install parsers synchronously (only applied to `ensure_installed`)
    sync_install = false,

    auto_install = true,

    highlight = {
    enable = true,
    },
}
