; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char* str = "Hello, World!";
  %"str" = alloca i8*
  ; C Syntax: "Hello, World!"
  %"str_array" = alloca [14 x i8]
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"str_array"
  %".5" = getelementptr [14 x i8], [14 x i8]* %"str_array", i32 0, i32 0
  store i8* %".5", i8** %"str"
  ; C Syntax: printf("%s", str);
  ; C Syntax: printf("%s", str)
  %".9" = bitcast [3 x i8]* @"c638c025-9ffc-4328-ab0e-5ed48629a815" to i8*
  %".10" = load i8*, i8** %"str"
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".9", i8* %".10")
  ret i32 0
}

@"c638c025-9ffc-4328-ab0e-5ed48629a815" = constant [3 x i8] c"%s\00"