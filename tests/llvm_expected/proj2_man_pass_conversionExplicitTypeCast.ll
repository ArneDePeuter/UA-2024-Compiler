; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int x = 5;
  %"x" = alloca i32
  store i32 5, i32* %"x"
  ; float f = 33989.586265;
  %"f" = alloca double
  store double 0x40e098b2c2aed139, double* %"f"
  ; int z = (int) f;
  %"z" = alloca i32
  %".7" = load double, double* %"f"
  %".8" = fptosi double %".7" to i32
  store i32 %".8", i32* %"z"
  ; float z2 = (float) x;
  %"z2" = alloca double
  %".11" = load i32, i32* %"x"
  %".12" = sitofp i32 %".11" to double
  store double %".12", double* %"z2"
  ; int a = (int) (f + z2 * 2);
  %"a" = alloca i32
  %".15" = load double, double* %"f"
  %".16" = load double, double* %"z2"
  %".17" = sitofp i32 2 to double
  %".18" = fmul double %".16", %".17"
  %".19" = fadd double %".15", %".18"
  %".20" = fptosi double %".19" to i32
  store i32 %".20", i32* %"a"
  ; float f2 = (float) f;
  %"f2" = alloca double
  %".23" = load double, double* %"f"
  store double %".23", double* %"f2"
  %".25" = load double, double* %"f2"
  %".26" = load i32, i32* %"a"
  %".27" = load double, double* %"z2"
  %".28" = mul i32 3, 65232
  %".29" = sitofp i32 %".28" to double
  %".30" = fdiv double %".27", %".29"
  %".31" = sitofp i32 %".26" to double
  %".32" = fadd double %".31", %".30"
  %".33" = alloca double
  store double %".32", double* %".33"
  ret i32 0
}
