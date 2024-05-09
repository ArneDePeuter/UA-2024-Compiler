; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a = 0;
  %"a" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"a"
  ; C Syntax: int counter = 0;
  %"counter" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"counter"
  ; C Syntax: while (counter < 1000000) {-        a++;-        counter++;-    }
  br label %"w_condition"
w_condition:
  ; C Syntax: counter < 1000000
  %".11" = load i32, i32* %"counter"
  %".12" = icmp slt i32 %".11", 1000000
  br i1 %".12", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        a++;-        counter++;-    }
  ; C Syntax: a++;
  ; C Syntax: a++
  %".17" = load i32, i32* %"a"
  %".18" = add i32 %".17", 1
  store i32 %".18", i32* %"a"
  ; C Syntax: counter++;
  ; C Syntax: counter++
  %".22" = load i32, i32* %"counter"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* %"counter"
  br label %"w_condition"
w_after:
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".28" = bitcast [3 x i8]* @"05b762c9-5457-4ff6-b25d-111625b909c9" to i8*
  %".29" = load i32, i32* %"a"
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".28", i32 %".29")
  ret i32 0
}

@"05b762c9-5457-4ff6-b25d-111625b909c9" = constant [3 x i8] c"%d\00"