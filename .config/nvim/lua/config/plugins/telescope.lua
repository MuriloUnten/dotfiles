return {
        'nvim-telescope/telescope.nvim',
        branch = '0.1.x',
        dependencies = {
            'nvim-lua/plenary.nvim',
            { "nvim-telescope/telescope-fzf-native.nvim", build = "make"},
            "nvim-tree/nvim-web-devicons",
        },
        config = function()
            local telescope = require("telescope")
            local actions = require("telescope.actions")
            telescope.setup({
                defaults = {
                    mappings = {
                        i = {
                            ["<C-k>"] = actions.move_selection_previous,
                            ["<C-j>"] = actions.move_selection_next,
                            ["<C-q>"] = actions.send_selected_to_qflist + actions.open_qflist,
                        }
                    }
                },
                pickers = {
                    -- Default configuration for builtin pickers goes here:
                    -- picker_name = {
                    --   picker_config_key = value,
                    --   ...
                    -- }
                    -- Now the picker_config_key will be applied every time you call this
                    -- builtin picker
                },
                extensions = {
                    -- Your extension configuration goes here:
                    -- extension_name = {
                    --   extension_config_key = value,
                    -- }
                    -- please take a look at the readme of the extension you want to configure
                }
            })

            telescope.load_extension("fzf")

            local builtinTelescope = require("telescope.builtin")
            local description = "Fuzzy find files in cwd"
            vim.keymap.set('n', '<leader>ff', builtinTelescope.find_files, {desc = description})
            description = "Find string in cwd"
            vim.keymap.set('n', '<leader>fs', builtinTelescope.live_grep, {desc = description})
            description = "Fuzzy find open buffers"
            vim.keymap.set('n', '<leader>fb', builtinTelescope.buffers, {desc = description})
            description = "Fuzzy find recent files"
            vim.keymap.set('n', '<leader>fr', builtinTelescope.oldfiles, {desc = description})
            description = "Find string under cursor in cwd"
            vim.keymap.set('n', '<leader>fh', builtinTelescope.grep_string, {desc = description})
        end,
}

