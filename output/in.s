.data
printf_text_2525674406192:
	.asciiz "a is 0\n"
printf_text_2525674406960:
	.asciiz "yes\n"
printf_text_2525674407792:
	.asciiz "no\n"
printf_text_2525674408176:
	.asciiz "hello"

.text
main:
	addiu $sp, $sp, -20
	sw $ra, 16($sp)
	sw $fp, 12($sp)
	move $fp, $sp
	li $t0, 0
	sw $t0, 0($fp)
	li $t0, 1
	beq $t0, $zero, endif_344df3a8aafd4ef0b29fc6eb0c087c4a
	nop
if_2a83c7e9651c4c0cb67175d64805626a:
	jal printf_2525674392144
	nop
	li $t1, 1
	beq $t1, $zero, else_774d7c08c7104469bf85dd8b34bf199e
	nop
if_d14f120483fc4a46bbfb14edccc142da:
	jal printf_2525674395280
	nop
	j endif_1c70a7867b744a34a30ac48f035963ee
	nop
else_774d7c08c7104469bf85dd8b34bf199e:
	jal printf_2525674395728
	nop
	j endif_1c70a7867b744a34a30ac48f035963ee
	nop
endif_1c70a7867b744a34a30ac48f035963ee:
	j endif_344df3a8aafd4ef0b29fc6eb0c087c4a
	nop
endif_344df3a8aafd4ef0b29fc6eb0c087c4a:
	jal printf_2525674395984
	nop
	li $t2, 0
	move $v0, $t2
	move $sp, $fp
	lw $fp, 12($sp)
	lw $ra, 16($sp)
	addiu $sp, $sp, 20
	li $v0, 10
	syscall
printf_2525674392144:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_2525674406192
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_2525674395280:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_2525674406960
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_2525674395728:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_2525674407792
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_2525674395984:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_2525674408176
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop