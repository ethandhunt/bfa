segment .text
global _start
_start:
	push rbp
	mov rbp, rsp
	sub rsp, 32768
	mov r11, 0
;	-- ADD --
	add BYTE [rbp-32768+r11], 7
;	-- LOOP START --
.loop_start_7:
	movzx rax, BYTE [rbp-32768+r11]
	cmp rax, 0
	jz .loop_end_7
;	-- SUB --
	sub BYTE [rbp-32768+r11], 1
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 10
;	-- DEC POINTER --
	sub r11, 1
;	-- LOOP END --
	jmp .loop_start_7
.loop_end_7:
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 2
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 69
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 76
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 79
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 87
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 82
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 68
;	-- INC POINTER --
	add r11, 1
;	-- ADD --
	add BYTE [rbp-32768+r11], 32
;	-- DEC POINTER --
	sub r11, 7
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- INC POINTER --
	add r11, 1
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- INC POINTER --
	add r11, 1
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- INC POINTER --
	add r11, 1
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- INC POINTER --
	add r11, 4
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- DEC POINTER --
	sub r11, 3
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
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
;	-- INC POINTER --
	add r11, 2
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- DEC POINTER --
	sub r11, 3
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- INC POINTER --
	add r11, 4
;	-- WRITE STDOUT --
	mov rax, 1
	mov rdi, 0
	push r11
	lea rsi, [rbp-32768+r11]
	mov rdx, 1
	syscall
	pop r11
;	-- EXIT --
	mov rax, 60
	mov rdi, 0
	syscall
