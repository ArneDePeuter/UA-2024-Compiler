.data
printf_text_2131574845680:
	.asciiz "a is 0\n"
printf_text_2131574846320:
	.asciiz "hey\n"
printf_text_2131574846448:
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
	beq $t0, $zero, endif_07deb27e849343ecbfa16945e524166e
	nop
if_c2c0604e844c41569513888ad2cdb4e2:
	jal printf_2131574833936
	nop
	li $t1, 1
	beq $t1, $zero, endif_b623c037f51c4fc29256ace55425ea81
	nop
if_979047cdf511465aa31286ec11c9a185:
	jal printf_2131574833872
	nop
	j endif_b623c037f51c4fc29256ace55425ea81
	nop
endif_b623c037f51c4fc29256ace55425ea81:
	j endif_07deb27e849343ecbfa16945e524166e
	nop
endif_07deb27e849343ecbfa16945e524166e:
	jal printf_2131574835664
	nop
	li $t2, 0
	move $v0, $t2
	move $sp, $fp
	lw $fp, 12($sp)
	lw $ra, 16($sp)
	addiu $sp, $sp, 20
	li $v0, 10
	syscall
printf_2131574833936:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_2131574845680
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_2131574833872:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_2131574846320
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_2131574835664:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_2131574846448
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop