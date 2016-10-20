function! s:require()
  if (exists('g:acid_auto_require') && expand('%') !~ 'test/.*_test.clj')
    AcidRequire
  endif
endfunction
augroup acid
  au!
  au FileType clojure
      \ nmap <buffer> <C-F> :AcidGoToDefinition<CR>
  au BufEnter,BufWritePost *.clj call s:require()
augroup END
