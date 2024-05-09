; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

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
  %".10" = load i32, i32* %"some_value"
  %".11" = load i32, i32* %"val"
  %".12" = and i32 %".10", %".11"
  store i32 %".12", i32* %"another_value"
  ; C Syntax: int x = 1;
  %"x" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"x"
  ; C Syntax: while (x < 10) {-        int result = mul(x, 2);--        if (x > 5) {-            result = mul(result, x);-        }--        printf("%d", result); // show the result--        x = x + 1;-    }
  br label %"w_condition"
w_condition:
  ; C Syntax: x < 10
  %".20" = load i32, i32* %"x"
  %".21" = icmp slt i32 %".20", 10
  br i1 %".21", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        int result = mul(x, 2);--        if (x > 5) {-            result = mul(result, x);-        }--        printf("%d", result); // show the result--        x = x + 1;-    }
  ; C Syntax: int result = mul(x, 2);
  %"result" = alloca i32
  ; C Syntax: mul(x, 2)
  %".26" = load i32, i32* %"x"
  %".27" = call i32 @"mul"(i32 %".26", i32 2)
  store i32 %".27", i32* %"result"
  ; C Syntax: if (x > 5) {-            result = mul(result, x);-        }
  ; C Syntax: x > 5
  %".31" = load i32, i32* %"x"
  %".32" = icmp sgt i32 %".31", 5
  br i1 %".32", label %"w_body.if", label %"w_body.endif"
w_after:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
w_body.if:
  ; C Syntax: result = mul(result, x);
  ; C Syntax: result
  %".36" = load i32, i32* %"result"
  ; C Syntax: mul(result, x)
  %".38" = load i32, i32* %"result"
  %".39" = load i32, i32* %"x"
  %".40" = call i32 @"mul"(i32 %".38", i32 %".39")
  store i32 %".40", i32* %"result"
  br label %"w_body.endif"
w_body.endif:
  ; C Syntax: printf("%d", result);
  ; C Syntax: printf("%d", result)
  %".45" = bitcast [3 x i8]* @"cb235b18-5123-4676-9970-ab53e5d65a80" to i8*
  %".46" = load i32, i32* %"result"
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".45", i32 %".46")
  ; C Syntax: x = x + 1;
  ; C Syntax: x
  %".50" = load i32, i32* %"x"
  ; C Syntax: x + 1
  %".52" = load i32, i32* %"x"
  %".53" = add i32 %".52", 1
  store i32 %".53", i32* %"x"
  br label %"w_condition"
}

@"cb235b18-5123-4676-9970-ab53e5d65a80" = constant [3 x i8] c"%d\00"