function! myspacevim#before() abort
    let g:neomake_c_enabled_makers = ['clang']
    " you can defined mappings in bootstrap function
    " for example, use jj to exit insert mode.
    inoremap jj <Esc>
    " share clipboard
    set clipboard=unnamedplus
    " settings black for formatting python files (yapf)
    let g:neoformat_python_black = {
    \ 'exe': 'black',
    \ 'stdin': 1,
    \ 'args': ['-q', '-', '-l 80'],
    \ }
    let g:neoformat_enabled_python = ['black', ]
    " github layer configs
    let g:github_dashboard = { 'username': 'ali-aref', 'password': "ala-4e2g:Dhh-arsalis" }
    let g:gista#client#default_username = 'monkeyxite'
endfunction

function! myspacevim#after() abort
    " you can remove key binding in bootstrap_after function
    " iunmap kj
endfunction

