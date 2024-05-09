; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int number = 4;
  %"number" = alloca i32
  ; C Syntax: 4
  store i32 4, i32* %"number"
  ; C Syntax: if (number > 3) {-        printf("%d", 1);-    } else {-        printf("%d", 0);-    }
  ; C Syntax: number > 3
  %".7" = load i32, i32* %"number"
  %".8" = icmp sgt i32 %".7", 3
  br i1 %".8", label %"entry.if", label %"entry.else"
entry.if:
  ; C Syntax: printf("%d", 1);
  ; C Syntax: printf("%d", 1)
  %".12" = bitcast [3 x i8]* @"aa1805fa-5ef6-4ba2-8d86-e6958a1515b2" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 1)
  br label %"entry.endif"
entry.else:
  ; C Syntax: printf("%d", 0);
  ; C Syntax: printf("%d", 0)
  %".17" = bitcast [3 x i8]* @"d31c5552-19c0-46ad-9b9c-b4f813b2ca0b" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 0)
  br label %"entry.endif"
entry.endif:
  ret i32 0
}

@"aa1805fa-5ef6-4ba2-8d86-e6958a1515b2" = constant [3 x i8] c"%d\00"
@"d31c5552-19c0-46ad-9b9c-b4f813b2ca0b" = constant [3 x i8] c"%d\00"