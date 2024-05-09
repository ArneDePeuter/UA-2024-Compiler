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
  ; C Syntax: if (a > 5) {-        printf("%d", a);-        if (a > 15) {-            printf("%d", a);-        } else {-            printf("%d", a);-        }-    }
  ; C Syntax: a > 5
  %".7" = load i32, i32* %"a"
  %".8" = icmp sgt i32 %".7", 5
  br i1 %".8", label %"entry.if", label %"entry.endif"
entry.if:
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".12" = bitcast [3 x i8]* @"27aaa51f-4e8d-4ff7-88ec-ea1c7ee19f74" to i8*
  %".13" = load i32, i32* %"a"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".13")
  ; C Syntax: if (a > 15) {-            printf("%d", a);-        } else {-            printf("%d", a);-        }
  ; C Syntax: a > 15
  %".17" = load i32, i32* %"a"
  %".18" = icmp sgt i32 %".17", 15
  br i1 %".18", label %"entry.if.if", label %"entry.if.else"
entry.endif:
  ret i32 0
entry.if.if:
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".22" = bitcast [3 x i8]* @"0b0f348f-9b7a-4031-b901-5fecd5bf6b8d" to i8*
  %".23" = load i32, i32* %"a"
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %".23")
  br label %"entry.if.endif"
entry.if.else:
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".28" = bitcast [3 x i8]* @"97c75523-2eb7-4fae-918b-166d7840d7bf" to i8*
  %".29" = load i32, i32* %"a"
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".28", i32 %".29")
  br label %"entry.if.endif"
entry.if.endif:
  br label %"entry.endif"
}

@"27aaa51f-4e8d-4ff7-88ec-ea1c7ee19f74" = constant [3 x i8] c"%d\00"
@"0b0f348f-9b7a-4031-b901-5fecd5bf6b8d" = constant [3 x i8] c"%d\00"
@"97c75523-2eb7-4fae-918b-166d7840d7bf" = constant [3 x i8] c"%d\00"