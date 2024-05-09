; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int marks = 85;
  %"marks" = alloca i32
  ; C Syntax: 85
  store i32 85, i32* %"marks"
  ; C Syntax: if (marks > 90) {-        printf("%d", 10);-    } else if (marks > 80) {-        printf("%d", 8);-    } else if (marks > 70) {-        printf("%d", 7);-    } else if (marks > 60) {-        printf("%d", 6);-    } else {-        printf("%d", 0);-    }
  ; C Syntax: marks > 90
  %".7" = load i32, i32* %"marks"
  %".8" = icmp sgt i32 %".7", 90
  br i1 %".8", label %"entry.if", label %"entry.else"
entry.if:
  ; C Syntax: printf("%d", 10);
  ; C Syntax: printf("%d", 10)
  %".12" = bitcast [3 x i8]* @"711aefcb-fe20-4417-b58a-3ea5aecfd0b5" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 10)
  br label %"entry.endif"
entry.else:
  ; C Syntax: printf("%d", 8);
  ; C Syntax: printf("%d", 8)
  %".17" = bitcast [3 x i8]* @"644f3d3d-abe0-4a1c-b39d-47d3a1489194" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 8)
  br label %"entry.endif"
entry.endif:
  ret i32 0
}

@"711aefcb-fe20-4417-b58a-3ea5aecfd0b5" = constant [3 x i8] c"%d\00"
@"644f3d3d-abe0-4a1c-b39d-47d3a1489194" = constant [3 x i8] c"%d\00"