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
  %".25" = call i32 @"mul"(i32 1, i32 2)
  store i32 %".25", i32* %"result"
  ; C Syntax: if (x > 5) {-            result = mul(result, x);-        }
  ; C Syntax: x > 5
  %".29" = load i32, i32* %"x"
  %".30" = icmp sgt i32 %".29", 5
  br i1 %".30", label %"w_body.if", label %"w_body.endif"
w_after:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
w_body.if:
  ; C Syntax: result = mul(result, x);
  ; C Syntax: result
  %".34" = load i32, i32* %"result"
  ; C Syntax: mul(result, x)
  %".36" = load i32, i32* %"result"
  %".37" = load i32, i32* %"x"
  %".38" = call i32 @"mul"(i32 %".36", i32 %".37")
  store i32 %".38", i32* %"result"
  br label %"w_body.endif"
w_body.endif:
  ; C Syntax: printf("%d", result);
  ; C Syntax: printf("%d", result)
  %".43" = bitcast [3 x i8]* @"48203111-699e-4733-86a1-01d54a239b78" to i8*
  %".44" = load i32, i32* %"result"
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".43", i32 %".44")
  ; // show the result
  ;
  ; C Syntax: x = x + 1;
  ; C Syntax: x
  %".50" = load i32, i32* %"x"
  ; C Syntax: x + 1
  %".52" = load i32, i32* %"x"
  %".53" = add i32 %".52", 1
  store i32 %".53", i32* %"x"
  br label %"w_condition"
}

@"48203111-699e-4733-86a1-01d54a239b78" = constant [3 x i8] c"%d\00"