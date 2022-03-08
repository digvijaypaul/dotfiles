# dotfiles
A collection of my dotfiles and configs

## Operating System
This configuration has been done mainly on a Manjaro KDE installation, though these files should work with any distro or even Mac. I installed first i3 and then qtile.The latter is what is currently being used and updated. I imagine doing an installation without a preexisting desktop environment would require quite a bit more configuration including icon sets/cursor packs etc.

## Packages used
- [bash](https://www.gnu.org/software/bash/)
- [vim](https://www.vim.org/) or [neovim](https://neovim.io/)
- [i3-gaps](https://github.com/Airblader/i3) (Switched to qtile)
- [polybar](https://polybar.github.io/) (Switched to qtile)
- [qtile](http://www.qtile.org/)
- [zathura](https://pwmt.org/projects/zathura/)
- [LaTeX](https://www.latex-project.org/)
- [nodejs](https://nodejs.org/en/) (used by vim plugin CoC) 
- [yarn](https://yarnpkg.com/) (used by vim plugin CoC) 
- [kitty](https://sw.kovidgoyal.net/kitty/)
- [joplin-terminal](https://joplinapp.org/terminal/)
- [rofi](https://github.com/davatorium/rofi)
- [ranger](https://github.com/ranger/ranger)
- [picom](https://github.com/yshui/picom)
- [fish](https://fishshell.com/)
- [JetBrains Mono](https://www.jetbrains.com/lp/mono/) (optionally, the Nerd Font patched version for ranger devicons)

### Neovim 
~~I attempt to keep one config file for both vim and neovim.~~
~~#### Import .vimrc config to init.vim~~
~~See `:h nvim-from-vim` for info.~~
~~#### Import Coc settings from .vim folder~~
~~Symlink `coc-settings.json` from `~/.vim` to `~.config/nvim`:~~
```bash
ln -s ~/.vim/coc-settings.json ~/.config/nvim/coc-settings.json
```
#### Coloring issue
There is an issue in neovim but not in vim where if you change the colorscheme while editing a file and change back to the original colorscheme, some text loses their syntax highlighting. Switching from `joshdick/one-dark.vim` and `drewtemplemeyer/palenight.vim` to `srcery-colors/srcery-vim` or `arcticicestudio/nord-vim` causes this to happen but switching between the former two does not. 

Another issue that occured in both vim and neovim: It seems that the installation of `srcery-vim` messed up some other syntax highlighting. In the part of the `.vimrc` that lists all the plugins, the name of the plugins contained in `' '` are not colored green. Uninstalling and reinstalling neovim fixed this, though it may be best to just remove `srcery-colors/srcery-vim`. **(REMOVED)**

#### Coc 
**Plugins used**
- coc-pyright
- coc-vimtex
- coc-r-lsp
	- Requires the [R Language Server](https://github.com/REditorSupport/languageserver) which can be obtained from CRAN. At the R prompt:
		```r
		install.packages("languageserver")
		```
		*Note:* Installing R packages requires the [tk](https://archlinux.org/packages/?name=tk) package to be installed.

### Qtile 
#### Autostart
The `autostart.sh` file is used to set the wallpaper on boot. When creating a shell
script it must be made into an executable file. This can be done by:
```bash
chmod +x path/to/file
```
in our case,
```bash
chmod +x ~/.config/qtile/autostart.sh
```

### Zathura
#### Plugins
For zathura to display any file it needs the requisite plugin to also be installed.
e.g. 
- `zathura-pdf-poppler` or `zathura-pdf-mupdf` (what I use) plugin for viewing PDFs.
- `zatura-cb` for viewing comic books

### Kitty
#### Themes
I use the OneDark theme from the [dexpota/kitty-themes](https://github.com/dexpota/kitty-themes) repository.
#### Theming
I have enabled transparency to use picom's blur. I use the [JetBrains Mono](https://www.jetbrains.com/lp/mono/) font family.

### Ranger
#### Devicons
Install this [plugin](https://github.com/alexanderjeurissen/ranger_devicons) to prefix file names with devicons using glyphs from a Nerd Font patched font.

### Fish
#### Config
Adding lines to `.config/fish/fish_config` only saves it to `.config/fish/fish_variables`, so if you edit for example, an abbreviation in `fish_config`, both the old and the edited abbreviation will exist in the `fish_variables` file and will have to be manually deleted :roll_eyes:.
#### Theming
Fish uses the terminal's color scheme for the prompt colors and output highlighting. In my case kitty is using the OneDark colorscheme.
For syntax highlighting user inputs, the colors have to be set in `.config/fish/fish_variables`.
#### Give fish the OneDark treatment
Instead of OneDark, I use fish's built in Nord theme (by entering `fish_config` at the prompt). This makes it so that the prompt colors and output highlights are easily distinguishable from user input highlighting.
However, it *is* possible to manually change the colors to the OneDark theme.

Swap out the corresponding lines in `.config/fish/fish_variables` for the following:
```config
SETUVAR fish_color_autosuggestion:4B5263
SETUVAR fish_color_command:61AEFF
SETUVAR fish_color_comment:5C6370
SETUVAR fish_color_end:C678DD
SETUVAR fish_color_error:E5C07B
SETUVAR fish_color_escape:56B6C2
SETUVAR fish_color_operator:56B6C2
SETUVAR fish_color_param:ABB2BF
SETUVAR fish_color_quote:98C379
SETUVAR fish_color_redirection:BE5046
```
> Here are the Hex codes for easy viewing using the [colorizer](https://github.com/chrisbra/Colorizer) vim plugin
> #4B5263
> #61AEFF
> #5C6370
> #C678DD
> #E5C07B
> #56B6C2
> #56B6C2
> #ABB2BF
> #98C379

### JetBrains Mono
A nice monospaced font with ligatures.
#### Kitty
I use the Nerd Font patched version from the AUR in Kitty so that ranger can make use of it's devicons. In the config file I simply specify the font family to `JetBrains Mono` and it seems to use the Nerd Font one  automatically(??). I don't need to specify for each **bold**, *italic* or ***bold italic***.
#### Qtile
The package from the Manjaro repo is easiest to use for qtile configuration.
I can't get The Nerd Font version to work reliably particularly in the `GroupBox` widget. I have trouble with setting `JetBrains Mono Bold` (non Nerd Font) in that widget as well.

