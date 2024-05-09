; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char b = '\n';
  %"b" = alloca i8
  ; C Syntax: '\n'
  store i8 10, i8* %"b"
  ; C Syntax: printf("%c", b);
  ; C Syntax: printf("%c", b)
  %".7" = bitcast [3 x i8]* @"4f05ce09-adc4-4e8b-9d28-a734204b5d82" to i8*
  %".8" = load i8, i8* %"b"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".7", i8 %".8")
  ret i32 0
}

@"4f05ce09-adc4-4e8b-9d28-a734204b5d82" = constant [3 x i8] c"%c\00"