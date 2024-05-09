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
  %".12" = bitcast [3 x i8]* @"e0349fdb-dbbb-4d93-b5d8-4edb2838993e" to i8*
  %".13" = load i32, i32* %"a"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".13")
  br label %"entry.endif"
entry.endif:
  ; C Syntax: if (a == 10) {-        printf("%d", a);-    }
  ; C Syntax: a == 10
  %".18" = load i32, i32* %"a"
  %".19" = icmp eq i32 %".18", 10
  br i1 %".19", label %"entry.endif.if", label %"entry.endif.endif"
entry.endif.if:
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".23" = bitcast [3 x i8]* @"bc0187b1-defb-4acf-8542-2763907db02d" to i8*
  %".24" = load i32, i32* %"a"
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %".24")
  br label %"entry.endif.endif"
entry.endif.endif:
  ret i32 0
}

@"e0349fdb-dbbb-4d93-b5d8-4edb2838993e" = constant [3 x i8] c"%d\00"
@"bc0187b1-defb-4acf-8542-2763907db02d" = constant [3 x i8] c"%d\00"