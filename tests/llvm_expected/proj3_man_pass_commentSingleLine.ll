; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; // line 1
  ; char c = '\n';
  %"c" = alloca i8
  store i8 10, i8* %"c"
  ; float f = 33.1;
  %"f" = alloca double
  store double 0x40408ccccccccccd, double* %"f"
  ; // another line
  ; /////// some documentation
  ; /////////////////////////////////////
  ; // abcdef 123 //////////
  ; float final_line = 33.99895;
  %"final_line" = alloca double
  store double 0x4040ffdd97f62b6b, double* %"final_line"
  ret i32 0
}
