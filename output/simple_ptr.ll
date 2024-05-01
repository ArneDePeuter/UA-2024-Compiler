; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a = 3;
  %"a" = alloca i32
  ; C Syntax: 3
  store i32 3, i32* %"a"
  ; C Syntax: int *a_ptr = &a;
  %"a_ptr" = alloca i32*
  ; C Syntax: &a
  %".7" = load i32, i32* %"a"
  store i32* %"a", i32** %"a_ptr"
  ret i32 0
}
