; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int x = 4;
  %"x" = alloca i32
  store i32 4, i32* %"x"
  ; int b = 9632;
  %"b" = alloca i32
  store i32 9632, i32* %"b"
  ; const int* x_ptr = &x;
  %"x_ptr" = alloca i32*
  %".7" = load i32, i32* %"x"
  store i32* %"x", i32** %"x_ptr"
  %".9" = load i32*, i32** %"x_ptr"
  %".10" = load i32, i32* %"b"
  %".11" = ptrtoint i32* %"b" to i32
  store i32 %".11", i32* %".9"
  ret i32 0
}
