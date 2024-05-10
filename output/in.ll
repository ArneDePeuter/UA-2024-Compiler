; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char str[] = "This is a string\n";
  %"str" = alloca [18 x i8]
  ; C Syntax: "This is a string\n"
  store [18 x i8] [i8 84, i8 104, i8 105, i8 115, i8 32, i8 105, i8 115, i8 32, i8 97, i8 32, i8 115, i8 116, i8 114, i8 105, i8 110, i8 103, i8 10, i8 0], [18 x i8]* %"str"
  ; C Syntax: printf("%s", str);
  ; C Syntax: printf("%s", str)
  %".7" = bitcast [3 x i8]* @"cf8f1f62-aa8b-4700-b8fc-ddba529b09ab" to i8*
  %".8" = load [18 x i8], [18 x i8]* %"str"
  %"temp_str" = alloca [18 x i8]
  store [18 x i8] %".8", [18 x i8]* %"temp_str"
  %".10" = getelementptr [18 x i8], [18 x i8]* %"temp_str", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".7", i8* %".10")
  ; C Syntax: printf("%s", "This is a string\n");
  ; C Syntax: printf("%s", "This is a string\n")
  %".14" = bitcast [3 x i8]* @"36285d33-8240-40bb-83ad-3a8e202c61b5" to i8*
  %"temp_str.1" = alloca [18 x i8]
  store [18 x i8] [i8 84, i8 104, i8 105, i8 115, i8 32, i8 105, i8 115, i8 32, i8 97, i8 32, i8 115, i8 116, i8 114, i8 105, i8 110, i8 103, i8 10, i8 0], [18 x i8]* %"temp_str.1"
  %".16" = getelementptr [18 x i8], [18 x i8]* %"temp_str.1", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".14", i8* %".16")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"cf8f1f62-aa8b-4700-b8fc-ddba529b09ab" = constant [3 x i8] c"%s\00"
@"36285d33-8240-40bb-83ad-3a8e202c61b5" = constant [3 x i8] c"%s\00"