; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int x;
  %"x" = alloca i32
  store i32 0, i32* %"x"
  ; C Syntax: int y = 5;
  %"y" = alloca i32
  ; C Syntax: 5
  store i32 5, i32* %"y"
  ; C Syntax: int* ptr = &x;
  %"ptr" = alloca i32*
  ; C Syntax: &x
  %".9" = load i32, i32* %"x"
  store i32* %"x", i32** %"ptr"
  ; C Syntax: printf("%d", *ptr);
  ; C Syntax: printf("%d", *ptr)
  %".13" = load i32*, i32** %"ptr"
  %".14" = load i32, i32* %".13"
  %".15" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_8_4" to i8*), i32 %".14")
  ret i32 0
}

@"printf_format_8_4" = constant [3 x i8] c"%d\0a"