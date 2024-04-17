; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %".3" = load i32, i32* %"a"
  %".4" = add i32 %".3", 1
  store i32 %".4", i32* %"a"
  %".6" = load i32, i32* %"a"
  %".7" = sub i32 %".6", 1
  store i32 %".7", i32* %"a"
  %".9" = load i32, i32* %"a"
  %".10" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_9_4" to i8*), i32 %".9")
  ret i32 0
}

@"printf_format_9_4" = constant [3 x i8] c"%d\0a"