; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"factorial"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  ; C Syntax: if (n == 0 || n == 1) {-        return 1;-    } else {-        return n * factorial(n - 1);-    }
  ; C Syntax: n == 0 || n == 1
  %".6" = load i32, i32* %"n"
  %".7" = icmp eq i32 %".6", 0
  %".8" = load i32, i32* %"n"
  %".9" = icmp eq i32 %".8", 1
  %".10" = or i1 %".7", %".9"
  %".11" = icmp ne i1 %".10", 0
  br i1 %".11", label %"entry.if", label %"entry.else"
entry.if:
  ; C Syntax: return 1;
  ; C Syntax: 1
  ret i32 1
entry.else:
  ; C Syntax: return n * factorial(n - 1);
  ; C Syntax: n * factorial(n - 1)
  %".18" = load i32, i32* %"n"
  %".19" = load i32, i32* %"n"
  %".20" = sub i32 %".19", 1
  %".21" = call i32 @"factorial"(i32 %".20")
  %".22" = mul i32 %".18", %".21"
  ret i32 %".22"
entry.endif:
  ret i32 0
}

define i32 @"main"()
{
entry:
  ; C Syntax: int num = 5;
  %"num" = alloca i32
  ; C Syntax: 5
  store i32 5, i32* %"num"
  ; C Syntax: int result = factorial(num);
  %"result" = alloca i32
  ; C Syntax: factorial(num)
  %".7" = load i32, i32* %"num"
  %".8" = call i32 @"factorial"(i32 %".7")
  store i32 %".8", i32* %"result"
  ; C Syntax: printf("%d", num);
  ; C Syntax: printf("%d", num)
  %".12" = bitcast [3 x i8]* @"7b435b5e-599d-4595-ab53-d6325c4af3e8" to i8*
  %".13" = load i32, i32* %"num"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".13")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"7b435b5e-599d-4595-ab53-d6325c4af3e8" = constant [3 x i8] c"%d\00"