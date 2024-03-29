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

from libqtile.config import DropDown, Key, Screen, Group, Drag, Click, Match, ScratchPad
from libqtile.command import lazy
from libqtile import bar, widget, hook
# Import layout objects
# qtile documentation seems to be outdated. To find out where to import from,
# search the layout in the documentation and select its source. At the top of 
# source page, it will say "Source code for libqtile.layout.xyz"
from libqtile.layout.xmonad import MonadTall, MonadWide
from libqtile.layout.floating import Floating
from libqtile.layout.ratiotile import RatioTile
from libqtile.layout.bsp import Bsp
# The following libraries and `hook` above are used to call the autostart.sh
# file
import os
import subprocess

from typing import List  # noqa: F401

mod     = "mod4"
term    = "kitty"
browser = "firefox"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "k", lazy.layout.up(), 
        desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus left"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus right"),

    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        desc="Move window to the left stack"),
    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc="Move window to the right stack"),

    # Resize windows
    Key([mod], "equal", lazy.layout.grow(),
        desc="Increase the size of a window"),
    Key([mod], "minus", lazy.layout.shrink(),
        desc="Decrease the size of a window"),
    Key([mod, "shift"], "equal", lazy.layout.maximize(),
        desc="Maximize the size of a window"),
    Key([mod, "shift"], "minus", lazy.layout.reset(),
        desc="Reset the size of all windows"),

    # Switch window focus to other pane(s) of stack
    # Key([mod], "space", lazy.layout.next()),

    # Launch rofi with drun modi
    Key([mod], "space", lazy.spawn("rofi -show drun"),
        desc="Launch rofi"),

    # Swap panes of split stack
    # Key([mod, "shift"], "space", lazy.layout.rotate()),
    # Flip layout
    Key([mod, "shift"], "space", lazy.layout.flip(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Launch a terminal window 
    Key([mod], "Return", lazy.spawn(term), desc="Launch terminal (kitty)"),

    # Launch a browser
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser (firefox)"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # System binds
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # Key([mod], "r", lazy.spawncmd(),
    #     desc="Spawn a command using a prompt widget"),

   # Toggle modes other than tiling mode 
    Key([mod], "m", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod], "z", lazy.window.toggle_floating(),
        desc="Toggle floating mode"),
]

groups = [Group(i) for i in "asdfuiop"]

# Put One-Dark hex-codes in a dictionary to easily specify colors 
onedark = {
    "black":         "#282C34",
    "white":         "#ABB2BF",
    "light_red":     "#E06C75",
    "dark_red":      "#BE5046",
    "green":         "#98C379",
    "yellow":        "#E5C07B",
    "orange":        "#D19A66",
    "blue":          "#61AEFF",
    "purple":        "#C678DD",
    "cyan":          "#56B6C2",
    "gutter_grey":   "#4B5263",
    "comment_grey":  "#5C6370"
}


# This is to call the `autostart.sh` file
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('quake', term, x=0.25, y=0.15, height=0.7, width=0.5)
    ]))

# Extend keys list for navigating scratchpads
keys.extend([
    Key([mod], 'grave', lazy.group['scratchpad'].dropdown_toggle('quake'), 
        desc="Toggle a floating terminal window")
    ])

layouts = [
    # layout.Max(),
    MonadTall(border_focus=onedark["blue"],
                     border_normal=onedark["black"],
                     border_width=1,
                     single_border_width=0,
                     margin=10),
    MonadWide(border_focus=onedark["blue"],
                     border_normal=onedark["white"],
                     border_width=1,
                     margin=10),
    Bsp(border_focus=onedark["light_red"],
               border_normal=onedark["black"],
               border_width=1,
               margin=5,
               fair=False),
    RatioTile(border_focus=onedark["light_red"],
                     border_normal=onedark["black"],
                     border_width=1,
                     margin=5),
]

widget_defaults = dict(
    # Changing font from default 'sans' made the text appear more centered 
    # instead of slightly too high in the bar
    font="JetBrainsMono Nerd Font Bold",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(background=onedark["gutter_grey"]),
                widget.CurrentLayout(background=onedark["gutter_grey"],
                                     foreground=onedark["orange"],),
                widget.GroupBox(background=onedark["comment_grey"],
                                font="JetBrainsMono medium",
                                highlight_method="line",
                                highlight_color=[onedark["green"],
                                                 onedark["green"]],
                                this_current_screen_border=onedark["green"],
                                margin_x=0,
                                margin_y=5,
                                inactive=onedark["black"],
                                urgent_border=onedark["dark_red"]),
                widget.WindowName(background=onedark["black"],
                                  foreground=onedark["white"],
                                  font="JetBrains Mono Medium"),
                widget.CheckUpdates(background=onedark["orange"],
                                    foreground=onedark["black"],
                                    distro='Arch',
                                    colour_have_updates=onedark["black"],
                                    execute='doas pacman -Syu'),
                widget.CapsNumLockIndicator(background=onedark["comment_grey"],
                                            foreground=onedark["white"],
                                            font="JetBrains Mono Medium"),
                widget.Volume(background=onedark["gutter_grey"],
                              foreground=onedark["purple"]),
                widget.Systray(),
                widget.Clock(background=onedark["gutter_grey"],
                             foreground=onedark["blue"],
                             format='%Y-%m-%d %a %H:%M:%S')
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
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = Floating(
    border_focus=onedark['cyan'],
    border_normal=onedark['black'],
    opacity=1,
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
