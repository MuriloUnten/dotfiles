return {
    "benlubas/molten-nvim",
    version = "^1.0.0", -- use version <2.0.0 to avoid breaking changes
    dependencies = { "3rd/image.nvim" },
    build = ":UpdateRemotePlugins",
    init = function()
        -- these are examples, not defaults. Please see the readme
        vim.g.molten_image_provider = "image.nvim"
        vim.g.molten_output_win_max_height = 30
        vim.g.molten_image_location = "float"
        vim.g.molten_virt_text_output = true
        vim.g.molten_virt_lines_off_by_1 = true -- show output below ``` delimiter

        local opts = { desc = "", silent = true, }

        opts.desc = "evaluate operator"
        vim.keymap.set("n", "<localleader>ne", ":MoltenEvaluateOperator<CR>", opts)

        opts.desc = "open output window"
        vim.keymap.set("n", "<localleader>no", ":noautocmd MoltenEnterOutput<CR>", opts)

        opts.desc = "reevaluate cell"
        vim.keymap.set("n", "<localleader>nre", ":MoltenReevaluateCell<CR>", opts)

        opts.desc = "evaluate selection"
        vim.keymap.set("v", "<localleader>ne", ":MoltenReevaluateCell<CR>", opts)

    end,
}
