; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; C Syntax: 1326549 + 215492154;
  %".3" = add i32 1326549, 215492154
  ; C Syntax: 548416;
  ; C Syntax: 3-6;
  %".6" = sub i32 3, 6
  ; C Syntax: -9899563254;
  %".8" = sub i32 0, 9899563254
  ; C Syntax: +998315;
  ret i32 0
}
