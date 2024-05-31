.data
array_5365acb1468942f59eda65e46a31e18a:
	.word 1, 2, 3
printf_text_86f4410230f249f19c828d4b7e210aa8:
	.asciiz "\n"
printf_text_d299faac971444b18405b10b525cc74f:
	.asciiz "\n"
printf_text_0b74ce3cd7164a208f251dd73f706079:
	.asciiz "\n"
printf_text_b051456970c0415e9ec52a3bea794cfd:
	.asciiz "\n"
printf_text_38b47cf3df854e3c8512f759cc06a3d1:
	.asciiz "\n"
printf_text_cfaee77a3c394450b292d1ef943f38cf:
	.asciiz "\n"

.text
.globl main
main:
	addiu $sp, $sp, -28
	sw $ra, 24($sp)
	sw $fp, 20($sp)
	move $fp, $sp
	# {1, 2, 3}
	la $t0, array_5365acb1468942f59eda65e46a31e18a
	sw $t0, 0($fp)
	# printf("%d\n", arr[0])
	# None
	# None
	lw $t0, 0($fp)
	la $t1, 0($fp)
	# None
	li $t2, 0
	add $t3, $t1, $t2
	lw $t4, ($t3)
	jal printf_5eead35ee83a41ec9864d962fc0c3590
	nop
	# printf("%d\n", arr[1])
	# None
	# None
	lw $t4, 0($fp)
	la $t1, 0($fp)
	# None
	li $t0, 1
	add $t2, $t1, $t0
	lw $t5, ($t2)
	jal printf_802e13eb281f4475b599456e01104e51
	nop
	# printf("%d\n", arr[2])
	# None
	# None
	lw $t5, 0($fp)
	la $t1, 0($fp)
	# None
	li $t4, 2
	add $t0, $t1, $t4
	lw $t6, ($t0)
	jal printf_42da94d3ff644d10b9901074aabe2de5
	nop
	# arr[0]
	# None
	lw $t6, 0($fp)
	la $t1, 0($fp)
	# None
	li $t5, 0
	add $t4, $t1, $t5
	lw $t7, ($t4)
	# 4
	li $t1, 4
	sw $t1, ($t4)
	# arr[1]
	# None
	lw $t4, 0($fp)
	la $t7, 0($fp)
	# None
	li $t1, 1
	add $t6, $t7, $t1
	lw $t5, ($t6)
	# 5
	li $t7, 5
	sw $t7, ($t6)
	# arr[2]
	# None
	lw $t6, 0($fp)
	la $t5, 0($fp)
	# None
	li $t7, 2
	add $t4, $t5, $t7
	lw $t1, ($t4)
	# 6
	li $t5, 6
	sw $t5, ($t4)
	# printf("%d\n", arr[0])
	# None
	# None
	lw $t4, 0($fp)
	la $t1, 0($fp)
	# None
	li $t5, 0
	add $t6, $t1, $t5
	lw $t7, ($t6)
	jal printf_9de0325917444b97b87503f2adc55998
	nop
	# printf("%d\n", arr[1])
	# None
	# None
	lw $t7, 0($fp)
	la $t1, 0($fp)
	# None
	li $t4, 1
	add $t5, $t1, $t4
	lw $t8, ($t5)
	jal printf_7c35e82516bf4ef3ac182e1039deb1bf
	nop
	# printf("%d\n", arr[2])
	# None
	# None
	lw $t8, 0($fp)
	la $t1, 0($fp)
	# None
	li $t7, 2
	add $t4, $t1, $t7
	lw $t9, ($t4)
	jal printf_3ffac3520cbf422cb8baba7a634bd4a6
	nop
	# 0
	li $t9, 0
	move $v0, $t9
	move $sp, $fp
	lw $fp, 20($sp)
	lw $ra, 24($sp)
	addiu $sp, $sp, 28
	li $v0, 10
	syscall
printf_5eead35ee83a41ec9864d962fc0c3590:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	move $a0, $t4
	li $v0, 1
	syscall
	la $a0, printf_text_86f4410230f249f19c828d4b7e210aa8
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_802e13eb281f4475b599456e01104e51:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	move $a0, $t5
	li $v0, 1
	syscall
	la $a0, printf_text_d299faac971444b18405b10b525cc74f
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_42da94d3ff644d10b9901074aabe2de5:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	move $a0, $t6
	li $v0, 1
	syscall
	la $a0, printf_text_0b74ce3cd7164a208f251dd73f706079
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_9de0325917444b97b87503f2adc55998:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	move $a0, $t7
	li $v0, 1
	syscall
	la $a0, printf_text_b051456970c0415e9ec52a3bea794cfd
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_7c35e82516bf4ef3ac182e1039deb1bf:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	move $a0, $t8
	li $v0, 1
	syscall
	la $a0, printf_text_38b47cf3df854e3c8512f759cc06a3d1
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_3ffac3520cbf422cb8baba7a634bd4a6:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	move $a0, $t9
	li $v0, 1
	syscall
	la $a0, printf_text_cfaee77a3c394450b292d1ef943f38cf
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop