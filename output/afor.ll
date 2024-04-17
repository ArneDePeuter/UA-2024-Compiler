; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 0, i32* %"a"
  br label %"w_condition"
w_condition:
  %".4" = load i32, i32* %"a"
  %".5" = icmp slt i32 %".4", 10
  br i1 %".5", label %"w_body", label %"w_after"
w_body:
  %".7" = load i32, i32* %"a"
  %".8" = add i32 %".7", 1
  store i32 %".8", i32* %"a"
  %".10" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_4_8" to i8*), i32 %".8")
  br label %"w_condition"
w_after:
  ret i32 0
}

@"printf_format_4_8" = constant [3 x i8] c"%d\0a"