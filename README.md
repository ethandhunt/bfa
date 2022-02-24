# bfa
low level language that compiles to brainfuck, also compiles that brainfuck into assembly

### Progress
- [x] Compile raw bf to nasm elf64 assembly
- [ ] Compile assembly into elf64 executables natively (within main.py)

### .bfa0 Syntax Planning 
Similar to a state machine

Examples
```
LAYOUT
a char
b array char 3
c short

%INCLUDE a_file

DECLARETEMP 4 // the size of temp

EXTEND.CONST char max
VALUE 255

EXTEND.MACRO short add @ $
PARAMS self value
TEMPALLOC 1
// Affects cmp result
TEMPCOMPARE 0 self[0] char.max


STATE 1
```
incomplete
