; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; C Syntax: 1 +    3 * 877 + (    33     +                5        )    ;
  %".3" = mul i32 3, 877
  %".4" = add i32 1, %".3"
  %".5" = add i32 33, 5
  %".6" = add i32 %".4", %".5"
  ret i32 0
}
