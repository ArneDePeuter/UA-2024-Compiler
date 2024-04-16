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
  %".5" = icmp slt i32 %".4", 10
  br i1 %".5", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: printf("%d", a);
  ; printf("%d", a)
  %".9" = load i32, i32* %"a"
  %".10" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_4_8" to i8*), i32 %".9")
  %".11" = load i32, i32* %"a"
  %".12" = load i32, i32* %"a"
  %".13" = add i32 %".12", 1
  %".14" = alloca i32
  store i32 %".13", i32* %".14"
  %".16" = load i32, i32* %".14"
  %".17" = icmp slt i32 %".16", 10
  br i1 %".17", label %"w_body", label %"w_after"
w_after:
  ret i32 0
}

@"printf_format_4_8" = constant [3 x i8] c"%d\0a"
declare i32 @"printf"(i8* %".1", ...)
