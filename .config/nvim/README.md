# Neovim config
I attempt to keep one config file for both vim and neovim.
## Import .vimrc config to init.vim
See `:h nvim-from-vim` for info.
## Import Coc settings from .vim folder
Symlink `coc-settings.json` from `~/.vim`:
```
ln -s ~/.vim/coc-settings.json ~/.config/nvim/coc-settings.json
```
