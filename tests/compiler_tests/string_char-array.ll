; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char c[7] = "Hello!";
  %"c" = alloca [7 x i8]
  ; C Syntax: "Hello!"
  store [7 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 33, i8 0], [7 x i8]* %"c"
  ; C Syntax: printf("%c", c[0]);
  ; C Syntax: printf("%c", c[0])
  %".7" = bitcast [3 x i8]* @"eb223a00-b023-4c53-accd-91f9527f6239" to i8*
  %".8" = load [7 x i8], [7 x i8]* %"c"
  %".9" = getelementptr [7 x i8], [7 x i8]* %"c", i32 0, i32 0
  %".10" = load i8, i8* %".9"
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".7", i8 %".10")
  ret i32 0
}

@"eb223a00-b023-4c53-accd-91f9527f6239" = constant [3 x i8] c"%c\00"