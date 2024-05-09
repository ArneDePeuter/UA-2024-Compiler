; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a[5];
  %"a" = alloca [5 x i32]
  store [5 x i32] zeroinitializer, [5 x i32]* %"a"
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
