" Vim syntax file
" Language: bfa0 (Brainfuck bfa iteration 0)
" Maintainer: Ethan Hunt - ethandhunt@gmail.com - github.com/ethandhunt
" Last Change: 2022-03-17
"              yyyy-mm-dd
"
" Run by typing ':so {rel_path}/bfa0_syntax.vim' while in a .bfa0 file buffer.

if exists("b:current_syntax") " if syntax already loaded don't load
    echo "Syntax already loaded"
    finish
endif

syn match Bfa0While '{\|}'
syn match Bfa0CellRef '[^\<\>\+\-\[\]\,\.\{\}\!x 1234567890][^\<\>\+\-\[\]\,\.\{\}\!x ]*'
syn match Bfa0Num '\(}\)\@!\_s*\d'
syn region Bfa0Comment start='//' end='$'
syn region Bfa0Comment start='/\*' end='\*/'
syn match Bfa0CellOp '+\|-'
syn match Bfa0LoopOp '\[\|\]'
syn match Bfa0PtrOp '<\|>'
syn match Bfa0IoOp '\.\|,'
syn match Bfa0Extended 'x\|\!'

hi def link Bfa0Comment Comment
hi def link Bfa0CellOp Constant
hi def link Bfa0Num Number
hi def link Bfa0LoopOp Statement
hi def link Bfa0PtrOp Type
hi def link Bfa0Extended Function
hi def link Bfa0CellRef Type
hi def link Bfa0While Conditional
hi def link Bfa0IoOp PreProc

echo 'Done'
