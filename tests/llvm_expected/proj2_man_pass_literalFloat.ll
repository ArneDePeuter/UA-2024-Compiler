; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; float x = 0.478984;
  %"x" = alloca double
  store double 0x3fdea7ac81d3aa37, double* %"x"
  ; float y = 5489451.245847;
  %"y" = alloca double
  store double 0x4154f0cacfbbf50e, double* %"y"
  ; float f = 1654.0000;
  %"f" = alloca double
  store double 0x4099d80000000000, double* %"f"
  ; float z = 0000.00000;
  %"z" = alloca double
  store double              0x0, double* %"z"
  %".10" = load double, double* %"z"
  %".11" = sub double              0x0, 0x4081a9b94855da27
  %".12" = alloca double
  store double %".11", double* %".12"
  ret i32 0
}
