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

define i32 @"main"(i32 %".1")
{
entry:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
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
  %".12" = load i32, i32* %"some_value"
  %".13" = load i32, i32* %"val"
  %".14" = and i32 %".12", %".13"
  store i32 %".14", i32* %"another_value"
  ; C Syntax: int x = 1;
  %"x" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"x"
  ; C Syntax: while (x < 10) {-        int result = mul(x, 2);--        if (x > 5) {-            result = mul(result, x);-        }--        printf("%d", result); // show the result--        x = x + 1;-    }
  br label %"w_condition"
w_condition:
  ; C Syntax: x < 10
  %".22" = load i32, i32* %"x"
  %".23" = icmp slt i32 %".22", 10
  br i1 %".23", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        int result = mul(x, 2);--        if (x > 5) {-            result = mul(result, x);-        }--        printf("%d", result); // show the result--        x = x + 1;-    }
  ; C Syntax: int result = mul(x, 2);
  %"result" = alloca i32
  ; C Syntax: mul(x, 2)
  ; C Syntax: x
  %".29" = load i32, i32* %"x"
  ; C Syntax: 2
  %".31" = call i32 @"mul"(i32 %".29", i32 2)
  store i32 %".31", i32* %"result"
  ; C Syntax: if (x > 5) {-            result = mul(result, x);-        }
  ; C Syntax: x > 5
  %".35" = load i32, i32* %"x"
  %".36" = icmp sgt i32 %".35", 5
  br i1 %".36", label %"w_body.if", label %"w_body.endif"
w_after:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
w_body.if:
  ; C Syntax: result = mul(result, x);
  ; C Syntax: result
  %".40" = load i32, i32* %"result"
  ; C Syntax: mul(result, x)
  ; C Syntax: result
  %".43" = load i32, i32* %"result"
  ; C Syntax: x
  %".45" = load i32, i32* %"x"
  %".46" = call i32 @"mul"(i32 %".43", i32 %".45")
  store i32 %".46", i32* %"result"
  br label %"w_body.endif"
w_body.endif:
  ; C Syntax: printf("%d", result);
  ; C Syntax: printf("%d", result)
  ; C Syntax: result
  %".52" = load i32, i32* %"result"
  %".53" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_26_8" to i8*), i32 %".52")
  ; C Syntax: // show the result-
  ; // show the result
  ; C Syntax: x = x + 1;
  ; C Syntax: x
  %".58" = load i32, i32* %"x"
  ; C Syntax: x + 1
  %".60" = load i32, i32* %"x"
  %".61" = add i32 %".60", 1
  store i32 %".61", i32* %"x"
  br label %"w_condition"
}

@"printf_format_26_8" = internal constant [3 x i8] c"%d\00"