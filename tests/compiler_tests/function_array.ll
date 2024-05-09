; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define void @"print_array"([5 x i32] %".1")
{
entry:
  %"arr" = alloca [5 x i32]
  store [5 x i32] %".1", [5 x i32]* %"arr"
  ; C Syntax: for (int i = 0; i < 5; i++) {-        printf("%d", arr[i]);-    }
  ; C Syntax: int i = 0;
  %"i" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"i"
  br label %"w_condition"
w_condition:
  ; C Syntax: i < 5;
  %".10" = load i32, i32* %"i"
  %".11" = icmp slt i32 %".10", 5
  br i1 %".11", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        printf("%d", arr[i]);-    }
  ; C Syntax: printf("%d", arr[i]);
  ; C Syntax: printf("%d", arr[i])
  %".16" = bitcast [3 x i8]* @"b26f1c29-99ea-4b8a-b6b9-4e75db395d80" to i8*
  %".17" = load [5 x i32], [5 x i32]* %"arr"
  %".18" = load i32, i32* %"i"
  %".19" = getelementptr [5 x i32], [5 x i32]* %"arr", i32 0, i32 %".18"
  %".20" = load i32, i32* %".19"
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %".20")
  ; C Syntax: i++
  ; C Syntax: i++
  %".24" = load i32, i32* %"i"
  %".25" = add i32 %".24", 1
  store i32 %".25", i32* %"i"
  br label %"w_condition"
w_after:
  ret void
}

@"b26f1c29-99ea-4b8a-b6b9-4e75db395d80" = constant [3 x i8] c"%d\00"
define i32 @"main"()
{
entry:
  ; C Syntax: int numbers[5] = {1, 2, 3, 4, 5};
  %"numbers" = alloca [5 x i32]
  ; C Syntax: {1, 2, 3, 4, 5}
  ; C Syntax: 1
  ; C Syntax: 2
  ; C Syntax: 3
  ; C Syntax: 4
  ; C Syntax: 5
  store [5 x i32] [i32 1, i32 2, i32 3, i32 4, i32 5], [5 x i32]* %"numbers"
  ; C Syntax: print_array(numbers);
  ; C Syntax: print_array(numbers)
  %".12" = load [5 x i32], [5 x i32]* %"numbers"
  call void @"print_array"([5 x i32] %".12")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
