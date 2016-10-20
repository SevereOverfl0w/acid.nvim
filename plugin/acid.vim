if exists('g:acid_init')
  finish
endif

AcidInit

function! s:require()
  if (exists('g:acid_auto_require')
        \ && g:acid_auto_require
        \ && expand('%') !~ 'test/.*_test.clj')
    AcidRequire
  endif
endfunction

function! s:start_repls()
  if (exists('g:acid_auto_start_repl')
        \ && g:acid_auto_start_repl)
    AcidStartRepl
endfunction

augroup acid
  au!
  au FileType clojure
      \ nmap <buffer> <C-F> :AcidGoToDefinition<CR>
  au BufEnter,BufWritePost *.clj call s:require()
  au BufEnter *.clj call s:require()
augroup END

