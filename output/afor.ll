; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int a = 0;
  %"a" = alloca i32
  store i32 0, i32* %"a"
  br label %"w_condition"
w_condition:
  %".5" = load i32, i32* %"a"
  %".6" = xor i32 %".5", -1
  %".7" = icmp ne i32 %".6", 0
  br i1 %".7", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: printf("%d", a);
  ; printf("%d", a)
  %".11" = load i32, i32* %"a"
  %".12" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_4_8" to i8*), i32 %".11")
  br label %"w_condition"
w_after:
  ret i32 0
}

@"printf_format_4_8" = constant [3 x i8] c"%d\0a"
declare i32 @"printf"(i8* %".1", ...)
