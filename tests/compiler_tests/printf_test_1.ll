; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char b = 'a';
  %"b" = alloca i8
  ; C Syntax: 'a'
  store i8 97, i8* %"b"
  ; C Syntax: printf("%c", b);
  ; C Syntax: printf("%c", b)
  %".7" = bitcast [3 x i8]* @"a13b97bd-cce4-4553-b79a-6868c1744006" to i8*
  %".8" = load i8, i8* %"b"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".7", i8 %".8")
  ; C Syntax: printf("%c", 'b');
  ; C Syntax: printf("%c", 'b')
  %".12" = bitcast [3 x i8]* @"fda936cf-70d6-4840-b587-3a172d3b0f41" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i8 98)
  ret i32 0
}

@"a13b97bd-cce4-4553-b79a-6868c1744006" = constant [3 x i8] c"%c\00"
@"fda936cf-70d6-4840-b587-3a172d3b0f41" = constant [3 x i8] c"%c\00"