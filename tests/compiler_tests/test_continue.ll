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
  ; C Syntax: while (counter < 1000000) {-        counter++;-        continue;-        a++;-    }
  br label %"w_condition"
w_condition:
  ; C Syntax: counter < 1000000
  %".11" = load i32, i32* %"counter"
  %".12" = icmp slt i32 %".11", 1000000
  br i1 %".12", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        counter++;-        continue;-        a++;-    }
  ; C Syntax: counter++;
  ; C Syntax: counter++
  %".17" = load i32, i32* %"counter"
  %".18" = add i32 %".17", 1
  store i32 %".18", i32* %"counter"
  ; C Syntax: continue;
  br label %"w_condition"
w_after:
  ; C Syntax: printf("%d", (a==0) & (counter==1000000));
  ; C Syntax: printf("%d", (a==0) & (counter==1000000))
  %".24" = bitcast [3 x i8]* @"a5f5ac87-d1fc-4724-ab5f-505d42b40125" to i8*
  ; C Syntax: a==0
  %".26" = load i32, i32* %"a"
  %".27" = icmp eq i32 %".26", 0
  ; C Syntax: counter==1000000
  %".29" = load i32, i32* %"counter"
  %".30" = icmp eq i32 %".29", 1000000
  %".31" = and i1 %".27", %".30"
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".24", i1 %".31")
  ret i32 0
}

@"a5f5ac87-d1fc-4724-ab5f-505d42b40125" = constant [3 x i8] c"%d\00"