; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; const int x = 5;
  %"x" = alloca i32
  store i32 5, i32* %"x"
  ; const float f = 0.5487;
  %"f" = alloca double
  store double 0x3fe18ef34d6a161e, double* %"f"
  ; const int y = x * 35 * -5;
  %"y" = alloca i32
  %".7" = load i32, i32* %"x"
  %".8" = mul i32 %".7", 35
  %".9" = sub i32 0, 5
  %".10" = mul i32 %".8", %".9"
  store i32 %".10", i32* %"y"
  ; const float z = f * f * f;
  %"z" = alloca double
  %".13" = load double, double* %"f"
  %".14" = load double, double* %"f"
  %".15" = fmul double %".13", %".14"
  %".16" = load double, double* %"f"
  %".17" = fmul double %".15", %".16"
  store double %".17", double* %"z"
  ret i32 0
}
