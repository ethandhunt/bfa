segment .text
global _start
_start:
	push rbp
	mov rbp, rsp
	sub rsp, 32768
	mov r11, 0
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- READ STDIN --
	mov rax, 0
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- LOOP START --
.loop_start_3:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_3
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP START --
.loop_start_5:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_5
;	-- INC POINTER --
	add r11, 2
;	-- ADD --
	add BYTE [rbp-32768+r11], 4
;	-- LOOP START --
.loop_start_12:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_12
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 8
;	-- DEC POINTER --
	sub r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_12
.loop_end_12:
;	-- DEC POINTER --
	sub r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- DEC POINTER --
	sub r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP START --
.loop_start_29:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_29
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP START --
.loop_start_36:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_36
;	-- INC POINTER --
	add r11, 3
;	-- LOOP END --
	jmp .loop_start_36
.loop_end_36:
;	-- DEC POINTER --
	sub r11, 1
;	-- LOOP START --
.loop_start_42:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_42
;	-- LOOP START --
.loop_start_43:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_43
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- DEC POINTER --
	sub r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_43
.loop_end_43:
;	-- INC POINTER --
	add r11, 2
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 1
;	-- LOOP END --
	jmp .loop_start_42
.loop_end_42:
;	-- DEC POINTER --
	sub r11, 5
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_29
.loop_end_29:
;	-- LOOP END --
	jmp .loop_start_5
.loop_end_5:
;	-- INC POINTER --
	add r11, 3
;	-- LOOP START --
.loop_start_65:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_65
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_65
.loop_end_65:
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 2
;	-- LOOP START --
.loop_start_72:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_72
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP START --
.loop_start_74:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_74
;	-- DEC POINTER --
	sub r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 3
;	-- LOOP START --
.loop_start_81:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_81
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_81
.loop_end_81:
;	-- LOOP END --
	jmp .loop_start_74
.loop_end_74:
;	-- LOOP END --
	jmp .loop_start_72
.loop_end_72:
;	-- DEC POINTER --
	sub r11, 1
;	-- LOOP START --
.loop_start_87:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_87
;	-- ADD --
	add BYTE [rbp-32768+r11], 12
;	-- DEC POINTER --
	sub r11, 1
;	-- LOOP START --
.loop_start_101:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_101
;	-- INC POINTER --
	add r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP START --
.loop_start_104:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_104
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 2
;	-- LOOP END --
	jmp .loop_start_104
.loop_end_104:
;	-- INC POINTER --
	add r11, 1
;	-- LOOP START --
.loop_start_111:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_111
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- LOOP START --
.loop_start_113:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_113
;	-- DEC POINTER --
	sub r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_113
.loop_end_113:
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 2
;	-- LOOP END --
	jmp .loop_start_111
.loop_end_111:
;	-- DEC POINTER --
	sub r11, 5
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_101
.loop_end_101:
;	-- INC POINTER --
	add r11, 2
;	-- LOOP START --
.loop_start_133:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_133
;	-- DEC POINTER --
	sub r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_133
.loop_end_133:
;	-- INC POINTER --
	add r11, 1
;	-- LOOP START --
.loop_start_140:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_140
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP START --
.loop_start_142:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_142
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- DEC POINTER --
	sub r11, 2
;	-- LOOP START --
.loop_start_146:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_146
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_146
.loop_end_146:
;	-- INC POINTER --
	add r11, 2
;	-- LOOP END --
	jmp .loop_start_142
.loop_end_142:
;	-- DEC POINTER --
	sub r11, 2
;	-- LOOP START --
.loop_start_154:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_154
;	-- DEC POINTER --
	sub r11, 2
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 2
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_154
.loop_end_154:
;	-- INC POINTER --
	add r11, 2
;	-- LOOP END --
	jmp .loop_start_140
.loop_end_140:
;	-- DEC POINTER --
	sub r11, 2
;	-- LOOP START --
.loop_start_167:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_167
;	-- DEC POINTER --
	sub r11, 2
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 2
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_167
.loop_end_167:
;	-- LOOP END --
	jmp .loop_start_87
.loop_end_87:
;	-- DEC POINTER --
	sub r11, 1
;	-- LOOP START --
.loop_start_177:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_177
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_177
.loop_end_177:
;	-- DEC POINTER --
	sub r11, 1
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- LOOP START --
.loop_start_182:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_182
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_182
.loop_end_182:
;	-- DEC POINTER --
	sub r11, 1
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- READ STDIN --
	mov rax, 0
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- ADD --
	add BYTE [rbp-32768+r11], 1
;	-- LOOP END --
	jmp .loop_start_3
.loop_end_3:
;	-- EXIT --
	mov rax, 60
	mov rdi, 0
	syscall
