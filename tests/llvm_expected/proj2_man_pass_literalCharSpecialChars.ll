; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; char nl = '\n';
  %"nl" = alloca i8
  store i8 10, i8* %"nl"
  ; char tab = '\t';
  %"tab" = alloca i8
  store i8 9, i8* %"tab"
  ; char character_null = '\0';
  %"character_null" = alloca i8
  store i8 0, i8* %"character_null"
  ret i32 0
}
