; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a = 1;
  %"a" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"a"
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  ; C Syntax: a
  %".8" = load i32, i32* %"a"
  %".9" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_5_4" to i8*), i32 %".8")
  ret i32 0
}

@"printf_format_5_4" = internal constant [3 x i8] c"%d\00"