#!/bin/python3.10
import sys
import subprocess

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


def compileBf(inFP, outFP, mode='classic'):
    '''
    tape should be fine up to 1024 cells

    assembly memory layout:
    pointer: DWORD [rbp - 4]

    '''
    if mode == 'classic':
        # classic brainfuck
        start = (
                'segment .text\n'
                'global _start\n'
                '_start:\n'
                '\tpush rbp\n'
                '\tmov rbp, rsp\n'
                '\tsub rsp, 1024\n'
        )

        end = (
                '\tmov rax, 60\n'
                '\tmov rdi, 0\n'
                '\tsyscall\n'
        )

        readSTDIN = (
                ';\t-- READ STDIN --\n'
                'mov eax, DWORD [rbp-4]\n'
                '\tlea rsi, [rbp-1024+rax]\n'
                '\tmov rax, 0\n'
                '\tmov rdi, 0\n'
                '\tmov rdx, 1\n'
                '\tsyscall\n'
        )

        writeSTDOUT = (
                ';\t-- WRITE STDOUT --\n'
                '\tmov edx, DWORD [rbp-4]\n' # get pointer
                '\tmov rax, 1\n'
                '\tmov rdi, 0\n'
                '\tmov rsi, rbp\n'
                '\tsub rsi, 1024\n'
                '\tadd rsi, rdx\n'
                '\tmov rdx, 1\n'
                '\tsyscall\n'
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
                        ';\t -- INC POINTER --\n'
                       f'\tadd DWORD [rbp-4], {len(c)}\n'
                )

            elif c[0] == '<':
                compiled += (
                        ';\t -- DEC POINTER --\n'
                       f'\tsub DWORD [rbp-4], {len(c)}\n'
                )

            elif c[0] == '+':
                compiled += (
                        ';\t-- ADD --\n'
                        '\tmov edx, DWORD [rbp-4]\n' # get pointer
                        '\tmovzx eax, BYTE [rbp-1024+rdx]\n'
                       f'\tadd eax, {len(c)}\n'
                        '\tmov BYTE [rbp-1024+rdx], al\n'
                )

            elif c[0] == '-':
                compiled += (
                        ';\t-- SUB --\n'
                        '\tmov edx, DWORD [rbp-4]\n' # get pointer
                        '\tmovzx eax, BYTE [rbp-1024+rdx]\n'
                       f'\tsub eax, {len(c)}\n'
                        '\tmov BYTE [rbp-1024+rdx], al\n'
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
                        '\tmov edx, DWORD [rbp-4]\n' # get pointer
                        '\tmovzx eax, BYTE [rbp-1024+rdx]\n'
                        '\tcmp eax, 0\n'
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
        subprocess.run(['nasm', '-f', 'elf64', '-o', outFP+'.o', outFP])
        subprocess.run(['ld', '-o', outFP+'.x', outFP+'.o'])
        if 'r' in flags or 'run' in flags:
            print(f'{ansi.bright.green}Executing {outFP+".x"}{ansi.reset}')
            subprocess.run(['./'+outFP+'.x'])
            print(f'{ansi.bright.green}Done{ansi.reset}')


class compileBFA:
    def _0(inFP, outFP):
        pass


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
        return f'\t{ansi.bright.cyan + ansi.bold}{name}{ansi.reset} - {ansi.bright.green}{description}{ansi.reset}'


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
            f'{ansi.bright.yellow + ansi.bold}Usage{ansi.reset}: python3 {ansi.bright.green}main.py{ansi.reset} <{ansi.bright.cyan + ansi.bold}subcommand{ansi.reset}> <{ansi.bright.cyan + ansi.bold}args{ansi.reset}>\n'
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
            compileBf(args[0], args[1])

        case 'assemble':
            if len(args) != 2:
                print(subcommandUsage('assemble', ['inFile.bfAsm', 'outFile.bf']))
                exit(1)
        
        case 'flags':
            print(f'{ansi.bright.yellow + ansi.bold}Flags{ansi.reset}:')
            print(flagUsage('--verbose', 'print verbose info'))
            print(flagUsage('-x --executable', 'generate executable instead of assemebly file with the compile subcommand'))
            print(flagUsage('-r --run', 'run the executable after compilation'))
            exit(1)

if __name__ == "__main__":
    main()
