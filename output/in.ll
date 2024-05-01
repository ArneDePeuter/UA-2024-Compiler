; ModuleID = ""

%"struct.Inner" = type {i32}
%"struct.Outer" = type {%"struct.Inner"*}
declare i32 @"printf"(i8* %".1", ...)

define void @"modifyInner"(%"struct.Outer"* %".1")
{
entry:
  %"outer" = alloca %"struct.Outer"*
  store %"struct.Outer"* %".1", %"struct.Outer"** %"outer"
  ; C Syntax: if (outer != 0) {-        if (outer->inner_ptr != 0) {-            outer->inner_ptr->value = 42;-        }-    }
  ; C Syntax: outer != 0
  %".6" = load %"struct.Outer"*, %"struct.Outer"** %"outer"
  %".7" = ptrtoint %"struct.Outer"* %".6" to i32
  %".8" = icmp ne i32 %".7", 0
  br i1 %".8", label %"entry.if", label %"entry.endif"
entry.if:
  ; C Syntax: if (outer->inner_ptr != 0) {-            outer->inner_ptr->value = 42;-        }
  ; C Syntax: outer->inner_ptr != 0
  %".12" = load %"struct.Outer"*, %"struct.Outer"** %"outer"
  %".13" = load %"struct.Outer", %"struct.Outer"* %".12"
  %".14" = getelementptr %"struct.Outer", %"struct.Outer"* %".12", i32 0, i32 0
  %".15" = load %"struct.Inner"*, %"struct.Inner"** %".14"
  %".16" = ptrtoint %"struct.Inner"* %".15" to i32
  %".17" = icmp ne i32 %".16", 0
  br i1 %".17", label %"entry.if.if", label %"entry.if.endif"
entry.endif:
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
  br label %"entry.if.endif"
entry.if.endif:
  br label %"entry.endif"
}

define i32 @"main"()
{
entry:
  ; C Syntax: struct Inner inner = {10};
  %"inner" = alloca %"struct.Inner"
  ; C Syntax: {10}
  ; C Syntax: 10
  %".5" = insertvalue %"struct.Inner" zeroinitializer, i32 10, 0
  store %"struct.Inner" %".5", %"struct.Inner"* %"inner"
  ; C Syntax: struct Outer outer = {&inner};
  %"outer" = alloca %"struct.Outer"
  ; C Syntax: {&inner}
  ; C Syntax: &inner
  %".10" = load %"struct.Inner", %"struct.Inner"* %"inner"
  %".11" = insertvalue %"struct.Outer" zeroinitializer, %"struct.Inner"* %"inner", 0
  store %"struct.Outer" %".11", %"struct.Outer"* %"outer"
  ; C Syntax: printf("%d", outer.inner_ptr->value);
  ; C Syntax: printf("%d", outer.inner_ptr->value)
  ; C Syntax: outer.inner_ptr->value
  %".16" = load %"struct.Outer", %"struct.Outer"* %"outer"
  %".17" = getelementptr %"struct.Outer", %"struct.Outer"* %"outer", i32 0, i32 0
  %".18" = load %"struct.Inner"*, %"struct.Inner"** %".17"
  %".19" = load %"struct.Inner", %"struct.Inner"* %".18"
  %".20" = getelementptr %"struct.Inner", %"struct.Inner"* %".18", i32 0, i32 0
  %".21" = load i32, i32* %".20"
  %".22" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_23_4" to i8*), i32 %".21")
  ; C Syntax: modifyInner(&outer);
  ; C Syntax: modifyInner(&outer)
  ; C Syntax: &outer
  %".26" = load %"struct.Outer", %"struct.Outer"* %"outer"
  call void @"modifyInner"(%"struct.Outer"* %"outer")
  ; C Syntax: printf("%d", outer.inner_ptr->value);
  ; C Syntax: printf("%d", outer.inner_ptr->value)
  ; C Syntax: outer.inner_ptr->value
  %".31" = load %"struct.Outer", %"struct.Outer"* %"outer"
  %".32" = getelementptr %"struct.Outer", %"struct.Outer"* %"outer", i32 0, i32 0
  %".33" = load %"struct.Inner"*, %"struct.Inner"** %".32"
  %".34" = load %"struct.Inner", %"struct.Inner"* %".33"
  %".35" = getelementptr %"struct.Inner", %"struct.Inner"* %".33", i32 0, i32 0
  %".36" = load i32, i32* %".35"
  %".37" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_25_4" to i8*), i32 %".36")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"printf_format_23_4" = internal constant [3 x i8] c"%d\00"
@"printf_format_25_4" = internal constant [3 x i8] c"%d\00"