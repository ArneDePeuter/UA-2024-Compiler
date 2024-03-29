; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int x = -60;
  %"x" = alloca i32
  %".3" = sub i32 0, 60
  store i32 %".3", i32* %"x"
  ; int* some_pointer = &x;
  %"some_pointer" = alloca i32*
  %".6" = load i32, i32* %"x"
  store i32* %"x", i32** %"some_pointer"
  %".8" = load i32*, i32** %"some_pointer"
  %".9" = load i32, i32* %".8"
  %".10" = alloca i32
  store i32 53, i32* %".10"
  ; int** another_pointer = &some_pointer;
  %"another_pointer" = alloca i32**
  %".13" = load i32*, i32** %"some_pointer"
  store i32** %"some_pointer", i32*** %"another_pointer"
  ; int*** triple_pointer = &another_pointer;
  %"triple_pointer" = alloca i32***
  %".16" = load i32**, i32*** %"another_pointer"
  store i32*** %"another_pointer", i32**** %"triple_pointer"
  ; int y = ***triple_pointer;
  %"y" = alloca i32
  %".19" = load i32***, i32**** %"triple_pointer"
  %".20" = load i32**, i32*** %".19"
  %".21" = load i32*, i32** %".20"
  %".22" = load i32, i32* %".21"
  store i32 %".22", i32* %"y"
  ret i32 0
}
