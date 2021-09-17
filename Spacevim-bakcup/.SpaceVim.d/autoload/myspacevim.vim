function! myspacevim#before() abort
    let g:neomake_c_enabled_makers = ['clang']
    " you can defined mappings in bootstrap function
    " for example, use jj to exit insert mode.
    inoremap jj <Esc>
    " share clipboard
    set clipboard=unnamedplus
    " status line
    let g:lightline = {'colorscheme' : 'tokyonight'}
    let g:airline_theme = "tokyonight"
    " settings black for formatting python fiels (yapf)
    let g:neoformat_python_black = {
    \ 'exe': 'black',
    \ 'stdin': 1,
    \ 'args': ['-q', '-', '-l 110'],
    \ }
    let g:neoformat_enabled_python = ['black', ]
endfunction

function! myspacevim#after() abort
    " you can remove key binding in bootstrap_after function
    " iunmap kj
endfunction

