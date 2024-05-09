; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int f[10][10];
  %"f" = alloca [10 x [10 x i32]]
  store [10 x [10 x i32]] zeroinitializer, [10 x [10 x i32]]* %"f"
  ; C Syntax: f[0][0] = 1;
  ; C Syntax: f[0][0]
  %".6" = load [10 x [10 x i32]], [10 x [10 x i32]]* %"f"
  %".7" = getelementptr [10 x [10 x i32]], [10 x [10 x i32]]* %"f", i32 0, i32 0
  %".8" = load [10 x i32], [10 x i32]* %".7"
  %".9" = getelementptr [10 x i32], [10 x i32]* %".7", i32 0, i32 0
  %".10" = load i32, i32* %".9"
  ; C Syntax: 1
  store i32 1, i32* %".9"
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
