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
  ; C Syntax: i < 5;
  %".16" = load i32, i32* %"i"
  %".17" = icmp slt i32 %".16", 5
  br i1 %".17", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        printf("%d\n", a[i]);-    }
  ; C Syntax: printf("%d\n", a[i]);
  ; C Syntax: printf("%d\n", a[i])
  %".22" = bitcast [4 x i8]* @"0f60005c-5150-400a-8692-32aac04ec930" to i8*
  %".23" = load [5 x i32], [5 x i32]* %"a"
  %".24" = load i32, i32* %"i"
  %".25" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 %".24"
  %".26" = load i32, i32* %".25"
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %".26")
  ; C Syntax: i++
  ; C Syntax: i++
  %".30" = load i32, i32* %"i"
  %".31" = add i32 %".30", 1
  store i32 %".31", i32* %"i"
  br label %"w_condition"
w_after:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"0f60005c-5150-400a-8692-32aac04ec930" = constant [4 x i8] c"%d\0a\00"