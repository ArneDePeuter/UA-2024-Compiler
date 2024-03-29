; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; bool x = 1;
  %"x" = alloca i32
  store i32 1, i32* %"x"
  ; bool y = 0;
  %"y" = alloca i32
  store i32 0, i32* %"y"
  ; int z = x && y;
  %"z" = alloca i32
  %".7" = load i32, i32* %"x"
  %".8" = load i32, i32* %"y"
  %".9" = and i32 %".7", %".8"
  store i32 %".9", i32* %"z"
  ; bool b = y * z * 57809;
  %"b" = alloca i32
  %".12" = load i32, i32* %"y"
  %".13" = load i32, i32* %"z"
  %".14" = mul i32 %".12", %".13"
  %".15" = mul i32 %".14", 57809
  store i32 %".15", i32* %"b"
  ret i32 0
}
