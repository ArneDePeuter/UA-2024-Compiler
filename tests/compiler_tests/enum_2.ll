; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"test"()
{
entry:
  %"MONDAY" = alloca i32
  store i32 0, i32* %"MONDAY"
  %"TUESDAY" = alloca i32
  store i32 1, i32* %"TUESDAY"
  ; C Syntax: enum Days day;
  %"day" = alloca i32
  store i32 0, i32* %"day"
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

define i32 @"main"()
{
entry:
  ; C Syntax: test();
  ; C Syntax: test()
  %".4" = call i32 @"test"()
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
