local opts = {noremap = true, silent = true}
local keymap = vim.api.nvim_set_keymap

vim.g.mapleader = " "
vim.g.maplocalleader = " "


keymap("n", "<leader>w", ":w<cr>", opts) -- save file
keymap("n", "<leader>h", ":noh<cr>", opts) -- clear highlights
keymap("n", "<leader>c", ":bdelete<cr>", opts) -- close buffer
keymap("n", "<leader>e", ":NvimTreeToggle<cr>", opts)


-- buffer navigation
keymap("n", "<S-h>", ":bprevious<cr>", opts)
keymap("n", "<S-l>", ":bnext<cr>", opts)

keymap("i", "jk", "<Esc>", opts)
keymap("i", "kj", "<Esc>", opts)

keymap("n", "<C-d>", "<C-d>zz", opts) -- pgdown && center
keymap("n", "<C-u>", "<C-u>zz", opts) -- pgup && center
keymap("n", "n", "nzzzv", opts) -- search next && center
keymap("n", "N", "Nzzzv", opts) -- search previous && center


-- window navigation
keymap("n", "<C-h>", "<C-w>h", opts)
keymap("n", "<C-j>", "<C-w>j", opts)
keymap("n", "<C-k>", "<C-w>k", opts)
keymap("n", "<C-l>", "<C-w>l", opts)


-- resize windows
keymap("n", "<C-Up>", ":resize +2<cr>", opts)
keymap("n", "<C-Down>", ":resize -2<cr>", opts)
keymap("n", "<C-Left>", ":vertical resize -2<cr>", opts)
keymap("n", "<C-Right>", ":vertical resize +2<cr>", opts)


-- Move lines up and down
keymap("v", "<A-j>", ":m '>+1<CR>gv=gv", opts)
keymap("v", "<A-k>", ":m '<-2<CR>gv=gv", opts)
keymap("n", "<A-j>", "V:m '>+1<CR>gv=gv<Esc>", opts)
keymap("n", "<A-k>", "V:m '<-2<CR>gv=gv<Esc>", opts)
keymap("i", "<A-j>", "<Esc>V:m '>+1<CR>gv=gv<Esc>a", opts)
keymap("i", "<A-k>", "<Esc>V:m '<-2<CR>gv=gv<Esc>a", opts)


-- Change indentation && continue in VISUAL mode
keymap("v", ">", ">gv", opts)
keymap("v", "<", "<gv", opts)
