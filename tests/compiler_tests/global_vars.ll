; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"a" = global i32 3
define i32 @"main"()
{
entry:
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".4" = bitcast [3 x i8]* @"a442c2f3-d34e-41d5-a2e0-c9fcb5161d94" to i8*
  %".5" = load i32, i32* @"a"
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".5")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"a442c2f3-d34e-41d5-a2e0-c9fcb5161d94" = constant [3 x i8] c"%d\00"