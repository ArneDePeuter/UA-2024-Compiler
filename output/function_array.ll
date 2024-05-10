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
  %".9" = icmp ne i32 1, 0
  br i1 %".9", label %"w_body", label %"w_after"
w_body:
  ; C Syntax: {-        printf("%d", arr[i]);-    }
  ; C Syntax: printf("%d", arr[i]);
  ; C Syntax: printf("%d", arr[i])
  %".14" = bitcast [3 x i8]* @"9a4425c6-cd21-4ab8-ad11-7f4a0c4b4ef8" to i8*
  %".15" = load [5 x i32], [5 x i32]* %"arr"
  ; C Syntax: 0
  %".17" = getelementptr [5 x i32], [5 x i32]* %"arr", i32 0, i32 0
  %".18" = load i32, i32* %".17"
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".18")
  ; C Syntax: i++
  ; C Syntax: i++
  %".22" = load i32, i32* %"i"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* %"i"
  br label %"w_condition"
w_after:
  ret void
}

@"9a4425c6-cd21-4ab8-ad11-7f4a0c4b4ef8" = constant [3 x i8] c"%d\00"
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
  ; // Example array
  ;
  ; C Syntax: print_array(numbers);
  ; C Syntax: print_array(numbers)
  %".14" = load [5 x i32], [5 x i32]* %"numbers"
  call void @"print_array"([5 x i32] %".14")
  ; // Call the print function
  ;
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
