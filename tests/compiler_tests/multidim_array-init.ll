; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char c[2][3] = {{'a', 'b', 'c'}, {'d', 'e', 'f'}};
  %"c" = alloca [2 x [3 x i8]]
  ; C Syntax: {{'a', 'b', 'c'}, {'d', 'e', 'f'}}
  ; C Syntax: {'a', 'b', 'c'}
  ; C Syntax: 'a'
  ; C Syntax: 'b'
  ; C Syntax: 'c'
  ; C Syntax: {'d', 'e', 'f'}
  ; C Syntax: 'd'
  ; C Syntax: 'e'
  ; C Syntax: 'f'
  store [2 x [3 x i8]] [[3 x i8] [i8 97, i8 98, i8 99], [3 x i8] [i8 100, i8 101, i8 102]], [2 x [3 x i8]]* %"c"
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
