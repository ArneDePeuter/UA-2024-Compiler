; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"factorial"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  ; C Syntax: if(n == 0) {-      return 1;-   } else {-      return n * factorial(n-1);-   }
  ; C Syntax: n == 0
  %".6" = load i32, i32* %"n"
  %".7" = icmp eq i32 %".6", 0
  br i1 %".7", label %"entry.if", label %"entry.else"
entry.if:
  ; C Syntax: return 1;
  ; C Syntax: 1
  ret i32 1
entry.else:
  ; C Syntax: return n * factorial(n-1);
  ; C Syntax: n * factorial(n-1)
  %".14" = load i32, i32* %"n"
  %".15" = load i32, i32* %"n"
  %".16" = sub i32 %".15", 1
  %".17" = call i32 @"factorial"(i32 %".16")
  %".18" = mul i32 %".14", %".17"
  ret i32 %".18"
entry.endif:
  ret i32 0
}

define i32 @"main"()
{
entry:
  ; C Syntax: printf("%d", factorial(5));
  ; C Syntax: printf("%d", factorial(5))
  %".4" = bitcast [3 x i8]* @"f12d21b6-b867-4459-833e-ada53cad283e" to i8*
  %".5" = call i32 @"factorial"(i32 5)
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".5")
  ret i32 0
}

@"f12d21b6-b867-4459-833e-ada53cad283e" = constant [3 x i8] c"%d\00"