return {
    "epwalsh/obsidian.nvim",
    version = "*",  -- recommended, use latest release instead of latest commit
    lazy = true,
    ft = "markdown",
    -- Replace the above line with this if you only want to load obsidian.nvim for markdown files in your vault:
    -- event = {
        --   -- If you want to use the home shortcut '~' here you need to call 'vim.fn.expand'.
        --   -- E.g. "BufReadPre " .. vim.fn.expand "~" .. "/my-vault/*.md"
        --   -- refer to `:h file-pattern` for more examples
        --   "BufReadPre path/to/my-vault/*.md",
        --   "BufNewFile path/to/my-vault/*.md",
        -- },
    dependencies = {
        "nvim-lua/plenary.nvim",
        "hrsh7th/nvim-cmp",
        "nvim-telescope/telescope.nvim"
    },
    opts = {

    },
    config = function ()
        require('obsidian').setup({
            workspaces = {
                {
                    name = "personal",
                    path = "~/Obsidian/murilo",
                },
            },

            ui = { enable = false },

            daily_notes = {
                folder = "daily-notes/",
                date_format = "%Y-%m-%d",
                -- Optional, if you want to change the date format of the default alias of daily notes.
                alias_format = "%B %-d, %Y",
                default_tags = { "daily-notes", "notes" },
                -- Optional, if you want to automatically insert a template from your template directory like 'daily.md'
                template = nil -- TODO add template for daily note
            },

            completion = {
                nvim_cmp = true,
                min_chars = 2,
            },

            mappings = {
                ["gf"] = {
                    action = function()
                        return require("obsidian").util.gf_passthrough()
                    end,
                    opts = { noremap = false, expr = true, buffer = true },
                },
                ["<leader>ch"] = {
                    action = function()
                        return require("obsidian").util.toggle_checkbox()
                    end,
                    opts = { buffer = true },
                },
            },

            preferred_link_style = "wiki",

            templates = {
                folder = "templates",
                date_format = "%Y-%m-%d",
                time_format = "%H:%M",
                -- A map for custom variables, the key should be the variable and the value a function
                substitutions = {},
            },

            ---@param url string
            follow_url_func = function(url)
                vim.fn.jobstart({"xdg-open", url})  -- linux
            end,

            picker = {
                name = "telescope.nvim",
                note_mappings = {
                    -- Create a new note from your query.
                    new = "<localleader>nn",
                    -- Insert a link to the selected note.
                    insert_link = "<localleader>nl",
                },
            },

            -- Optional, customize how note file names are generated given the ID, target directory, and title.
            ---@param spec { id: string, dir: obsidian.Path, title: string|? }
            ---@return string|obsidian.Path
            note_path_func = function(spec)
                local path = spec.dir / tostring(spec.title)
                return path:with_suffix(".md")
            end,

            wiki_link_func = "use_path_only",
            markdown_link_func = "use_path_only",

        })
    end
}
