; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; /*
  ;  * This is a comment
  ;  *
  ;  *
  ; int line_of_code = 5;
  %"line_of_code" = alloca i32
  store i32 5, i32* %"line_of_code"
  ; /**
  ;  * Another Comment
  ;   ***** /
  ;
  ;   /**
  ;
  ;   *
  ;   *
  ;   **
  ; float f = 45;
  %"f" = alloca double
  %".18" = sitofp i32 45 to double
  store double %".18", double* %"f"
  ; /* /// ** ** // // //  *
  ; char c = 'b';
  %"c" = alloca i8
  store i8 98, i8* %"c"
  ; int x = 5;
  %"x" = alloca i32
  store i32 5, i32* %"x"
  ret i32 0
}
