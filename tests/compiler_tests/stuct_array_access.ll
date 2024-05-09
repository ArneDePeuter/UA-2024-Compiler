; ModuleID = ""

%"struct.Test" = type {[5 x i32]}
declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: struct Test test = {{10, 20, 30, 40, '2'}};
  %"test" = alloca %"struct.Test"
  ; C Syntax: {{10, 20, 30, 40, '2'}}
  ; C Syntax: {10, 20, 30, 40, '2'}
  ; C Syntax: 10
  ; C Syntax: 20
  ; C Syntax: 30
  ; C Syntax: 40
  %".9" = insertvalue %"struct.Test" zeroinitializer, [5 x i32] [i32 10, i32 20, i32 30, i32 40, i32 50], 0
  store %"struct.Test" %".9", %"struct.Test"* %"test"
  ; C Syntax: for (int i = 0; i < 5; i++ ) {-        printf("%d", test.array[i]);-    }
  ; C Syntax: int i = 0;
  %"i" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"i"
  br label %"w_condition"
w_condition:
  ; C Syntax: i < 5;
  %".17" = load i32, i32* %"i"
  %".18" = icmp slt i32 %".17", 5
  br i1 %".18", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        printf("%d", test.array[i]);-    }
  ; C Syntax: printf("%d", test.array[i]);
  ; C Syntax: printf("%d", test.array[i])
  %".23" = bitcast [3 x i8]* @"92bb0096-f61c-4d8d-8e83-6ecaa82539c8" to i8*
  %".24" = load %"struct.Test", %"struct.Test"* %"test"
  %".25" = getelementptr %"struct.Test", %"struct.Test"* %"test", i32 0, i32 0
  %".26" = load [5 x i32], [5 x i32]* %".25"
  %".27" = load i32, i32* %"i"
  %".28" = getelementptr [5 x i32], [5 x i32]* %".25", i32 0, i32 %".27"
  %".29" = load i32, i32* %".28"
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %".29")
  ; C Syntax: i++
  ; C Syntax: i++
  %".33" = load i32, i32* %"i"
  %".34" = add i32 %".33", 1
  store i32 %".34", i32* %"i"
  br label %"w_condition"
w_after:
  ret i32 0
}

@"92bb0096-f61c-4d8d-8e83-6ecaa82539c8" = constant [3 x i8] c"%d\00"