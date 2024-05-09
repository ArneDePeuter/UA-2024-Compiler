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
  ; C Syntax: while (counter < 1000000) {-        a++;-        break;-        counter++;-    }
  br label %"w_condition"
w_condition:
  ; C Syntax: counter < 1000000
  %".11" = load i32, i32* %"counter"
  %".12" = icmp slt i32 %".11", 1000000
  br i1 %".12", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        a++;-        break;-        counter++;-    }
  ; C Syntax: a++;
  ; C Syntax: a++
  %".17" = load i32, i32* %"a"
  %".18" = add i32 %".17", 1
  store i32 %".18", i32* %"a"
  ; C Syntax: break;
  br label %"w_after"
w_after:
  ; C Syntax: printf("%d", (a==1) & (counter==0));
  ; C Syntax: printf("%d", (a==1) & (counter==0))
  %".24" = bitcast [3 x i8]* @"e8a4462a-75e6-45d6-9fdf-b0501a844541" to i8*
  ; C Syntax: a==1
  %".26" = load i32, i32* %"a"
  %".27" = icmp eq i32 %".26", 1
  ; C Syntax: counter==0
  %".29" = load i32, i32* %"counter"
  %".30" = icmp eq i32 %".29", 0
  %".31" = and i1 %".27", %".30"
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".24", i1 %".31")
  ret i32 0
}

@"e8a4462a-75e6-45d6-9fdf-b0501a844541" = constant [3 x i8] c"%d\00"