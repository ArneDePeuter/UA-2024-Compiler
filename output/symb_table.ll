; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"globalVar" = global i32 10
define i32 @"add"(i32 %".1", i32 %".2")
{
entry:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"b" = alloca i32
  store i32 %".2", i32* %"b"
  ; C Syntax: int sum = a + b;
  %"sum" = alloca i32
  ; C Syntax: a + b
  %".8" = load i32, i32* %"a"
  %".9" = load i32, i32* %"b"
  %".10" = add i32 %".8", %".9"
  store i32 %".10", i32* %"sum"
  ; // Local variable in add function
  ;
  ; C Syntax: {-        int scopeVar = 20; // Block scope variable inside add function-    }
  ; C Syntax: int scopeVar = 20;
  %"scopeVar" = alloca i32
  ; C Syntax: 20
  store i32 20, i32* %"scopeVar"
  ; // Block scope variable inside add function
  ;
  ; C Syntax: int localVar = 30;
  %"localVar" = alloca i32
  ; C Syntax: 30
  store i32 30, i32* %"localVar"
  ; // Local variable in add function
  ;
  ; C Syntax: return sum;
  ; C Syntax: sum
  %".27" = load i32, i32* %"sum"
  ret i32 %".27"
}

define i32 @"main"()
{
entry:
  ; C Syntax: int scope1Var = 30;
  %"scope1Var" = alloca i32
  ; C Syntax: 30
  store i32 30, i32* %"scope1Var"
  ; // Local variable in main
  ;
  ; C Syntax: {-        int scope2Var = 40; // Block scope variable inside if statement-    }
  ; C Syntax: int scope2Var = 40;
  %"scope2Var" = alloca i32
  ; C Syntax: 40
  store i32 40, i32* %"scope2Var"
  ; // Block scope variable inside if statement
  ;
  ; C Syntax: int localVar = 50;
  %"localVar" = alloca i32
  ; C Syntax: 50
  store i32 50, i32* %"localVar"
  ; // Local variable in main
  ;
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
