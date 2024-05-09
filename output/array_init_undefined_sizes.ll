; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a[] = {1, 2, 3, 4, 5};
  %"a" = alloca [5 x i32]
  ; C Syntax: {1, 2, 3, 4, 5}
  ; C Syntax: 1
  ; C Syntax: 2
  ; C Syntax: 3
  ; C Syntax: 4
  ; C Syntax: 5
  store [5 x i32] [i32 1, i32 2, i32 3, i32 4, i32 5], [5 x i32]* %"a"
  ; C Syntax: for (int i = 0; i < 5; i++) {-        printf("%d\n", a[i]);-    }
  ; C Syntax: int i = 0;
  %"i" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"i"
  br label %"w_condition"
w_condition:
  %".15" = icmp ne i32 1, 0
  br i1 %".15", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        printf("%d\n", a[i]);-    }
  ; C Syntax: printf("%d\n", a[i]);
  ; C Syntax: printf("%d\n", a[i])
  %".20" = bitcast [4 x i8]* @"f0cbae8f-6b2f-4510-bacb-d80a2ee5a772" to i8*
  %".21" = load [5 x i32], [5 x i32]* %"a"
  ; C Syntax: 0
  %".23" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 0
  %".24" = load i32, i32* %".23"
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".24")
  ; C Syntax: i++
  ; C Syntax: i++
  %".28" = load i32, i32* %"i"
  %".29" = add i32 %".28", 1
  store i32 %".29", i32* %"i"
  br label %"w_condition"
w_after:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"f0cbae8f-6b2f-4510-bacb-d80a2ee5a772" = constant [4 x i8] c"%d\0a\00"