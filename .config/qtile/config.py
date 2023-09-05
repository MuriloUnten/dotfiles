# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -*- coding: utf-8 -*-

import psutil
from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Open rofi drun"),
    Key([mod], "b", lazy.spawn("brave"), desc="launch browser"),
    Key([mod], "o", lazy.spawn("obsidian"), desc="launch Obsidian"),

    Key([], "XF86MonBrightnessDown", lazy.spawn("brillo -q -U 5"), desc="decrease screeen brightness"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brillo -q -A 5"), desc="increase screeen brightness"),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc="toggle mute"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5"), desc="Lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +5"), desc="Raise volume"),

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "control"], "k", lazy.layout.grow(), desc="Grow window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_screen(), desc="Focus next screen"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = []

group_names = ["1", "2", "3", "4", "5"]
group_labels = ["", "󰾔", "󰭹", "󰎄", ""]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
            Group(
                name=group_names[i],
                layout=group_layouts[i],
                label=group_labels[i],
            )
    )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(
        border_focus=["#e2863f00"],
        border_normal=["#7f472e00"],
        border_width=3,
        margin=11,
        new_client_position="bottom"
    ),
    # layout.Columns(
    #     border_focus_stack=["#d75f5f", "#8f3d3d"],
    #     border_width=2,
    #     margin=6
    # ),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


def init_colors():
    return [["#ebdbb2", "#ebdbb2"],  # color 0
            ["#282828cc", "#282828cc"],  # color 1
            ["#a89984", "#a89984"],  # color 2
            ["#a3be8c", "#a3be8c"],  # color 3
            ["#e2863f", "#e2863f"],  # color 4
            ["#d26d3f", "#d26d3f"],  # color 5
            ["#bf616a", "#bf616a"],  # color 6
            ["#81a1c1", "#81a1c1"],  # color 7
            ["#b48ead", "#b48ead"],  # color 8
            ["#d08770", "#d08770"]]  # color 9


colors = init_colors()


widget_defaults = dict(
    font="JetBrainsMono Nerd Font bold",
    fontsize=14,
    padding=3,
    background=colors[1]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[1]
                        ),
               widget.CurrentLayoutIcon(
                        padding = 0,
                        scale = 0.6,
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[1]
                        ),
               widget.GroupBox(font="JetBrainsMono Nerd Font semi bold",
                        fontsize=20,
                        margin_y=2,
                        margin_x=10,
                        padding_y=2,
                        padding_x=1,
                        borderwidth=5,
                        disable_drag=True,
                        active=colors[0],
                        inactive=colors[2],
                        rounded=False,
                        highlight_color=colors[4],
                        highlight_method="text",
                        this_current_screen_border=colors[4],
                        foreground=colors[2],
                        background=colors[1],
                        # decorations = [
                        #     RectDecoration (
                        #         colour = colors[5],
                        #         padding_y = 2,
                        #         radius = 5,
                        #         filled = True
                        #     ),
                        # ],
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        background = colors[1],
                        foreground = colors[1],
                        ),
               widget.WindowName(font="JetBrainsMono Nerd Font bold",
                        fontsize = 14,
                        foreground = colors[0],
                        background = colors[1],
                        ),
               widget.Sep(
                        foreground = colors[1],
                        background = colors[1],
                        padding = 10,
                        linewidth = 1
                        ),
               widget.CPU(
                        format = '   {freq_current}GHz | {load_percent}% |',
                        background = colors[1],
                        foreground = colors[1],
                        font = "JetBrainsMono Nerd Font bold",
                        fontsize = 14,
                        decorations = [
                            RectDecoration (
                                colour = colors[4],
                                padding_y = 2,
                                radius = [5, 0, 0, 5],
                                filled = True
                            ),
                        ],
                        ),
               widget.ThermalSensor(
                        foreground = colors[1],
                        background = colors[1],
                        threshold = 90,
                        fmt = ' {} |',
                        padding = 5,
                        decorations = [
                            RectDecoration (
                                colour = colors[4],
                                padding_y = 2,
                                radius = 0,
                                filled = True
                            ),
                        ],
                        ),
               widget.Memory(
                        format = '{MemUsed: .0f}{mm}/{MemTotal:.0f}{mm}',
                        foreground = colors[1],
                        background = colors[1],
                        font = "JetBrainsMono Nerd Font bold",
                        fontsize = 14,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(guess_terminal() + ' -e htop')},
                        fmt = 'RAM:{} ',
                        decorations = [
                            RectDecoration (
                                colour = colors[4],
                                padding_y = 2,
                                radius = [0, 5, 5, 0],
                                filled = True
                                ),
                        ],
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[1]
                        ),
                widget.Battery(
                        full_char = "󰁹",
                        charge_char = "󰂄",
                        discharge_char = "󰂂",
                        font = "JetBrainsMono Nerd Font bold",
                        fontsize = 13,
                        background = colors[1],
                        foreground = colors[1],
                        format = " {char} {percent:2.0%}",
                        update_interval = 30,
                        decorations = [
                            RectDecoration (
                                colour = colors[5],
                                padding_y = 2,
                                radius = [5, 0, 0, 5],
                                filled = True
                                ),
                        ],
                        ),
               widget.Volume(
                        foreground = colors[1],
                        background = colors[1],
                        fmt = '| 󰕾 {} |',
                        padding = 5,
                        decorations = [
                            RectDecoration (
                                colour = colors[5],
                                padding_y = 2,
                                radius = 0,
                                filled = True
                                ),
                        ],
                        ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[1],
               #          background = colors[1]
               #          ),
               widget.Clock(
                        foreground = colors[1],
                        background = colors[1],
                        fontsize = 14,
                        font = "JetBrainsMono Nerd Font bold",
                        format="󰃭 %d/%m/%y | 󰥔 %H:%M ",
                        decorations = [
                            RectDecoration (
                                colour = colors[5],
                                padding_y = 2,
                                radius = [0, 5, 5, 0],
                                filled = True
                            ),
                        ],
                        ),
               #Spotify(
               #     foreground = colors[3],
               #     background = colors[1],
               #     font = 'JetBrainsMono Nerd Font bold Bold',
               #     fontsize = 13,
               #     play_icon = '>',
               #     pause_icon = 'x',
               #     format = '{icon} {artist}: {track}'
               #       ),
                # widget.UPowerWidget(
                #         border_colour = '#d8dee9',
                #         border_critical_colour = '#bf616a'
                #         ),
                # widget.Systray(
                #         background = colors[1],
                #         icon_size = 20,
                #         padding = 4
                #         ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[1]
                        ),
              ]
    return widgets_list

screens = [
    Screen(
        top=bar.Bar(
            widgets=init_widgets_list(),
            size=22,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background="#282828e5",
            margin=[7, 11, -4, 11],
            opacity=1.0
        )
    ),
    Screen(
        top=bar.Bar(
            widgets=init_widgets_list(),
            size=22,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background="#282828e5",
            margin=[7, 11, -4, 11],
            opacity=1.0
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
