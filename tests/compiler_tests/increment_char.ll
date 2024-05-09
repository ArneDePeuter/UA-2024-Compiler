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
  ; C Syntax: b++;
  ; C Syntax: b++
  %".7" = load i8, i8* %"b"
  %".8" = add i8 %".7", 1
  store i8 %".8", i8* %"b"
  ; C Syntax: printf("%c", b);
  ; C Syntax: printf("%c", b)
  %".12" = bitcast [3 x i8]* @"1be8a312-2ee2-4e97-963b-8ffb4c731351" to i8*
  %".13" = load i8, i8* %"b"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".12", i8 %".13")
  ret i32 0
}

@"1be8a312-2ee2-4e97-963b-8ffb4c731351" = constant [3 x i8] c"%c\00"