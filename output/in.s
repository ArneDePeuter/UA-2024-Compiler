.data
printf_text_3bc26e1ff24946ed9899e4b4e74a2f78:
	.asciiz "Hello, World!\n"
printf_text_a003687fcdf24bcbbc9376b532cc8a94:
	.asciiz "WE ARE THE BEST\n"
printf_text_bf588240f6794ddfb30b8d44fbf74615:
	.asciiz "WELCOME TO OUR COMPILER\n"

.text
.globl main
main:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	# printf("Hello, World!\n")
	jal printf_89d5b3f4314e4366a7c348f4da555018
	nop
	# printf("WE ARE THE BEST\n")
	jal printf_ab4b9cdc6564425bb9b886df655ec719
	nop
	# printf("WELCOME TO OUR COMPILER\n")
	jal printf_54cba40f5a784162b1147b41d6fd74fa
	nop
	# 0
	li $t0, 0
	move $v0, $t0
	j main_exit
	nop
main_exit:
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	li $v0, 10
	syscall
printf_89d5b3f4314e4366a7c348f4da555018:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_3bc26e1ff24946ed9899e4b4e74a2f78
	li $v0, 4
	syscall
printf_89d5b3f4314e4366a7c348f4da555018_exit:
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_ab4b9cdc6564425bb9b886df655ec719:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_a003687fcdf24bcbbc9376b532cc8a94
	li $v0, 4
	syscall
printf_ab4b9cdc6564425bb9b886df655ec719_exit:
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_54cba40f5a784162b1147b41d6fd74fa:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_bf588240f6794ddfb30b8d44fbf74615
	li $v0, 4
	syscall
printf_54cba40f5a784162b1147b41d6fd74fa_exit:
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop