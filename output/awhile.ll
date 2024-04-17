; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int a = 0;
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %".4" = load i32, i32* %"a"
  %".5" = load i32, i32* %"a"
  %".6" = add i32 %".5", 1
  %".7" = alloca i32
  store i32 %".6", i32* %".7"
  ; C Syntax: printf("%d", a);
  ; printf("%d", a)
  %".11" = load i32, i32* %".7"
  %".12" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_6_4" to i8*), i32 %".11")
  ret i32 0
}

@"printf_format_6_4" = constant [3 x i8] c"%d\0a"
declare i32 @"printf"(i8* %".1", ...)
