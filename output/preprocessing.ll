; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"mul"(i32 %".1", i32 %".2")
{
entry:
  %"x" = alloca i32
  store i32 %".1", i32* %"x"
  %"y" = alloca i32
  store i32 %".2", i32* %"y"
  ; C Syntax: return x * y;
  ; C Syntax: x * y
  %".8" = load i32, i32* %"x"
  %".9" = load i32, i32* %"y"
  %".10" = mul i32 %".8", %".9"
  ret i32 %".10"
}

define i32 @"main"()
{
entry:
  ; C Syntax: int val = 0;
  %"val" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"val"
  ; C Syntax: int some_value = 1;
  %"some_value" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"some_value"
  ; C Syntax: int another_value = some_value && val;
  %"another_value" = alloca i32
  ; C Syntax: some_value && val
  ; C Syntax: 1
  %".11" = load i32, i32* %"val"
  %".12" = and i32 1, %".11"
  store i32 %".12", i32* %"another_value"
  ; C Syntax: int x = 1;
  %"x" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"x"
  ; C Syntax: while (x < 10) {-        int result = mul(x, 2);--        if (x > 5) {-            result = mul(result, x);-        }--        printf("%d", result); // show the result--        x = x + 1;-    }
  br label %"w_condition"
w_condition:
  %".19" = icmp ne i32 1, 0
  br i1 %".19", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        int result = mul(x, 2);--        if (x > 5) {-            result = mul(result, x);-        }--        printf("%d", result); // show the result--        x = x + 1;-    }
  ; C Syntax: int result = mul(x, 2);
  %"result" = alloca i32
  ; C Syntax: mul(x, 2)
  ; C Syntax: 1
  ; C Syntax: 2
  %".26" = call i32 @"mul"(i32 1, i32 2)
  store i32 %".26", i32* %"result"
  ; C Syntax: if (x > 5) {-            result = mul(result, x);-        }
  ; C Syntax: x > 5
  %".30" = load i32, i32* %"x"
  %".31" = icmp sgt i32 %".30", 5
  br i1 %".31", label %"w_body.if", label %"w_body.endif"
w_after:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
w_body.if:
  ; C Syntax: result = mul(result, x);
  ; C Syntax: result
  %".35" = load i32, i32* %"result"
  ; C Syntax: mul(result, x)
  ; C Syntax: result
  %".38" = load i32, i32* %"result"
  ; C Syntax: x
  %".40" = load i32, i32* %"x"
  %".41" = call i32 @"mul"(i32 %".38", i32 %".40")
  store i32 %".41", i32* %"result"
  br label %"w_body.endif"
w_body.endif:
  ; C Syntax: printf("%d", result);
  ; C Syntax: printf("%d", result)
  ; C Syntax: result
  %".47" = load i32, i32* %"result"
  %".48" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_23_8" to i8*), i32 %".47")
  ; C Syntax: // show the result-
  ; // show the result
  ; C Syntax: x = x + 1;
  ; C Syntax: x
  %".53" = load i32, i32* %"x"
  ; C Syntax: x + 1
  %".55" = load i32, i32* %"x"
  %".56" = add i32 %".55", 1
  store i32 %".56", i32* %"x"
}

@"printf_format_23_8" = internal constant [3 x i8] c"%d\00"