; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a = 10;
  %"a" = alloca i32
  ; C Syntax: 10
  store i32 10, i32* %"a"
  ; C Syntax: if (a > 5) {-        printf("%d", a);-    }
  ; C Syntax: a > 5
  %".7" = load i32, i32* %"a"
  %".8" = icmp sgt i32 %".7", 5
  br i1 %".8", label %"entry.if", label %"entry.endif"
entry.if:
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".12" = bitcast [3 x i8]* @"63b3a658-dfb7-4953-8dd3-8e3527607835" to i8*
  %".13" = load i32, i32* %"a"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".13")
  br label %"entry.endif"
entry.endif:
  ret i32 0
}

@"63b3a658-dfb7-4953-8dd3-8e3527607835" = constant [3 x i8] c"%d\00"