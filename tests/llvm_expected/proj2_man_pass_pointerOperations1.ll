; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; char x = 'a';
  %"x" = alloca i8
  store i8 97, i8* %"x"
  ; char* chr_ptr = &x;
  %"chr_ptr" = alloca i8*
  %".5" = load i8, i8* %"x"
  store i8* %"x", i8** %"chr_ptr"
  %".7" = load i8*, i8** %"chr_ptr"
  %".8" = load i8, i8* %".7"
  %".9" = alloca i8
  store i8 98, i8* %".9"
  ; char another_char = *chr_ptr;
  %"another_char" = alloca i8
  %".12" = load i8*, i8** %"chr_ptr"
  %".13" = load i8, i8* %".12"
  store i8 %".13", i8* %"another_char"
  ret i32 0
}
