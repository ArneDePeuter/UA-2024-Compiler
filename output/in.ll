; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; // switch statements: switch, break, case.
  ;
  ; C Syntax: int switch_x = 5;
  %"switch_x" = alloca i32
  ; C Syntax: 5
  store i32 5, i32* %"switch_x"
  ; C Syntax: switch (switch_x) {-        case 1:-            printf("switch_x is 1\n");-            break;-        case 2:-            printf("switch_x is 2\n");-            break;-        case 3:-            printf("switch_x is 3\n");-            break;-        default:-            printf("switch_x is not 1, 2, or 3\n");-    }
  %".8" = icmp ne i32 0, 0
  br i1 %".8", label %"entry.if", label %"entry.else"
entry.if:
  ; C Syntax: printf("switch_x is 1\n");
  ; C Syntax: printf("switch_x is 1\n")
  %".12" = bitcast [15 x i8]* @"01dbf1fe-a836-4a2e-9c22-aac5e9ff30e4" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12")
  br label %"entry.endif"
entry.else:
  ; C Syntax: 5
  ; C Syntax: 2
  %".17" = icmp eq i32 5, 2
  br i1 %".17", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
entry.else.if:
  ; C Syntax: printf("switch_x is 2\n");
  ; C Syntax: printf("switch_x is 2\n")
  %".21" = bitcast [15 x i8]* @"fa6f040a-a9bb-4594-b83f-51fe1af4a003" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21")
  br label %"entry.else.endif"
entry.else.else:
  ; C Syntax: 5
  ; C Syntax: 3
  %".26" = icmp eq i32 5, 3
  br i1 %".26", label %"entry.else.else.if", label %"entry.else.else.else"
entry.else.endif:
  br label %"entry.endif"
entry.else.else.if:
  ; C Syntax: printf("switch_x is 3\n");
  ; C Syntax: printf("switch_x is 3\n")
  %".30" = bitcast [15 x i8]* @"7f6b458d-9883-449c-902d-00330da15600" to i8*
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30")
  br label %"entry.else.else.endif"
entry.else.else.else:
  ; C Syntax: printf("switch_x is not 1, 2, or 3\n");
  ; C Syntax: printf("switch_x is not 1, 2, or 3\n")
  %".35" = bitcast [28 x i8]* @"31c903a0-4ff5-4416-b92b-ef38dae41709" to i8*
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".35")
  br label %"entry.else.else.endif"
entry.else.else.endif:
  br label %"entry.else.endif"
}

@"01dbf1fe-a836-4a2e-9c22-aac5e9ff30e4" = constant [15 x i8] c"switch_x is 1\0a\00"
@"fa6f040a-a9bb-4594-b83f-51fe1af4a003" = constant [15 x i8] c"switch_x is 2\0a\00"
@"7f6b458d-9883-449c-902d-00330da15600" = constant [15 x i8] c"switch_x is 3\0a\00"
@"31c903a0-4ff5-4416-b92b-ef38dae41709" = constant [28 x i8] c"switch_x is not 1, 2, or 3\0a\00"