; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: const ConstInt* b = 0;
  %"b" = alloca i32*
  ; C Syntax: 0
  store i32* null, i32** %"b"
  ; C Syntax: printf("%x", b);
  ; C Syntax: printf("%x", b)
  ; C Syntax: b
  %".8" = load i32*, i32** %"b"
  %".9" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_5_4" to i8*), i32* null)
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"printf_format_5_4" = internal constant [3 x i8] c"%x\00"