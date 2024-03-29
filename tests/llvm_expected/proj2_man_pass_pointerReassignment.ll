; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; const int b = -6250;
  %"b" = alloca i32
  %".3" = sub i32 0, 6250
  store i32 %".3", i32* %"b"
  ; const int x = 5;
  %"x" = alloca i32
  store i32 5, i32* %"x"
  ; int* non_const_pointer = &x;
  %"non_const_pointer" = alloca i32*
  %".8" = load i32, i32* %"x"
  store i32* %"x", i32** %"non_const_pointer"
  %".10" = load i32*, i32** %"non_const_pointer"
  %".11" = load i32, i32* %".10"
  %".12" = alloca i32
  store i32 36941, i32* %".12"
  %".14" = load i32*, i32** %"non_const_pointer"
  %".15" = load i32, i32* %"b"
  %".16" = ptrtoint i32* %"b" to i32
  store i32 %".16", i32* %".14"
  ; char c = 'x';
  %"c" = alloca i8
  store i8 120, i8* %"c"
  ; char nl = '\n';
  %"nl" = alloca i8
  store i8 10, i8* %"nl"
  ; char* char_ptr = &c;
  %"char_ptr" = alloca i8*
  %".23" = load i8, i8* %"c"
  store i8* %"c", i8** %"char_ptr"
  %".25" = load i8*, i8** %"char_ptr"
  %".26" = load i8, i8* %".25"
  %".27" = alloca i8
  store i8 9, i8* %".27"
  %".29" = load i8*, i8** %"char_ptr"
  %".30" = load i8, i8* %"nl"
  %".31" = ptrtoint i8* %"nl" to i8
  store i8 %".31", i8* %".29"
  ret i32 0
}
