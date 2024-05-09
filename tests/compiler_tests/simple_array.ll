; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a[5];
  %"a" = alloca [5 x i32]
  store [5 x i32] zeroinitializer, [5 x i32]* %"a"
  ; C Syntax: a[0] = 1;
  ; C Syntax: a[0]
  %".6" = load [5 x i32], [5 x i32]* %"a"
  %".7" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 0
  %".8" = load i32, i32* %".7"
  ; C Syntax: 1
  store i32 1, i32* %".7"
  ret i32 0
}
