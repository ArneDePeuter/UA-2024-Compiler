; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: printf("%f", 1.233);
  ; C Syntax: printf("%f", 1.233)
  ; C Syntax: 1.233
  %".5" = fpext float 0x3ff3ba5e40000000 to double
  %".6" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_3_4" to i8*), double %".5")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"printf_format_3_4" = internal constant [3 x i8] c"%f\00"