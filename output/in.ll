; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

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
  ; C Syntax: char c[] = "Hello, World!";
  %"c" = alloca [14 x i8]
  ; C Syntax: "Hello, World!"
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"c"
  ; C Syntax: char* str = "Hello, World!";
  %"str" = alloca i8*
  ; C Syntax: "Hello, World!"
  store i8* getelementptr ([14 x i8], [14 x i8]* @"str_str", i32 0, i32 0), i8** %"str"
  ret i32 0
}

@"str_str" = internal constant [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0]