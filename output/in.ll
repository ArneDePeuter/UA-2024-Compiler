; ModuleID = ""

%"struct.Inner" = type {i32}
%"struct.Outer" = type {%"struct.Inner"*}
declare i32 @"printf"(i8* %".1", ...)

define void @"modifyInner"(%"struct.Outer"* %".1")
{
entry:
  %"outer" = alloca %"struct.Outer"*
  store %"struct.Outer"* %".1", %"struct.Outer"** %"outer"
  ; C Syntax: if (outer != 0) {-        if (outer->inner_ptr != 0) {-            outer->inner_ptr->value = 42;-            return;-        }-    }
  ; C Syntax: outer != 0
  %".6" = load %"struct.Outer"*, %"struct.Outer"** %"outer"
  %".7" = ptrtoint %"struct.Outer"* %".6" to i32
  %".8" = icmp ne i32 %".7", 0
  br i1 %".8", label %"entry.if", label %"entry.endif"
entry.if:
  ; C Syntax: if (outer->inner_ptr != 0) {-            outer->inner_ptr->value = 42;-            return;-        }
  ; C Syntax: outer->inner_ptr != 0
  %".12" = load %"struct.Outer"*, %"struct.Outer"** %"outer"
  %".13" = load %"struct.Outer", %"struct.Outer"* %".12"
  %".14" = getelementptr %"struct.Outer", %"struct.Outer"* %".12", i32 0, i32 0
  %".15" = load %"struct.Inner"*, %"struct.Inner"** %".14"
  %".16" = ptrtoint %"struct.Inner"* %".15" to i32
  %".17" = icmp ne i32 %".16", 0
  br i1 %".17", label %"entry.if.if", label %"entry.if.endif"
entry.endif:
  ; C Syntax: printf("%d", 0);
  ; C Syntax: printf("%d", 0)
  ; C Syntax: 0
  %".36" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_17_4" to i8*), i32 0)
  ret void
entry.if.if:
  ; C Syntax: outer->inner_ptr->value = 42;
  ; C Syntax: outer->inner_ptr->value
  %".21" = load %"struct.Outer"*, %"struct.Outer"** %"outer"
  %".22" = load %"struct.Outer", %"struct.Outer"* %".21"
  %".23" = getelementptr %"struct.Outer", %"struct.Outer"* %".21", i32 0, i32 0
  %".24" = load %"struct.Inner"*, %"struct.Inner"** %".23"
  %".25" = load %"struct.Inner", %"struct.Inner"* %".24"
  %".26" = getelementptr %"struct.Inner", %"struct.Inner"* %".24", i32 0, i32 0
  %".27" = load i32, i32* %".26"
  ; C Syntax: 42
  store i32 42, i32* %".26"
  ; C Syntax: return;
  ret void
entry.if.endif:
  br label %"entry.endif"
}

@"printf_format_17_4" = internal constant [3 x i8] c"%d\00"
define i32 @"main"()
{
entry:
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
  ; C Syntax: a
  %".43" = load i32, i32* %"a"
  %".44" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_13_4" to i8*), i32 %".43")
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
