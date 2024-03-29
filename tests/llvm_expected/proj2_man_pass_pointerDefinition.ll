; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int x = 98362;
  %"x" = alloca i32
  store i32 98362, i32* %"x"
  ; int* x_ptr = &x;
  %"x_ptr" = alloca i32*
  %".5" = load i32, i32* %"x"
  store i32* %"x", i32** %"x_ptr"
  ; int** p = &x_ptr;
  %"p" = alloca i32**
  %".8" = load i32*, i32** %"x_ptr"
  store i32** %"x_ptr", i32*** %"p"
  ; int* z = &x;
  %"z" = alloca i32*
  %".11" = load i32, i32* %"x"
  store i32* %"x", i32** %"z"
  ; float a = 856.25668;
  %"a" = alloca double
  store double 0x408ac20dae3e6c4c, double* %"a"
  ; float* a_ptr = &a;
  %"a_ptr" = alloca double*
  %".16" = load double, double* %"a"
  store double* %"a", double** %"a_ptr"
  ret i32 0
}
