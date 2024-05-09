; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a = 1;
  %"a" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"a"
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".7" = bitcast [3 x i8]* @"0f1089ef-f62e-47e8-af73-d6a1ae9d536d" to i8*
  %".8" = load i32, i32* %"a"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".8")
  ret i32 0
}

@"0f1089ef-f62e-47e8-af73-d6a1ae9d536d" = constant [3 x i8] c"%d\00"