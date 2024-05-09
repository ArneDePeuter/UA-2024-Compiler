; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int f[10][10];
  %"f" = alloca [10 x [10 x i32]]
  store [10 x [10 x i32]] zeroinitializer, [10 x [10 x i32]]* %"f"
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
