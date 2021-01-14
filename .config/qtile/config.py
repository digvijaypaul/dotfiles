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

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
# The following libraries and `hook` above are used to call the autostart.sh
# file
import os
import subprocess

from typing import List  # noqa: F401

mod = "mod4"
term = "kitty"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),

    # Switch window focus to other pane(s) of stack
    # Key([mod], "space", lazy.layout.next()),

    # Launch rofi with drun modi
    Key([mod], "space", lazy.spawn("rofi -show drun")),

    # Swap panes of split stack
    # Key([mod, "shift"], "space", lazy.layout.rotate()),
    # Flip layout
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Launch a terminal window 
    Key([mod], "Return", lazy.spawn(term)),

    # Launch a browser
    Key([mod], "b", lazy.spawn("firefox")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "m", lazy.window.toggle_fullscreen()),
    Key([mod], "z", lazy.window.toggle_floating()),
]

groups = [Group(i) for i in "asdfuiop"]

# Put One-Dark hex-codes in a dictionary to easily specify colors 
colors = {
        "dark_grey": "#282C34",
        "red": "#E06C75",
        "green": "#98C379",
        "yellow": "#E5C07B",
        "blue": "#61AEFF",
        "purple": "#C678DD",
        "teal": "#56B6C2",
        "light_grey": "#ABB2BF"
}

# This is to call the `autostart.sh` file
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    # layout.Max(),
    layout.MonadTall(border_focus=colors["blue"],
        border_normal=colors["light_grey"],
        margin=15),
    layout.MonadWide(border_focus=colors["blue"],
        border_normal=colors["light_grey"], margin=15),
    layout.Bsp(fair=False, margin=5),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(background=colors["yellow"],
                    foreground=colors["dark_grey"]),
                widget.CurrentLayout(background=colors["yellow"],
                    foreground=colors["dark_grey"]),
                widget.GroupBox(background=colors["green"],
                    foreground=colors["light_grey"], 
                    highlight_method="line",
                    highlight_color=[colors["green"],
                        colors["purple"]], 
                    inactive=colors["dark_grey"]),
                # widget.Sep(),
                widget.WindowName(background=colors["dark_grey"],
                    foreground=colors["light_grey"]),
                # widget.TextBox("default config", name="default"),
                # widget.Sep(),
                widget.CheckUpdates(background=colors["light_grey"]),
                # widget.CapsNumLockIndicator(background=colors["red"]),
                widget.Volume(background=colors["purple"]),
                widget.Systray(),
                widget.Clock(background=colors["blue"],
                foreground=colors["dark_grey"], format='%Y-%m-%d %a %H:%M:%S'),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None 
follow_mouse_focus = True 
bring_front_click = False 
cursor_warp = False 
floating_layout = layout.Floating(float_rules=[ {'wmclass': 'confirm'}, {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
