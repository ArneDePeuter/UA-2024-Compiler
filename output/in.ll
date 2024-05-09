; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int switch_x = 5;
  %"switch_x" = alloca i32
  ; C Syntax: 5
  store i32 5, i32* %"switch_x"
  ; C Syntax: switch (switch_x) {-        case 1:-            printf("switch_x is 1\n");-            break;-        case 2:-            printf("switch_x is 2\n");-            break;-        case 3:-            printf("switch_x is 3\n");-            break;-        default:-            printf("switch_x is not 1, 2, or 3\n");-    }
  %".6" = icmp ne i32 0, 0
  br i1 %".6", label %"entry.if", label %"entry.else"
entry.if:
  ; C Syntax: printf("switch_x is 1\n");
  ; C Syntax: printf("switch_x is 1\n")
  %".10" = bitcast [15 x i8]* @"86beb7d4-6560-41ed-9f1b-a27278707a1a" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10")
  br label %"entry.endif"
entry.else:
  ; C Syntax: 5
  ; C Syntax: 2
  %".15" = icmp eq i32 5, 2
  br i1 %".15", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
entry.else.if:
  ; C Syntax: printf("switch_x is 2\n");
  ; C Syntax: printf("switch_x is 2\n")
  %".19" = bitcast [15 x i8]* @"aaf10169-2230-4061-9e4b-daafd7ea87d3" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19")
  br label %"entry.else.endif"
entry.else.else:
  ; C Syntax: 5
  ; C Syntax: 3
  %".24" = icmp eq i32 5, 3
  br i1 %".24", label %"entry.else.else.if", label %"entry.else.else.else"
entry.else.endif:
  br label %"entry.endif"
entry.else.else.if:
  ; C Syntax: printf("switch_x is 3\n");
  ; C Syntax: printf("switch_x is 3\n")
  %".28" = bitcast [15 x i8]* @"abe3f914-04a1-4694-8346-bffecd4cdedc" to i8*
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".28")
  br label %"entry.else.else.endif"
entry.else.else.else:
  ; C Syntax: printf("switch_x is not 1, 2, or 3\n");
  ; C Syntax: printf("switch_x is not 1, 2, or 3\n")
  %".33" = bitcast [28 x i8]* @"8c58e1d7-a35c-4104-a78a-bbb5adfb3f29" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33")
  br label %"entry.else.else.endif"
entry.else.else.endif:
  br label %"entry.else.endif"
}

@"86beb7d4-6560-41ed-9f1b-a27278707a1a" = constant [15 x i8] c"switch_x is 1\0a\00"
@"aaf10169-2230-4061-9e4b-daafd7ea87d3" = constant [15 x i8] c"switch_x is 2\0a\00"
@"abe3f914-04a1-4694-8346-bffecd4cdedc" = constant [15 x i8] c"switch_x is 3\0a\00"
@"8c58e1d7-a35c-4104-a78a-bbb5adfb3f29" = constant [28 x i8] c"switch_x is not 1, 2, or 3\0a\00"