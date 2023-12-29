return {
    'numToStr/Comment.nvim', 
    lazy = false,
    config = function()
        require("Comment").setup({
            padding = true,
            sticky = true, --Whether the cursor should stay at its position
            ignore = nil, --Lines to be ignored while (un)comment

            ---LHS of toggle mappings in NORMAL mode
            toggler = {
                ---Line-comment toggle keymap
                line = 'gcc',
                ---Block-comment toggle keymap
                block = 'gbc',
            },
            ---LHS of operator-pending mappings in NORMAL and VISUAL mode
            opleader = {
                ---Line-comment keymap
                line = 'gc',
                ---Block-comment keymap
                block = 'gb',
            },
            mappings = { basic = true, extra = false },
        })
    end
}
