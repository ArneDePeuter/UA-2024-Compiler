; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; char x = 'x';
  %"x" = alloca i8
  store i8 120, i8* %"x"
  ; char dot = '.';
  %"dot" = alloca i8
  store i8 46, i8* %"dot"
  ret i32 0
}
