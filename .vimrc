" The default vimrc file.
"
" Maintainer:	Bram Moolenaar <Bram@vim.org>
" Last change:	2019 Feb 18
"
" This is loaded if no vimrc file was found.
" Except when Vim is run with "-u NONE" or "-C".
" Individual settings can be reverted with ":set option&".
" Other commands can be reverted as mentioned below.

" When started as "evim", evim.vim will already have done these settings.
if v:progname =~? "evim"
  finish
endif

" Bail out if something that ran earlier, e.g. a system wide vimrc, does not
" want Vim to use these default values.
if exists('skip_defaults_vim')
  finish
endif

" Use Vim settings, rather than Vi settings (much better!).
" This must be first, because it changes other options as a side effect.
" Avoid side effects when it was already reset.
if &compatible
  set nocompatible
endif

" When the +eval feature is missing, the set command above will be skipped.
" Use a trick to reset compatible only when the +eval feature is missing.
silent! while 0
  set nocompatible
silent! endwhile

" Allow backspacing over everything in insert mode.
set backspace=indent,eol,start

set history=200		" keep 200 lines of command line history
set ruler		" show the cursor position all the time
set showcmd		" display incomplete commands
set wildmenu		" display completion matches in a status line

set ttimeout		" time out for key codes
set ttimeoutlen=100	" wait up to 100ms after Esc for special key

" Show @@@ in the last line if it is truncated.
set display=truncate

" Show a few lines of context around the cursor.  Note that this makes the
" text scroll if you mouse-click near the start or end of the window.
set scrolloff=5

" Do incremental searching when it's possible to timeout.
if has('reltime')
  set incsearch
endif

" Do not recognize octal numbers for Ctrl-A and Ctrl-X, most users find it
" confusing.
set nrformats-=octal

" For Win32 GUI: remove 't' flag from 'guioptions': no tearoff menu entries.
if has('win32')
  set guioptions-=t
endif

" Don't use Ex mode, use Q for formatting.
" Revert with ":unmap Q".
map Q gq

" CTRL-U in insert mode deletes a lot.  Use CTRL-G u to first break undo,
" so that you can undo CTRL-U after inserting a line break.
" Revert with ":iunmap <C-U>".
inoremap <C-U> <C-G>u<C-U>

" In many terminal emulators the mouse works just fine.  By enabling it you
" can position the cursor, Visually select and scroll with the mouse.
if has('mouse')
  set mouse=a
endif

" Switch syntax highlighting on when the terminal has colors or when using the
" GUI (which always has colors).
if &t_Co > 2 || has("gui_running")
  " Revert with ":syntax off".
  syntax on

  " I like highlighting strings inside C comments.
  " Revert with ":unlet c_comment_strings".
  let c_comment_strings=1
endif

" Only do this part when Vim was compiled with the +eval feature.
if 1

  " Enable file type detection.
  " Use the default filetype settings, so that mail gets 'tw' set to 72,
  " 'cindent' is on in C files, etc.
  " Also load indent files, to automatically do language-dependent indenting.
  " Revert with ":filetype off".
  filetype plugin indent on

  " Put these in an autocmd group, so that you can revert them with:
  " ":augroup vimStartup | au! | augroup END"
  augroup vimStartup
    au!

    " When editing a file, always jump to the last known cursor position.
    " Don't do it when the position is invalid, when inside an event handler
    " (happens when dropping a file on gvim) and for a commit message (it's
    " likely a different one than last time).
    autocmd BufReadPost *
      \ if line("'\"") >= 1 && line("'\"") <= line("$") && &ft !~# 'commit'
      \ |   exe "normal! g`\""
      \ | endif

  augroup END

endif

" Convenient command to see the difference between the current buffer and the
" file it was loaded from, thus the changes you made.
" Only define it when not defined already.
" Revert with: ":delcommand DiffOrig".
if !exists(":DiffOrig")
  command DiffOrig vert new | set bt=nofile | r ++edit # | 0d_ | diffthis
		  \ | wincmd p | diffthis
endif

if has('langmap') && exists('+langremap')
  " Prevent that the langmap option applies to characters that result from a
  " mapping.  If set (default), this may break plugins (but it's backward
  " compatible).
  set nolangremap
endif

"~ by Ali Aref
imap jj <Esc>

set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
" Add plugins here
Plugin 'preservim/nerdtree'
Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'
Plugin 'valloric/youcompleteme'
" Plugin 'kien/ctrlp.vim'
Plugin 'nvim-lua/plenary.nvim' " telescope dependency
Plugin 'nvim-telescope/telescope.nvim'
Plugin 'w0rp/ale'
" Plugin 'neoclide/coc.nvim'
Plugin 'tpope/vim-fugitive'
Plugin 'airblade/vim-gitgutter'
Plugin 'mg979/vim-visual-multi' " multi-cursor
Plugin 'mattn/emmet-vim'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'ryanoasis/vim-devicons' " vim icons
Plugin 'raimondi/delimitmate' " autoclose quotes, parenthesis, brackets, etc..
Plugin 'vimwiki/vimwiki'
" Plugin 'thaerkh/vim-workspace'
" Plugin 'vim-syntastic/syntastic'
Plugin 'sheerun/vim-polyglot' " advance syntax highlight

" colorschemes plugins
" Plugin 'flazz/vim-colorschemes'
Plugin 'ayu-theme/ayu-vim'
Plugin 'ayu-theme/ayu-vim-airline'
Plugin 'morhetz/gruvbox'
Plugin 'embark-theme/vim', { 'as': 'embark' }
Plugin 'ghifarit53/tokyonight-vim'

call vundle#end()
filetype plugin indent on

set number
set relativenumber
nnoremap <SPACE> <Nop>
let mapleader="\<Space>" " mapping leader key'\' to 'space'
set encoding=UTF-8
set updatetime=100 " setting gitgutter markers delay
set clipboard=unnamedplus
let g:user_emmet_leader_key='<leader>e'

" airline configurations
function! AirlineInit()
    call airline#parts#define_raw('linenr', '%l')
    call airline#parts#define_accent('linenr', 'bold')
    let g:airline_section_z = airline#section#create(['%3p%%', g:airline_symbols.linenr, 'linenr', 'maxlinenr', g:airline_symbols.colnr, '%c'])
endfunction
autocmd VimEnter * call AirlineInit()
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1 " enables the airline smart tabbar
let g:airline#extensions#tabline#formatter = 'default'
" let g:airline_theme='molokai'
let g:airline_theme = "tokyonight"
let g:lightline = {'colorscheme' : 'tokyonight'}


" setting the indentation on different files
autocmd Filetype html setlocal ts=2 sw=2 expandtab
autocmd Filetype htmldjango setlocal ts=2 sw=2 expandtab
let g:airline#extensions#whitespace#enabled = 0 " disableing trailing error from statusbar


" vim polyglot settings (advance highlight) 
" let g:polyglot_disabled = ['autoindent']


" NERDTree Custom Configurations
nnoremap <leader>t :NERDTreeToggle<CR>
" nnoremap <leader>tt :NERDTreeFocus<CR>
" Start NERDTree and put the cursor on it.
" let NERDTreeShowHidden=1
" autocmd VimEnter * NERDTree | wincmd p
" Open the existing NERDTree on each new tab
" autocmd BufWinEnter * if getcmdwintype() == '' | silent NERDTreeMirror | endif 
" Mirror the NERDTree before showing it. This makes it the same on all tabs.
nnoremap <C-n> :NERDTreeMirror<CR>:NERDTreeFocus<CR>
" Close the tab if NERDTree is the only window remaining in it.
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
" If another buffer tries to replace NERDTree, put it in the other window, and bring back NERDTree.
autocmd BufEnter * if bufname('#') =~ 'NERD_tree_\d\+' && bufname('%') !~ 'NERD_tree_\d\+' && winnr('$') > 1 |
    \ let buf=bufnr() | buffer# | execute "normal! \<C-W>w" | execute 'buffer'.buf | endif
" Nerdtree syntax highlight
let g:WebDevIconsDisableDefaultFolderSymbolColorFromNERDTreeDir = 1
let g:WebDevIconsDisableDefaultFileSymbolColorFromNERDTreeFile = 1
let g:NERDTreeLimitedSyntax = 1 " limit syntax highlighting to comman files, avoiding lag issues

" YCM you complete me
let g:ycm_autoclose_preview_window_after_insertion = 0

" Run Python File
" nmap <F10> <Esc>:w<CR>:!clear; python3 %<CR>
nmap <F10> <Esc>:w<CR>:! python3 %<CR>

" Switch to last tab t<Tab>
if !exists('g:lasttab')
  let g:lasttab = 1
endif
nmap t<Tab> :exe "tabn ".g:lasttab<CR>
au TabLeave * let g:lasttab = tabpagenr()

" Syntastic (Python highlight and Syntax Checking)
" set statusline+=%#warningmsg#
" set statusline+=%{SyntasticStatuslineFlag()}
" set statusline+=%*
" let g:syntastic_always_populate_loc_list = 1
" let g:syntastic_auto_loc_list = 1
" let g:syntastic_check_on_open = 1
" let g:syntastic_check_on_wq = 0

" Ale Configuration
"""" Better formatting fo worp/ale
let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%] [%...code...%]'
"""" Enable completion where available.
let g:ale_completion_enabled = 1
""" ale_fixers
let g:ale_fixers = {
    \    '*': ['remove_trailing_lines', 'trim_whitespace'],
    \    'html': ['tidy'],
    \    'htmldjango': ['tidy'],
    \    'javascript': ['tidy'],
    \    'python': ['black']
    \}
" Set this variable to 1 to fix files when you save them.
" let g:ale_fix_on_save = 1
""" Customize linters that are turned on
let g:ale_python_flake8_options = '--max-line-length=120'
let g:ale_linters = {
\   'python': ['flake8'],
\}
let g:ale_set_highlights = 0
let g:ale_sign_error = '>>' " >>'
let g:ale_sign_warning = '--' " '--'
nmap <F3> :ALEFix <CR>


" CtrlP configurations
let g:ctrlp_map = '<leader>p'

" Telescope configurations
" Find files using Telescope command-line sugar.
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>


" Color Schemes
" Ayu
" set termguicolors     " enable true colors support
" let ayucolor="light"  " for light version of theme
" let ayucolor="mirage" " for mirage version of theme
" let ayucolor="dark"   " for dark version of theme
" colorscheme ayu

" tokyo nights colorscheme
set termguicolors
let g:tokyonight_style = 'night' " available: night, storm
let g:tokyonight_enable_italic = 0
colorscheme tokyonight
