; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: for (int l = 0; l < 5; l++) {-        if (l == 3) {-            continue;-        }-        printf("%d\n", l);-    }
  ; C Syntax: int l = 0;
  %"l" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"l"
  br label %"w_condition"
w_condition:
  ; C Syntax: l < 5;
  %".8" = load i32, i32* %"l"
  %".9" = icmp slt i32 %".8", 5
  br i1 %".9", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        if (l == 3) {-            continue;-        }-        printf("%d\n", l);-    }
  ; C Syntax: if (l == 3) {-            continue;-        }
  ; C Syntax: l == 3
  %".14" = load i32, i32* %"l"
  %".15" = icmp eq i32 %".14", 3
  br i1 %".15", label %"w_body.if", label %"w_body.endif"
w_after:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
w_body.if:
  ; C Syntax: l++
  ; C Syntax: l++
  %".19" = load i32, i32* %"l"
  %".20" = add i32 %".19", 1
  store i32 %".20", i32* %"l"
  ; C Syntax: continue;
  br label %"w_condition"
w_body.endif:
  ; C Syntax: printf("%d\n", l);
  ; C Syntax: printf("%d\n", l)
  %".26" = bitcast [4 x i8]* @"6988845c-9407-410e-8867-fcdab85b78dd" to i8*
  %".27" = load i32, i32* %"l"
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".26", i32 %".27")
  ; C Syntax: l++
  ; C Syntax: l++
  %".31" = load i32, i32* %"l"
  %".32" = add i32 %".31", 1
  store i32 %".32", i32* %"l"
  br label %"w_condition"
}

@"6988845c-9407-410e-8867-fcdab85b78dd" = constant [4 x i8] c"%d\0a\00"