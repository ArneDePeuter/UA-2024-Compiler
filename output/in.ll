; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: printf("%s\n", "Hello, World!");
  ; C Syntax: printf("%s\n", "Hello, World!")
  %".4" = bitcast [4 x i8]* @"39b52278-a470-48a0-bf3a-3496042f6294" to i8*
  ; C Syntax: "Hello, World!"
  %"temp_str" = alloca [14 x i8]
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"temp_str"
  %".7" = getelementptr [14 x i8], [14 x i8]* %"temp_str", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".4", i8* %".7")
  ; C Syntax: printf("%s\n", "Hello, World!");
  ; C Syntax: printf("%s\n", "Hello, World!")
  %".11" = bitcast [4 x i8]* @"dab47243-0a0f-4368-956f-72fd48c763ba" to i8*
  ; C Syntax: "Hello, World!"
  %"temp_str.1" = alloca [14 x i8]
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"temp_str.1"
  %".14" = getelementptr [14 x i8], [14 x i8]* %"temp_str.1", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".11", i8* %".14")
  ; C Syntax: printf("%s\n", "Hello, World!");
  ; C Syntax: printf("%s\n", "Hello, World!")
  %".18" = bitcast [4 x i8]* @"5a34170a-e866-46fc-8685-6ac1c228bb16" to i8*
  ; C Syntax: "Hello, World!"
  %"temp_str.2" = alloca [14 x i8]
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"temp_str.2"
  %".21" = getelementptr [14 x i8], [14 x i8]* %"temp_str.2", i32 0, i32 0
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".18", i8* %".21")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"39b52278-a470-48a0-bf3a-3496042f6294" = constant [4 x i8] c"%s\0a\00"
@"dab47243-0a0f-4368-956f-72fd48c763ba" = constant [4 x i8] c"%s\0a\00"
@"5a34170a-e866-46fc-8685-6ac1c228bb16" = constant [4 x i8] c"%s\0a\00"