.data
printf_text_3f47ca4375154856829f71e65cbf6c0c:
	.asciiz "Car1: speed="
printf_text_39dbdff5aa854ec2a90392ea4d0803fc:
	.asciiz ", weight="
printf_text_8e418d48f6244c9b97ba358020168da2:
	.asciiz "\n"
printf_text_bf756d75408a4c19b3ae430802f9da39:
	.asciiz "Car2: speed="
printf_text_7ead48c249b6483fb712168da46ad92c:
	.asciiz ", weight="
printf_text_81382b95636541bc9b6011945c28c2e0:
	.asciiz "\n"

.text
.globl main
main:
	addiu $sp, $sp, -32
	sw $ra, 28($sp)
	sw $fp, 24($sp)
	move $fp, $sp
	lw $t0, 0($fp)
	la $t1, 0($fp)
	lw $t0, 0($t1)
	addi $t2, $t1, 0
	li $t1, 100
	sw $t1, 0($t2)
	lw $t2, 0($fp)
	la $t1, 0($fp)
	lw $t2, 4($t1)
	addi $t0, $t1, 4
	li $t1, 2000
	sw $t1, 0($t0)
	lw $t0, 8($fp)
	la $t1, 8($fp)
	lw $t0, 0($t1)
	addi $t2, $t1, 0
	li $t1, 200
	sw $t1, 0($t2)
	lw $t2, 8($fp)
	la $t1, 8($fp)
	lw $t2, 4($t1)
	addi $t0, $t1, 4
	li $t1, 3000
	sw $t1, 0($t0)
	# printf("Car1: speed=%d, weight=%d\n", car1.speed, car1.weight);
	lw $t0, 0($fp)
	la $t1, 0($fp)
	lw $t0, 0($t1)
	addi $t2, $t1, 0
	lw $t1, 0($fp)
	la $t3, 0($fp)
	lw $t1, 4($t3)
	addi $t4, $t3, 4
	jal printf_65f2493f905c497c8cd98bdd5c798ce0
	nop
	# printf("Car2: speed=%d, weight=%d\n", car2.speed, car2.weight);
	lw $t0, 8($fp)
	la $t1, 8($fp)
	lw $t0, 0($t1)
	addi $t3, $t1, 0
	lw $t1, 8($fp)
	la $t5, 8($fp)
	lw $t1, 4($t5)
	addi $t6, $t5, 4
	jal printf_6bb2bd408d394ea1bda92502aeb9739c
	nop
	li $t0, 0
	move $v0, $t0
	move $sp, $fp
	lw $fp, 24($sp)
	lw $ra, 28($sp)
	addiu $sp, $sp, 32
	li $v0, 10
	syscall
printf_65f2493f905c497c8cd98bdd5c798ce0:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_3f47ca4375154856829f71e65cbf6c0c
	li $v0, 4
	syscall
	move $a0, $t0
	li $v0, 1
	syscall
	la $a0, printf_text_39dbdff5aa854ec2a90392ea4d0803fc
	li $v0, 4
	syscall
	move $a0, $t1
	li $v0, 1
	syscall
	la $a0, printf_text_8e418d48f6244c9b97ba358020168da2
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop
printf_6bb2bd408d394ea1bda92502aeb9739c:
	addiu $sp, $sp, -16
	sw $ra, 12($sp)
	sw $fp, 8($sp)
	move $fp, $sp
	la $a0, printf_text_bf756d75408a4c19b3ae430802f9da39
	li $v0, 4
	syscall
	move $a0, $t0
	li $v0, 1
	syscall
	la $a0, printf_text_7ead48c249b6483fb712168da46ad92c
	li $v0, 4
	syscall
	move $a0, $t1
	li $v0, 1
	syscall
	la $a0, printf_text_81382b95636541bc9b6011945c28c2e0
	li $v0, 4
	syscall
	move $sp, $fp
	lw $fp, 8($sp)
	lw $ra, 12($sp)
	addiu $sp, $sp, 16
	jr $ra
	nop