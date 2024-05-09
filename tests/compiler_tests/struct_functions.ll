; ModuleID = ""

%"struct.Inner" = type {i32}
%"struct.Outer" = type {%"struct.Inner"*}
declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

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
  %".15" = bitcast [3 x i8]* @"5c6eb3f2-058f-4b4b-908f-94d493b65f44" to i8*
  %".16" = load %"struct.Outer", %"struct.Outer"* %"outer"
  %".17" = getelementptr %"struct.Outer", %"struct.Outer"* %"outer", i32 0, i32 0
  %".18" = load %"struct.Inner"*, %"struct.Inner"** %".17"
  %".19" = load %"struct.Inner", %"struct.Inner"* %".18"
  %".20" = getelementptr %"struct.Inner", %"struct.Inner"* %".18", i32 0, i32 0
  %".21" = load i32, i32* %".20"
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".21")
  ; C Syntax: modifyInner(&outer);
  ; C Syntax: modifyInner(&outer)
  %".25" = load %"struct.Outer", %"struct.Outer"* %"outer"
  call void @"modifyInner"(%"struct.Outer"* %"outer")
  ; C Syntax: printf("%d", outer.inner_ptr->value);
  ; C Syntax: printf("%d", outer.inner_ptr->value)
  %".29" = bitcast [3 x i8]* @"f2702e8f-b5e5-4035-8b99-a07c2aedcea4" to i8*
  %".30" = load %"struct.Outer", %"struct.Outer"* %"outer"
  %".31" = getelementptr %"struct.Outer", %"struct.Outer"* %"outer", i32 0, i32 0
  %".32" = load %"struct.Inner"*, %"struct.Inner"** %".31"
  %".33" = load %"struct.Inner", %"struct.Inner"* %".32"
  %".34" = getelementptr %"struct.Inner", %"struct.Inner"* %".32", i32 0, i32 0
  %".35" = load i32, i32* %".34"
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".29", i32 %".35")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"5c6eb3f2-058f-4b4b-908f-94d493b65f44" = constant [3 x i8] c"%d\00"
@"f2702e8f-b5e5-4035-8b99-a07c2aedcea4" = constant [3 x i8] c"%d\00"