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

### .bfa0
#### Comment Regex
All patterns matching `(\/\*([^*]|(\*+[^*\/]))*\*+\/)|(\/\/.*)` are removed
#### `HELLO WORLD`
```
seventy_two {+} 72
{ - H + } seventy_two // using a cell reference (acts as while loop,
// better to make memory safe loops explicit then need to look through
// each loop to check for non-memory safe behavior) instead of an integer
// literal
/*
 { - B + } A
 compiles into tokens similar to
  [
    bf   : [
    goto : A
    bf   : -
    goto : B
    bf   : +
    bf   : ]
  ]
 which compiles into raw bf as
 [->+<]
 */
{ E + } 69
{ L + } 76
{ O + } 79
{ W + } 87
{ R + } 82
{ D + } 68
{ SPACE + } 32

/*
 * multi-line comment
 */

/* also works like this */

/*
and this
*/

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
