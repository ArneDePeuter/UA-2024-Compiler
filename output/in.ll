; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char str[] = "Hello, World!";
  %"str" = alloca [14 x i8]
  ; C Syntax: "Hello, World!"
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"str"
  ; C Syntax: // Mutable array-
  ; // Mutable array
  ; C Syntax: char *ptr = str;
  %"ptr" = alloca i8*
  ; C Syntax: str
  %".9" = load [14 x i8], [14 x i8]* %"str"
  %"ptr_array" = alloca [14 x i8]
  store [14 x i8] %".9", [14 x i8]* %"ptr_array"
  %".11" = getelementptr [14 x i8], [14 x i8]* %"ptr_array", i32 0, i32 0
  store i8* %".11", i8** %"ptr"
  ; C Syntax: printf("%c", *ptr);
  ; C Syntax: printf("%c", *ptr)
  ; C Syntax: *ptr
  %".16" = load i8*, i8** %"ptr"
  %".17" = load i8, i8* %".16"
  %".18" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_4_4" to i8*), i8 %".17")
  ; C Syntax: printf("%s", ptr);
  ; C Syntax: printf("%s", ptr)
  ; C Syntax: ptr
  %".22" = load i8*, i8** %"ptr"
  %".23" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_5_4" to i8*), i8* %".22")
  ; C Syntax: ptr[7] = 'P';
  ; C Syntax: ptr[7]
  ; C Syntax: 7
  %".27" = load i8*, i8** %"ptr"
  %".28" = getelementptr i8, i8* %".27", i32 7
  %".29" = load i8, i8* %".28"
  ; C Syntax: 'P'
  store i8 80, i8* %".28"
  ; C Syntax: // Modify the string through the pointer-
  ; // Modify the string through the pointer
  ; C Syntax: printf("%s", ptr);
  ; C Syntax: printf("%s", ptr)
  ; C Syntax: ptr
  %".37" = load i8*, i8** %"ptr"
  %".38" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_7_4" to i8*), i8* %".37")
  ; C Syntax: // Prints "Hello, Porld!"-
  ; // Prints "Hello, Porld!"
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"printf_format_4_4" = internal constant [3 x i8] c"%c\00"
@"printf_format_5_4" = internal constant [3 x i8] c"%s\00"
@"printf_format_7_4" = internal constant [3 x i8] c"%s\00"