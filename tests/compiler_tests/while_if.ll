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
  ; C Syntax: int b = 0;
  %"b" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"b"
  ; C Syntax: while (counter < 1000000) {-        if (counter > 100) {-            b++;-        }-        a++;-        counter++;-    }
  br label %"w_condition"
w_condition:
  ; C Syntax: counter < 1000000
  %".14" = load i32, i32* %"counter"
  %".15" = icmp slt i32 %".14", 1000000
  br i1 %".15", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        if (counter > 100) {-            b++;-        }-        a++;-        counter++;-    }
  ; C Syntax: if (counter > 100) {-            b++;-        }
  ; C Syntax: counter > 100
  %".20" = load i32, i32* %"counter"
  %".21" = icmp sgt i32 %".20", 100
  br i1 %".21", label %"w_body.if", label %"w_body.endif"
w_after:
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".42" = bitcast [3 x i8]* @"e67792db-1bd7-4e6e-8806-0c6504492dec" to i8*
  %".43" = load i32, i32* %"a"
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".42", i32 %".43")
  ; C Syntax: printf("%d", b);
  ; C Syntax: printf("%d", b)
  %".47" = bitcast [3 x i8]* @"b03a0b5a-f784-460e-bc4a-a06caedab12d" to i8*
  %".48" = load i32, i32* %"b"
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".47", i32 %".48")
  ret i32 0
w_body.if:
  ; C Syntax: b++;
  ; C Syntax: b++
  %".25" = load i32, i32* %"b"
  %".26" = add i32 %".25", 1
  store i32 %".26", i32* %"b"
  br label %"w_body.endif"
w_body.endif:
  ; C Syntax: a++;
  ; C Syntax: a++
  %".31" = load i32, i32* %"a"
  %".32" = add i32 %".31", 1
  store i32 %".32", i32* %"a"
  ; C Syntax: counter++;
  ; C Syntax: counter++
  %".36" = load i32, i32* %"counter"
  %".37" = add i32 %".36", 1
  store i32 %".37", i32* %"counter"
  br label %"w_condition"
}

@"e67792db-1bd7-4e6e-8806-0c6504492dec" = constant [3 x i8] c"%d\00"
@"b03a0b5a-f784-460e-bc4a-a06caedab12d" = constant [3 x i8] c"%d\00"