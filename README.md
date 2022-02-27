# bfa
low level language that compiles to brainfuck, also compiles that brainfuck into assembly

### Progress
- [x] Compile raw bf to nasm elf64 assembly
- [ ] Compile assembly into elf64 executables natively (within main.py)
- [ ] Get .bf extension working
- [ ] Get .bf files self hosted

### .bf Extension
- `!` open new file descriptor, file path in `[pointer+1:NULL]`, `int fd` returned in `[pointer]`, mode in `[pointer]`
- `x` execute another file, same as above

### .bfa0 Syntax Planning 

Examples
```
H+72
E+69
L+76
O+79
W+87
R+82
D+68
SPACE+32

H.
E.
L.
L.
O.
SPACE.
W.
O.
R.
L.
D.
```
