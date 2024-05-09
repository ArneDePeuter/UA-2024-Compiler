; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a[5] = {1, 2, 3, 4, 5};
  %"a" = alloca [5 x i32]
  ; C Syntax: {1, 2, 3, 4, 5}
  ; C Syntax: 1
  ; C Syntax: 2
  ; C Syntax: 3
  ; C Syntax: 4
  ; C Syntax: 5
  store [5 x i32] [i32 1, i32 2, i32 3, i32 4, i32 5], [5 x i32]* %"a"
  ; C Syntax: a[0] = 58;
  ; C Syntax: a[0]
  %".12" = load [5 x i32], [5 x i32]* %"a"
  %".13" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 0
  %".14" = load i32, i32* %".13"
  ; C Syntax: 58
  store i32 58, i32* %".13"
  ret i32 0
}
