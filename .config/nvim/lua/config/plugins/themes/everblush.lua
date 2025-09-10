return {
    "Everblush/nvim",
    name = "everblush",
    lazy = false,
    priority = 1000, -- make sure to load this before all the other start plugins
    config = function()
        require('everblush').setup({
            -- override = {
                --     Normal = { fg = '#ffffff', bg = 'comment' },
                -- },

                -- Set transparent background
                transparent_background = false,

                -- Set contrast for nvim-tree highlights
                nvim_tree = {
                    contrast = true,
                },
        })
    end,

}
