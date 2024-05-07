; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a = 3;
  %"a" = alloca i32
  ; C Syntax: 3
  store i32 3, i32* %"a"
  ; C Syntax: int arr[1] = {a};
  %"arr" = alloca [1 x i32]
  ; C Syntax: {a}
  ; C Syntax: 3
  store [1 x i32] [i32 3], [1 x i32]* %"arr"
  ; C Syntax: //    int *arr[1] = {&a};-
  ; //    int *arr[1] = {&a};
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
