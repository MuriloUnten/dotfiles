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

from pathlib import Path
import subprocess
import socket


mod = "mod4"
terminal = guess_terminal()
fileManager = "nemo"
browser = "brave"
myFont = "FiraCode Nerd Font Bold"
hostname = socket.gethostname()


@hook.subscribe.startup
def autostart():
    script = Path("~/.config/qtile/autostart.sh").expanduser()
    subprocess.run(script)


def replace_window_name(text):
        windowIsBrave = text.find(" - Brave")
        if windowIsBrave != -1:
            text = "Brave"
        return text


keys = [
    Key([mod], "e", lazy.spawn(fileManager), desc="Open the file manager"),
    Key([mod], "b", lazy.spawn(browser), desc="launch browser"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Open rofi drun"),
    Key([mod], "o", lazy.spawn("obsidian"), desc="launch Obsidian"),
    Key([mod], "s", lazy.spawn("spotify-launcher"), desc="launch Spotify"),
    Key([mod], "d", lazy.spawn("discord"), desc="launch Discord"),

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
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "j", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "control"], "k", lazy.layout.grow(), desc="Grow window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_screen(), desc="Focus next screen"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    # Toggle between different layouts as defined below
    # Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
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
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = []

group_names = ["1", "2", "3", "4", "5"]
group_labels = ["", "", "", "", ""]
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
        border_focus=["#61afef00"],
        border_normal=["#282c3400"],
        border_width=2,
        margin=11,
        new_client_position="bottom"
    ),
    # layout.Columns(
    #     border_focus_stack=["#d75f5f", "#8f3d3d"],
    #     border_width=2,
    #     margin=6
    # ),
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
    # # Gruvbox
    # return [["#ebdbb2", "#ebdbb2"],  # color 0
    #         ["#282828cc", "#282828cc"],  # color 1
    #         ["#a89984", "#a89984"],  # color 2
    #         ["#a3be8c", "#a3be8c"],  # color 3
    #         ["#e2863f", "#e2863f"],  # color 4
    #         ["#d26d3f", "#d26d3f"],  # color 5
    #         ["#bf616a", "#bf616a"],  # color 6
    #         ["#81a1c1", "#81a1c1"],  # color 7
    #         ["#b48ead", "#b48ead"],  # color 8
    #         ["#d08770", "#d08770"]]  # color 9

    # Onedark
    return [["#282c34cc", "#282c34cc"],  # 0 (background)
            ["#abb2bf", "#abb2bf"],      # 1 (foreground)
            ["#e06c75", "#e06c75"],      # 2 (red)
            ["#98c379", "#98c379"],      # 3 (green)
            ["#e5c07b", "#e5c07b"],      # 4 (yellow)
            ["#61afef", "#61afef"],      # 5 (blue)
            ["#c678dd", "#c678dd"],      # 6 (magenta)
            ["#56b6c2", "#56b6c2"],      # 7 (cyan)
            ["#383c44", "#383c44"]]      # 8 (background 2 - grey)


colors = init_colors()


widget_defaults = dict(
    font=myFont,
    fontsize=14,
    padding=3,
    background=colors[1]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    separator0 = widget.Sep(
            linewidth=0,
            padding=0,
            foreground=colors[0],
            background=colors[0]
        )

    separator10 = widget.Sep(
            linewidth=1,
            padding=10,
            foreground=colors[0],
            background=colors[0]
        )
    separator15 = widget.Sep(
            linewidth=1,
            padding=15,
            foreground=colors[0],
            background=colors[0]
        )

    if hostname == "arch-laptop":
        batteryIcon = widget.BatteryIcon(
                theme_path='~/.config/qtile/assets/battery/',
                background=colors[0],
                scale=1,
                )

        battery = widget.Battery(
                font=myFont,
                fontsize=13,
                background=colors[0],
                foreground=colors[1],
                format="{percent:2.0%}",
                update_interval=10,
                )
        batterySep = separator10
    else:
        batteryIcon = separator0
        battery = separator0
        batterySep = separator0

    widgets_list = [
        separator10,
        widget.GroupBox(
            font="FiraCode Nerd Font Semi Bold",
            fontsize=22,
            margin_y=2,
            margin_x=5,
            padding_y=2,
            padding_x=1,
            borderwidth=5,
            disable_drag=True,
            active=colors[5],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[6],
            highlight_method="text",
            this_current_screen_border=colors[6],
            foreground=colors[1],
            background=colors[0],
        ),
        separator10,
        widget.WindowName(
            font=myFont,
            fontsize=14,
            foreground=colors[1],
            background=colors[0],
            parse_text=replace_window_name,
        ),
        separator10,
        widget.TextBox(
            text=" ",
            background=colors[0],
            foreground=colors[5],
            font=myFont,
            fontsize=14,
            decorations=[
                RectDecoration(
                    colour=colors[8],
                    padding_y=2,
                    radius=[12, 0, 0, 12],
                    filled=True,
                ),
            ],
        ),
        widget.CPU(
            format= ' {load_percent}% |',
            background=colors[0],
            foreground=colors[1],
            font=myFont,
            fontsize=14,
            decorations=[
                RectDecoration(
                    colour=colors[8],
                    padding_y=2,
                    radius=0,
                    filled=True,
                ),
            ],
        ),
        widget.TextBox(
            text="",
            background=colors[0],
            foreground=colors[2],
            font=myFont,
            fontsize=14,
            decorations=[
                RectDecoration(
                    colour=colors[8],
                    padding_y=2,
                    radius=0,
                    filled=True,
                ),
            ],
        ),
        widget.ThermalSensor(
            foreground=colors[1],
            background=colors[0],
            threshold=90,
            fmt='{} |',
            padding=5,
            decorations=[
                RectDecoration(
                    colour=colors[8],
                    padding_y=2,
                    radius=0,
                    filled=True,
                ),
            ],
        ),
        widget.TextBox(
            text="",
            background=colors[0],
            foreground=colors[5],
            font=myFont,
            fontsize=14,
            decorations=[
                RectDecoration(
                    colour=colors[8],
                    padding_y=2,
                    radius=0,
                    filled=True,
                ),
            ],
        ),
        widget.Memory(
            format='{MemUsed: .0f}{mm}',
            foreground=colors[1],
            background=colors[0],
            font=myFont,
            fontsize=14,
            fmt='{} ',
            decorations=[
                RectDecoration(
                    colour=colors[8],
                    padding_y=2,
                    radius=[0, 12, 12, 0],
                    filled=True,
                ),
            ],
        ),
        separator15,
        batteryIcon,
        battery,
        batterySep,
        widget.Volume(
            foreground=colors[1],
            background=colors[0],
            font=myFont,
            theme_path='~/.config/qtile/assets/volume/',
            emoji=True,
            fontsize=14,
        ),
        widget.Volume(
             foreground=colors[1],
             background=colors[0],
             fontsize=14,
             font=myFont,
             fmt='{}',
             padding=0,
        ),
        separator15,
        widget.TextBox(
            text="󰃭",
            background=colors[0],
            foreground=colors[5],
            font=myFont,
            fontsize=18,
        ),
        widget.Clock(
            foreground=colors[1],
            background=colors[0],
            fontsize=14,
            font=myFont,
            format=" %d/%m/%y ",
        ),
        widget.Clock(
            foreground=colors[1],
            background=colors[0],
            fontsize=14,
            font=myFont,
            format=" 󰥔 %H:%M ",
            decorations=[
                RectDecoration(
                    colour=colors[8],
                    padding_y=2,
                    radius=12,
                    filled=True,
                ),
            ],
        ),
        separator15,
    ]
    return widgets_list


screens = [
    Screen(
        top=bar.Bar(
            widgets=init_widgets_list(),
            size=28,
            background="#282c34ff",
            margin=[10, 11, -4, 11],
            opacity=1.0
        )
    ),
    Screen(
        top=bar.Bar(
            widgets=init_widgets_list(),
            size=22,
            background="#282c34ff",
            margin=[10, 11, -4, 11],
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
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=2,
    border_focus=colors[5],
    border_normal=colors[0],
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
