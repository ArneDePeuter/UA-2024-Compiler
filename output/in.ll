; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: printf("Hello, World!\n");
  ; C Syntax: printf("Hello, World!\n")
  %".4" = bitcast [15 x i8]* @"821d6c02-08fb-4033-8b8a-210658fce294" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  ; C Syntax: printf("WE ARE THE BEST\n");
  ; C Syntax: printf("WE ARE THE BEST\n")
  %".8" = bitcast [17 x i8]* @"0bda8886-4c18-4c13-b938-e2b8d076bf9c" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8")
  ; C Syntax: printf("WELCOME TO OUR COMPILER\n");
  ; C Syntax: printf("WELCOME TO OUR COMPILER\n")
  %".12" = bitcast [25 x i8]* @"c6d2f2ac-ed21-4713-aa64-823adb224052" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"821d6c02-08fb-4033-8b8a-210658fce294" = constant [15 x i8] c"Hello, World!\0a\00"
@"0bda8886-4c18-4c13-b938-e2b8d076bf9c" = constant [17 x i8] c"WE ARE THE BEST\0a\00"
@"c6d2f2ac-ed21-4713-aa64-823adb224052" = constant [25 x i8] c"WELCOME TO OUR COMPILER\0a\00"