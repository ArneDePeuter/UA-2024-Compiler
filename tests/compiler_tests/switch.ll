; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int x = 3;
  %"x" = alloca i32
  ; C Syntax: 3
  store i32 3, i32* %"x"
  ; C Syntax: switch (x) {-        case 1:-            printf("%d", x);-            break;-        case 2:-            printf("%d", x);-            break;-        default:-            printf("%d", x);-    }
  ; C Syntax: x
  %".7" = load i32, i32* %"x"
  ; C Syntax: 1
  %".9" = icmp eq i32 %".7", 1
  br i1 %".9", label %"entry.if", label %"entry.else"
entry.if:
  ; C Syntax: printf("%d", x);
  ; C Syntax: printf("%d", x)
  %".13" = bitcast [3 x i8]* @"ac1082f3-0a15-4760-b4ff-34301dc433dc" to i8*
  %".14" = load i32, i32* %"x"
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %".14")
  br label %"entry.endif"
entry.else:
  ; C Syntax: printf("%d", x);
  ; C Syntax: printf("%d", x)
  %".19" = bitcast [3 x i8]* @"6e440883-8043-40ab-835b-4f5327f0e5ad" to i8*
  %".20" = load i32, i32* %"x"
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".20")
  br label %"entry.endif"
entry.endif:
  ret i32 0
}

@"ac1082f3-0a15-4760-b4ff-34301dc433dc" = constant [3 x i8] c"%d\00"
@"6e440883-8043-40ab-835b-4f5327f0e5ad" = constant [3 x i8] c"%d\00"