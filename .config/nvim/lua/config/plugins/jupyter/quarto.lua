return {
    "quarto-dev/quarto-nvim",
    dependencies = {
        "jmbuhr/otter.nvim",
        "nvim-treesitter/nvim-treesitter",
    },
    config = function()
        require('quarto').setup {
            debug = false,
            closePreviewOnExit = true,
            lspFeatures = {
                enabled = true,
                chunks = "all",
                languages = { "r", "python", "julia", "bash", "html" },
                diagnostics = {
                    enabled = true,
                    triggers = { "BufWritePost" },
                },
                completion = {
                    enabled = true,
                },
            },
            codeRunner = {
                enabled = false,
                default_method = "molten",
                never_run = { "yaml" },
            },
        }

        local runner = require("quarto.runner")
        vim.keymap.set("n", "<localleader>nrc", runner.run_cell,  { desc = "run cell", silent = true })
        vim.keymap.set("n", "<localleader>nra", runner.run_above, { desc = "run cell and above", silent = true })
        vim.keymap.set("n", "<localleader>nrA", runner.run_all,   { desc = "run all cells", silent = true })
        vim.keymap.set("n", "<localleader>nrl", runner.run_line,  { desc = "run line", silent = true })
        vim.keymap.set("v", "<localleader>nr",  runner.run_range, { desc = "run visual range", silent = true })
    end,
}
