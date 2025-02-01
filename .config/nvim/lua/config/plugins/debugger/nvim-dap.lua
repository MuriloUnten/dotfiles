return {
    "mfussenegger/nvim-dap",
    dependencies = {
        "rcarriga/nvim-dap-ui",
        "leoluz/nvim-dap-go"
    },
    config = function ()
        local dap = require("dap")
        local dapui = require("dapui")
        local opts = {}

        require("dap-go").setup()

        opts.desc = "Debugger toggle breakpoint"
        vim.keymap.set("n", "<leader>dt", dap.toggle_breakpoint, opts)

        opts.desc = "Debugger continue"
        vim.keymap.set("n", "<leader>dc", dap.continue, opts)

        opts.desc = "Debugger step into"
        vim.keymap.set("n", "<leader>di", dap.step_into, opts)

        opts.desc = "Debugger step over"
        vim.keymap.set("n", "<leader>do", dap.step_over, opts)

        opts.desc = "Debugger step out"
        vim.keymap.set("n", "<leader>dq", dap.step_out, opts)

        dap.listeners.before.attach.dapui_config = function()
            dapui.open()
        end
        dap.listeners.before.launch.dapui_config = function()
            dapui.open()
        end
        dap.listeners.before.event_terminated.dapui_config = function()
            dapui.close()
        end
        dap.listeners.before.event_exited.dapui_config = function()
            dapui.close()
        end

    end,
}
