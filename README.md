# dotfiles
A collection of my dotfiles and configs

## Packages used
- [bash](https://www.gnu.org/software/bash/)
- [vim](https://www.vim.org/) or [neovim](https://neovim.io/)
- [i3-gaps](https://github.com/Airblader/i3)
- [polybar](https://polybar.github.io/)
- [zathura](https://pwmt.org/projects/zathura/)
- [LaTeX](https://www.latex-project.org/)
- [nodejs](https://nodejs.org/en/) (used by vim plugin CoC) 
- [yarn](https://yarnpkg.com/) (used by vim plugin CoC) 
- [kitty](https://sw.kovidgoyal.net/kitty/)
- [joplin-terminal](https://joplinapp.org/terminal/)
- [rofi](https://github.com/davatorium/rofi)
- [ranger](https://github.com/ranger/ranger)

### Neovim 
I attempt to keep one config file for both vim and neovim.
#### Import .vimrc config to init.vim
See `:h nvim-from-vim` for info.
#### Import Coc settings from .vim folder
Symlink `coc-settings.json` from `~/.vim`:
```
ln -s ~/.vim/coc-settings.json ~/.config/nvim/coc-settings.json
```

### Coc 
#### Packages used
- coc-pyright
- coc-vimtex
- coc-r-lsp
	- Requires the [R Language Server](https://github.com/REditorSupport/languageserver) which can be obtained from CRAN:
		```
		install.packages("languageserver")
		```
		*Note:* Installing R packages requires the [tk](https://archlinux.org/packages/?name=tk) package to be installed.

### Qtile 
#### Autostart
The `autostart.sh` file is used to set the wallpaper on boot. When creating a shell
script it must be made into an executable file. This can be done by:
```
$ chmod +x path/to/file
```
in our case,
```
$ chmod +x ~/.config/qtile/autostart.sh
```

### Zathura
#### Plugins
For zathura to display any file it needs the requisite plugin to also be installed.
e.g. 
- `zathura-pdf-poppler` or `zathura-pdf-mupdf` (what I use) plugin for viewing PDFs.
- `zatura-cb` for viewing comic books
