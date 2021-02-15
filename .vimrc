" Sourced from /usr/share/vim/vim82/vimrc_example.vim
if !has('nvim')
    source $VIMRUNTIME/vimrc_example.vim
endif

source $HOME/.config/coc/coc.vim
"=== === === === === === === === My config === === === === === === === === ===
"
set noswapfile
set nobackup

"_________________________ Page Formatting settings ___________________________
"
set number              " shows the actual number for the line the cursor is 
set relativenumber      "   on, and relative number for the surrounding lines
" set wrap               " Vim and neovim seem to wrap by default 
set linebreak           " breaks lines at end of word instead of in the middle
set colorcolumn=80
" set cursorline
set tabstop=4 softtabstop=4 expandtab
set scrolloff=12
set splitbelow splitright   " Changes automatic positioning of split windows to 
                            "   bottom and right instead of top and left
                              
" Return to last cursor position when opening files 
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

"______________________________ Search settings _______________________________
"
" The following turns highlight search on only while searching, eliminating the
" need to manually run the command `:noh` after a search
augroup vimrc-incsearch-highlight
  autocmd!
  autocmd CmdlineEnter /,\? :set hlsearch
  autocmd CmdlineLeave /,\? :set nohlsearch
augroup END

set ignorecase
set smartcase
set incsearch

"______________________________ Cursor settings _______________________________
"
" The following is for VTE compatible terminals (urxvt, st, xterm, 
" gnome-terminal 3.x, Konsole KDE5 and others) and wsltty
" 1 -> blinking block
" 2 -> solid block
" 3 -> blinking underscore
" 4 -> solid underscore
" 5 -> blinking vertical bar
" 6 -> solid vertical bar 
if !has('nvim')
    let &t_SI = "\<Esc>[5 q"        " INSERT mode
    let &t_SR = "\<Esc>[4 q"        " REPLACE mode
    let &t_EI = "\<Esc>[2 q"        " NORMAL mode
endif    
" These settings are default in neovim

"____________________________ Status bar settings _____________________________
"
" This function will be called in the staurs line to get a list of counts of
" added, modified, and removed lines in the current buffer.
function! GitStatus()
  let [a, m, r] = GitGutterGetHunkSummary()
  return printf('+%d ~%d -%d', a, m, r)
endfunction

set laststatus=2                        " makes the status bar permanent

" To check available colors or highlighting for status bar elements, run 
" `:so $VIMRUNTIME/syntax/hitest.vim`. The elements that set the highlights
" are surrounded by the `#` symbol
set statusline=
set statusline+=%#Directory#
set statusline+=\ [%M]\                 " shows '+' if any changes have been made to the file
set statusline+=%#IncSearch#
set statusline+=\ %y\                   " shows the curent filetype
set statusline+=%#StatusLine#
set statusline+=\ %F                    " shows filepath of the file

set statusline+=%=                      " everything after this will be on the right side

set statusline+=%#Directory#
set statusline+=\ %{GitStatus()}
set statusline+=%#SpellCap#
set statusline+=\ ☰%l/%L:\ %c\          " shows the curent c:l/L [column:line/total_lines] 

"_________________________ Filetype specific settings _________________________
"
au FileType markdown set spell conceallevel=2 

"_______________________________ Key remappings _______________________________
"
" Remap localleader key from \ to ;. Used in vimtex and Nvim-R
let mapleader=","
let maplocalleader=";"

" Move up and down lines in a paragraph that doesn't have line breaks
nnoremap j gj
nnoremap k gk

" Navigate splits using Ctrl + h/j/k/l instead of Ctrl + w -> Ctrl + h/j/k/l
nnoremap <C-h> <C-W>h		
nnoremap <C-j> <C-W>j
nnoremap <C-k> <C-W>k
nnoremap <C-l> <C-W>l
" Make adjusting split sizes easier
noremap <silent> <C-Left> :vertical resize -5<CR>
noremap <silent> <C-Right> :vertical resize +5<CR>
noremap <silent> <C-Down> :resize +3<CR>
noremap <silent> <C-Up> :resize -3<CR>
" Toggle horizontal and vertical orientation of split windows
map <Leader>th <C-w>H
map <Leader>tk <C-w>K

" Write with ZZ
nnoremap ZZ :w<CR>
" Save and quit with Zz (default ZZ)
nnoremap Zz :wq<CR>
" Quit with zz
nnoremap zz :q<CR>

" Move lines up or down after visually selecting with Shift + j/k 
xnoremap J :move '>+1<CR>gv-gv
xnoremap K :move '<-2<CR>gv-gv

" Exit insert mode with jj
imap jj <Esc>

" Map ctrl + n to open NERDTree
map <C-n> :NERDTreeToggle<CR>

map <F1> :colorscheme onedark<CR>
map <F2> :colorscheme palenight<CR>
map <F3> :colorscheme nord<CR>

" Nvim-R binds
" Use Ctrl+Space to do omnicompletion:
"if has('nvim') || has('gui_running')
"    inoremap <C-Space> <C-x><C-o>
"else
"    inoremap <Nul> <C-x><C-o>
"endif

" Press the space bar to send lines and selection to R:
" nmap <Space> <Plug>RDSendLine
" vmap <Space> <Plug>RDSendSelection

"__________________________________ Plugins ___________________________________
"
" auto-install vim-plug
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall
  " autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin()

Plug 'preservim/nerdtree'
Plug 'joshdick/onedark.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-commentary'
Plug 'lervag/vimtex'
Plug 'drewtempelmeyer/palenight.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'chrisbra/Colorizer'
Plug 'tpope/vim-surround'
Plug 'sheerun/vim-polyglot'
Plug 'jalvesaq/Nvim-R', {'branch': 'stable'}
Plug 'airblade/vim-gitgutter'
Plug 'jiangmiao/auto-pairs'
" ^This plugin makes it so that when you delete the first character of a line
" it pulls the line below up. It also makes it so the pressing enter on a 
" commented line in insert mode doesn't automatially comment the new line out.
" This issue may only occur for vim files as they use `"` for comments which
" this plugin would try to pair
Plug 'junegunn/goyo.vim'
Plug 'mhinz/vim-startify'
Plug 'godlygeek/tabular'

call plug#end()

" Automatically install missing plugins on startup
autocmd VimEnter *
  \  if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \|   PlugInstall --sync | q
  \| endif

"________________________________ Color config ________________________________
"
set termguicolors               " enables vim truecolor support 
let g:onedark_terminal_italics=1
let g:palenight_terminal_italics=1
colorscheme onedark

"_______________________________ vimtex config ________________________________
"
let g:tex_flavor='latex'
let g:vimtex_view_method='zathura'
"let g:vimtex_fold_enabled = 1

"_____________________________ gitgutter config _______________________________
"
" This setting allows gitgutter to work on the dotfiles tracked in the bare
" git repository. I simply used the settings that were passed to the `config`
" alias in the .bashrc
let g:gitgutter_git_args='--git-dir=$HOME/.cfg --work-tree=$HOME'

"_________________________________ kitty fix __________________________________
" Scrolling in vim would make background disappear. Other solutions posted at 
" https://github.com/kovidgoyal/kitty/issues/108
" vim hardcodes background color erase even if the terminfo file does
        " not contain bce (not to mention that libvte based terminals
        " incorrectly contain bce in their terminfo files). This causes
        " incorrect background rendering when using a color theme with a
        " background color.
        " let &t_ut=''
" Fixed by changing kitty theme to match vim theme
