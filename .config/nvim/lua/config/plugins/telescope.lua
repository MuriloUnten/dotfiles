return
{
    'nvim-telescope/telescope.nvim',
    tag = '0.1.2',
    dependencies = { 'nvim-lua/plenary.nvim' },
    keys = {
        { "<leader>ff", ":Telescope find_files<cr>", "n", {} },
        { "<leader>fg", ":Telescope live_grep<cr>", "n", {} },
        { "<leader>fb", ":Telescope buffers<cr>", "n", {} },
    },
}
