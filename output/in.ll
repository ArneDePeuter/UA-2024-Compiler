; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int chars_printed = printf("Hello, %s!", "World");
  %"chars_printed" = alloca i32
  ; C Syntax: printf("Hello, %s!", "World")
  ; C Syntax: "World"
  %".5" = call i32 (i8*, ...) @"printf"(i8* bitcast ([13 x i8]* @"printf_format_2_24" to i8*))
  store i32 0, i32* %"chars_printed"
  ; C Syntax: printf("Counting: %d %d %d %d %d", 1.5, 2, 3, 4, 5);
  ; C Syntax: printf("Counting: %d %d %d %d %d", 1.5, 2, 3, 4, 5)
  ; C Syntax: 1.5
  ; C Syntax: 2
  ; C Syntax: 3
  ; C Syntax: 4
  ; C Syntax: 5
  %".14" = call i32 (i8*, ...) @"printf"(i8* bitcast ([27 x i8]* @"printf_format_3_4" to i8*), i32 2, i32 3, i32 4, i32 5)
  ; C Syntax: printf("Hello, World!");
  ; C Syntax: printf("Hello, World!")
  %".17" = call i32 (i8*, ...) @"printf"(i8* bitcast ([16 x i8]* @"printf_format_4_4" to i8*))
  ; C Syntax: printf("Argument %d", 1);
  ; C Syntax: printf("Argument %d", 1)
  ; C Syntax: 1
  %".21" = call i32 (i8*, ...) @"printf"(i8* bitcast ([14 x i8]* @"printf_format_5_4" to i8*), i32 1)
  ret i32 0
}

@"printf_format_2_24" = internal constant [13 x i8] c"\22Hello, %s!\22\00"
@"printf_format_3_4" = internal constant [27 x i8] c"\22Counting: %d %d %d %d %d\22\00"
@"printf_format_4_4" = internal constant [16 x i8] c"\22Hello, World!\22\00"
@"printf_format_5_4" = internal constant [14 x i8] c"\22Argument %d\22\00"