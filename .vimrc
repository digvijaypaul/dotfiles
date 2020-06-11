" Sourced from /usr/share/vim/vim82/vimrc_example.vim 
source $VIMRUNTIME/vimrc_example.vim
source $HOME/.config/coc/coc.vim
"source $HOME/.vim/indentline_config.vim
"=== === === === === === === === My config === === === === === === === === ===

"_________________________ Page Formatting settings __________________________
"
set number              " shows the actual number for the line the cursor is 
set relativenumber      "   on, and relative number for the surrounding lines
set textwidth=78
set cursorline

"_____________________________ Cursor settings _______________________________
"
" The following is for VTE compatible terminals (urxvt, st, xterm, 
" gnome-terminal 3.x, Konsole KDE5 and others) and wsltty
" 1 -> blinking block
" 2 -> solid block
" 3 -> blinking underscore
" 4 -> solid underscore
" 5 -> blinking vertical bar
" 6 -> solid vertical bar 
let &t_SI = "\<Esc>[5 q"        " INSERT mode
let &t_SR = "\<Esc>[4 q"        " REPLACE mode
let &t_EI = "\<Esc>[2 q"        " NORMAL mode


"___________________________ Status bar settings _____________________________
"
set laststatus=2                        " makes the status bar permanent
set statusline=
set statusline+=%#SpellCap#             " color for the left side. Run :so $VIMRUNTIME/syntax/hitest.vim
set statusline+=\ %M                    " shows '+' if any changes have been made to the file
set statusline+=\ %y                    " shows the curent filetype
set statusline+=\ %F                    " shows full filepath of current file
set statusline+=%=                      " everything after this will be on the right side
set statusline+=%#WildMenu#             " color for the right side
set statusline+=\ %c:[%l/%L]            " shows the curent c:l/L [column:line/total_lines] 


"_______________________________ Key remapping _______________________________
"
" Remap localleader key from \ to ;. Used in vimtex 
let maplocalleader=";"

" Navigate splits using Ctrl + h/j/k/l instead of Ctrl + w -> Ctrl + h/j/k/l
nnoremap <C-h> <C-W>h		
nnoremap <C-j> <C-W>j
nnoremap <C-k> <C-W>k
nnoremap <C-l> <C-W>l
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

"_________________________________ Plugins ___________________________________
"
call plug#begin()

Plug 'preservim/nerdtree'
Plug 'joshdick/onedark.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-commentary'
Plug 'lervag/vimtex'
Plug 'drewtempelmeyer/palenight.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'chrisbra/Colorizer'

call plug#end()


"_______________________________ Color config ________________________________
"
set termguicolors               " enables vim truecolor support 
" set background=dark
colorscheme onedark


"____________________________ vimtex config __________________________________
"
let g:tex_flavor='latex'
let g:vimtex_view_method='zathura'
"let g:vimtex_fold_enabled = 1
