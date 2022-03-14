#!/bin/python3.10
import sys
import subprocess
import re
import string

class ansi:
    black = '\033[30m'
    class dark:
        red = '\033[31m'
        green = '\033[32m'
        yellow = '\033[33m'
        blue = '\033[34m'
        magenta = '\033[35m'
        cyan = '\033[36m'

    grey = '\033[90m'

    class bright:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        blue = '\033[94m'
        magenta = '\033[95m'
        cyan = '\033[96m'

    bold = '\033[1m'
    reset = '\033[0m'


def compileBf(inFP, outFP, extend=False):
    '''
    tape is allocated 32768 (2**15) bytes

    assembly memory layout:
    pointer: r11

    '''
    if extend:
        start = (
                'segment .text\n'
                'global _start\n'
                '_start:\n'
                '\tpush rbp\n'
                '\tmov rbp, rsp\n'
                '\tsub rsp, 32768\n'
                '\tmov r11, 0\n'
        )

        end = (
                ';\t-- EXIT --\n'
                '\tmov rax, 60\n'
                '\tmov rdi, 0\n'
                '\tsyscall\n'
        )

        readFD = (
                ';\t-- READ FD --\n'
                '\tmov rax, 0\n'
                '\tpush r11\n' # ???
                '\tmovzx rdi, BYTE [rbp-32768+r11]\n'
                '\tpop r11\n' # ???
                '\tpush r11\n' # ???
                '\tlea rsi, [rbp-32768+r11+1]\n'
                '\tmov rdx, 1\n'
                '\tsyscall\n'
                '\tpop r11\n' # ???
        )

        # TODO: not done writeFD
        writeFD = (
                ';\t-- WRITE FD --\n'
                '\tmov rax, 1\n'
                '\tmov rdi, 0\n'
                '\tpush r11\n' # ???
                '\tlea rsi, [rbp-32768+r11]\n'
                '\tmov rdx, 1\n'
                '\tsyscall\n'
                '\tpop r11\n' # ???
        )


    else:
        start = (
                'segment .text\n'
                'global _start\n'
                '_start:\n'
                '\tpush rbp\n'
                '\tmov rbp, rsp\n'
                '\tsub rsp, 32768\n'
                '\tmov r11, 0\n'
        )

        end = (
                ';\t-- EXIT --\n'
                '\tmov rax, 60\n'
                '\tmov rdi, 0\n'
                '\tsyscall\n'
        )

        readSTDIN = (
                ';\t-- READ STDIN --\n'
                '\tmov rax, 0\n'
                '\tmov rdi, 0\n'
                '\tpush r11\n' # ???
                '\tlea rsi, [rbp-32768+r11]\n'
                '\tmov rdx, 1\n'
                '\tsyscall\n'
                '\tpop r11\n' # ???
        )

        writeSTDOUT = (
                ';\t-- WRITE STDOUT --\n'
                '\tmov rax, 1\n'
                '\tmov rdi, 0\n'
                '\tpush r11\n' # ???
                '\tlea rsi, [rbp-32768+r11]\n'
                '\tmov rdx, 1\n'
                '\tsyscall\n'
                '\tpop r11\n' # ???
        )

        with open(inFP, 'r') as f:
            code = f.read()
        code = ''.join([x for x in code if x in '<>,.+-[]']) # remove non bf chars
        compiled = start
        print(code)
        if code.count('[') != code.count(']'):
            print(f'{ansi.dark.red}[ERROR]{ansi.reset} Number of opening brackets ({code.count("[")}) does not match number of closing brackets ({code.count("]")})')
            exit(1)
        heapable = '+-<>'
        processed = []
        last = ''
        for char in code:
            if char in heapable:
                if last == char:
                    processed[-1] += char
                else:
                    processed.append(char)
            else:
                processed.append(char)
            last = char

        read = ''
        i = 0
        for c in processed:
            if c[0] == '>':
                compiled += (
                        ';\t-- INC POINTER --\n'
                       f'\tadd r11, {len(c)}\n'
                )

            elif c[0] == '<':
                compiled += (
                        ';\t-- DEC POINTER --\n'
                       f'\tsub r11, {len(c)}\n'
                )

            elif c[0] == '+':
                compiled += (
                        ';\t-- ADD --\n'
                       f'\tadd BYTE [rbp-32768+r11], {len(c)}\n'
                )

            elif c[0] == '-':
                compiled += (
                        ';\t-- SUB --\n'
                       f'\tsub BYTE [rbp-32768+r11], {len(c)}\n'
                )

            elif c == '.':
                compiled += writeSTDOUT

            elif c == ',':
                compiled += readSTDIN

            elif c == ']':
                depth = 0
                addr = len(read)
                for x in read[::-1]:
                    if x == '[':
                        if depth == 0:
                            addr -= 1
                            break
                        else:
                            depth -= 1
                    elif x == ']':
                        depth += 1
                    addr -= 1

                if 'verbose' in flags:
                    print(f'ret_to {addr}')
                compiled += (
                        ';\t-- LOOP END --\n'
                       f'\tjmp .loop_start_{addr}\n'
                       f'.loop_end_{addr}:\n'
                )

            elif c == '[':
                addr = len(read)
                if 'verbose' in flags:
                    print(f'.loop_start_{addr}')
                compiled += (
                        ';\t-- LOOP START --\n'
                       f'.loop_start_{addr}:\n'
                        '\tmovzx rax, BYTE [rbp-32768+r11]\n'
                        '\tcmp rax, 0\n'
                       f'\tjz .loop_end_{addr}\n'
                )


            read += c
            i += 1
            if 'verbose' in flags:
                print(f'{ansi.bright.red}{len(read)}{ansi.bright.yellow}:{ansi.bright.red}{i}\t{ansi.bright.magenta}{len(c)}\t{ansi.bold+ansi.bright.cyan}{c[0]}{ansi.reset} -> {ansi.bright.green}{len(compiled)} B{ansi.reset}')

        compiled += end
        print(f'{ansi.bright.green}Program compiled successfully{ansi.reset}')

        with open(outFP, 'w') as f:
            f.write(compiled)

    if 'x' in flags or 'executable' in flags:
        subprocess.run(['mv', outFP, outFP+'.asm'])
        subprocess.run(['nasm', '-f', 'elf64', '-o', outFP+'.o', outFP+'.asm'])
        subprocess.run(['ld', '-o', outFP, outFP+'.o'])
        if 'r' in flags or 'run' in flags:
            print(f'{ansi.bright.green}Executing {outFP}{ansi.reset}')
            subprocess.run(['./'+outFP])
            print(f'{ansi.bright.green}Done{ansi.reset}')


class compileBFA:
    def _0(inFP, outFP):
        '''
        takes a .bfa0 file and compiles (transpiles?) it to a .bf file
        '''

        with open(inFP, 'r') as f:
            code = f.read()

        # remove comments and newlines
        code = re.sub(r'(\/\*([^*]|(\*+[^*\/]))*\*+\/)|(\/\/.*)', '', code, re.MULTILINE).replace('\n', '')
        for char in string.whitespace:
            code = code.replace(char, '')

        bfchar = '+-<>[],.'
        if 'e' in flags or 'extended' in flags:
            bfchar += '!x'

        # Tokenise code
        # syntax:
        #   Comments: '//' ... '\n' || '/*' ... '*/'
        #   Repeats: '{' {bfchar} '}' {{int}* || {CellRef}}
        #   Cell Referencing: {!bfchar && !int}*
        #   BF Instruction: {bfchar}


        # hacky
        def recursiveClean(code):
            print(f'{ansi.bright.yellow}recursiveClean({ansi.bright.green}{repr(code)}{ansi.bright.yellow}){ansi.reset}')
            if code.count('{') != code.count('}'):
                print(f'{ansi.dark.red}[ERROR]{ansi.reset} Number of opening brackets ({code.count("{")}) does not match number of closing brackets ({code.count("}")})')
                exit(1)
            tokens = []
            last = ''
            n = 0
            depth = 0
            while n < len(code):
                if code[n] == '{':
                    if depth == 0 and last != '':
                        # TODO: more testing
                        tokens.append( ('goto', last) )
                        last = ''

                    depth += 1

                elif code[n] == '}':
                    depth -= 1
                    if depth == 0:
                        recursiveLast = recursiveClean(last)
                        last = ''
                        n += 1
                        if code[n].isdigit():
                            repeatNum = ''
                            while code[n].isdigit() and n < len(code):
                                repeatNum += code[n]
                                n += 1
                                if n == len(code):
                                    break

                            repeatNum = int(repeatNum)
                            print(f'{ansi.bright.yellow}repeatNum: {ansi.bright.green}{repr(repeatNum)}{ansi.reset}')
                            n -= 1
                            tokens += recursiveLast * repeatNum # += intentionally
                            tokens.append( ('bf', ' ') )

                        elif code[n] not in (bfchar + '{' + '}'):
                            cellRef = ''
                            while code[n] not in (bfchar + '{' + '}'):
                                cellRef += code[n]
                                n += 1
                                if n == len(code):
                                    break
                            n -= 1

                            print(f'{ansi.bright.yellow}cellRef: {ansi.bright.green}{repr(cellRef)}{ansi.reset}')

                            tokens.append( ('goto', cellRef) )
                            tokens.append( ('bf', '[') )
                            tokens += recursiveLast # += intentionally
                            tokens.append( ('goto', cellRef) )
                            tokens.append( ('bf', ']') )
                            tokens.append( ('bf', ' ') )

                elif depth != 0:
                    last += code[n]
                
                elif code[n] not in (bfchar):
                    last += code[n]

                elif code[n] in bfchar:
                    if last != '':
                        # TODO: more testing
                        tokens.append( ('goto', last) ) # might raise problems
                        last = ''

                    tokens.append( ('bf', code[n]) )

                n += 1
                if 'v' in flags or 'verbose' in flags:
                    print(f'{ansi.bright.yellow}last: {ansi.bright.green}{repr(last)}{ansi.reset}')

            return tokens

        tokens = recursiveClean(code)

        # clean tokens
        newTokens = []
        currentGoto = ''
        for token in tokens:
            # remove redundant goto's
            if token[0] == 'goto':
                if currentGoto == token[1]:
                    print(' ', repr(currentGoto), repr(token[1]))
                    continue

                else:
                    print('e', repr(currentGoto), repr(token[1]))
                    currentGoto = token[1]
                    newTokens.append(token)

            elif token[0] == 'bf':
                newTokens.append(token)

            else:
                print(f'{ansi.bright.red}[ERROR]{ansi.reset} Unknown token type: {token[0]}')
                exit(1)

        tokens = newTokens

        if 'v' in flags or 'verbose' in flags:
            print(f'{ansi.bright.yellow}Tokens:{ansi.reset}')
            lastBF = ''
            lastBFIndex = 0
            for i, token in enumerate(tokens):
                if token[0] == 'goto':
                    if lastBF != '':
                        if lastBFIndex != i-1:
                            print(f'{ansi.bright.yellow}<TOKEN [{lastBFIndex:03}:{i-1:03}]\t{ansi.bright.green}(\'bf\', {lastBF})')

                        else:
                            print(f'{ansi.bright.yellow}<TOKEN [{i-1}]\t\t{ansi.bright.green}(\'bf\', {lastBF})')

                        lastBF = ''
                    print(f'{ansi.bright.yellow}<TOKEN [{i}]>\t\t{ansi.bright.green}{repr(token)}{ansi.reset}')

                if token[0] == 'bf':
                    if lastBF == '':
                        lastBFIndex = i

                    lastBF += token[1]

        cellRefs = {} # dict
        cellPtr = 0
        for ins in tokens:
            primary = ins[0]
            arg = ins[1]

            if primary == 'goto' and arg not in cellRefs:
                cellRefs[arg] = cellPtr
                cellPtr += 1

        print(f'{ansi.bright.yellow}cellRefs: {ansi.bright.green}{repr(cellRefs)}{ansi.reset}')

        cellPtr = 0
        compiled = ''
        for ins in tokens:
            primary = ins[0]
            arg = ins[1]

            if primary == 'goto':
                compiled += '<' * -(cellRefs[arg]-cellPtr) + '>' * (cellRefs[arg]-cellPtr)
                cellPtr = cellRefs[arg]

            elif primary == 'bf':
                compiled += arg
        print(f'{ansi.bright.yellow}compiled: {ansi.bright.green}{repr(compiled)}{ansi.reset}')

        with open(outFP, 'w') as f:
            f.write(compiled)


def main():
    def subcommand(name, args=[]):
        result = f'\t\t{ansi.bright.magenta+ansi.bold}{name}{ansi.reset} '
        for arg in args:
            if arg.count('.') == 0:
                result += f'<{ansi.bright.cyan}{arg}{ansi.reset}> '

            else:
                result += f'<{ansi.bright.cyan}{"".join(arg.split(".")[:-1])}{ansi.bright.green}.{arg.split(".")[-1]}{ansi.reset}> '

        return result.replace('?', f'{ansi.bright.magenta}?{ansi.bright.green}')

    def subcommandUsage(name, args=[]):
        f'{ansi.bright.yellow + ansi.bold}Usage{ansi.reset}: python3 main.py {ansi.bright.green}compile{ansi.reset} <{ansi.bright.cyan + ansi.bold}inFP{ansi.bright.green}.bf{ansi.reset}> <{ansi.bright.cyan + ansi.bold}outFP{ansi.bright.green}.asm{ansi.reset}>'
        result = f'{ansi.bright.yellow + ansi.bold}Usage{ansi.reset}:\n\tpython3 main.py {ansi.bright.green}{name}{ansi.reset} '
        for arg in args:
            if arg.count('.') == 0:
                result += f'<{ansi.bright.cyan + ansi.bold}{arg}{ansi.reset}> '

            else:
                result += f'<{ansi.bright.cyan + ansi.bold}{"".join(arg.split(".")[:-1])}{ansi.reset}{ansi.bright.green}.{arg.split(".")[-1]}{ansi.reset}> '

        return result.replace('?', f'{ansi.bright.magenta}?{ansi.bright.green}')

    def flagUsage(name, description):
        return f'\t{ansi.bright.cyan + ansi.bold}{name}{ansi.reset}\t- {ansi.bright.green}{description}{ansi.reset}'


    global flags, argv
    flags = []
    argv = []
    for arg in sys.argv[1:]:
        if arg.startswith('--'):
            flags.append(arg[2:])

        elif arg.startswith('-'):
            flags += arg[1:] # add all flags (supposed to be +=)

        else:
            argv.append(arg)

    if 'debug' in flags:
        print(f'flags: {flags}')
        print(f'argv: {argv}')

    if len(argv) < 1:
        print(
            f'{ansi.bright.yellow + ansi.bold}Usage{ansi.reset}:\tpython3 {ansi.bright.green}main.py{ansi.reset} <{ansi.bright.cyan + ansi.bold}subcommand{ansi.reset}> <{ansi.bright.cyan + ansi.bold}args{ansi.reset}>\n'
            f'\t{ansi.bright.cyan}subcommands{ansi.reset}:')
        print(subcommand('compile', ['inFile.bf', 'outFile.asm?x']))
        print(subcommand('assemble', ['bfa Version', 'inFile.bfa?', 'outFile.bf']))
        print(subcommand('flags', []))
        exit(1)

    subcommand = argv[0]
    args = argv[1:]
    match subcommand:
        case 'compile':
            if len(args) != 2:
                print(subcommandUsage('compile', ['inFile.bf', 'outFile.asm?x']))
                exit(1)
            compileBf(args[0], args[1], True if 'e' in flags or 'extended' in flags else False)

        case 'assemble':
            if len(args) != 3:
                print(subcommandUsage('assemble', ['bfa Version (\'.\' for file autodetect)', 'inFile.bfa?', 'outFile.bf']))
                exit(1)

            bfaVersion = args[0]

            if args[0] == '.':
                bfaVersion = args[1].split('.')[-1]

            if bfaVersion == 'bfa0':
                f = compileBFA._0

            else:
                print(f'{ansi.bright.yellow + ansi.bold}Error{ansi.reset}: Unknown bfa version {ansi.bright.cyan + ansi.bold}{args[0]}{ansi.reset}')
                exit(1)

            f(*args[1:])


        case 'flags':
            print(f'{ansi.bright.yellow + ansi.bold}Flags{ansi.reset}:')
            print(flagUsage('--verbose', 'print verbose info'))
            print(flagUsage('-x --executable', 'generate executable instead of assembly file with the compile subcommand'))
            print(flagUsage('-r --run', 'run the executable after compilation'))
            print(flagUsage('-e --extended', 'use extended brainfuck'))
            exit(1)

if __name__ == "__main__":
    main()
