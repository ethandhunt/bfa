" Vim syntax file
" Language: Brainfuck
" Maintainer: Ethan Hunt - ethandhunt@gmail.com - github.com/ethandhunt
" Last Change: 2022-03-17
"              yyyy-mm-dd
"
" Run by typing ':so bf_syntax.vim' while in a .bf file buffer.

if exists("b:current_syntax") " if syntax is already loaded don't load
    echo 'Syntax already loaded'
    finish
endif

syn match BrainfuckComment '.'
syn match BrainfuckCellOp '+\|-'
syn match BrainfuckLoopOp '\[\|\]'
syn match BrainfuckPtrOp '<\|>'
syn match BrainfuckIoOp '\.\|,'
syn match BrainfuckExtended 'x\|\!'

hi def link BrainfuckComment Comment
hi def link BrainfuckCellOp Constant
hi def link BrainfuckIoOp PreProc
hi def link BrainfuckLoopOp Statement
hi def link BrainfuckPtrOp Type
hi def link BrainfuckExtended Function

echo 'Done'
