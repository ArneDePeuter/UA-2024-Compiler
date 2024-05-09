; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: printf("%s\n", "Hello, World!");
  ; C Syntax: printf("%s\n", "Hello, World!")
  %".4" = bitcast [4 x i8]* @"f2986cbc-b07e-44f2-933e-8e4fa65e3c10" to i8*
  %"temp_str" = alloca [14 x i8]
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"temp_str"
  %".6" = getelementptr [14 x i8], [14 x i8]* %"temp_str", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".4", i8* %".6")
  ; C Syntax: printf("%s\n", "Hello, World!");
  ; C Syntax: printf("%s\n", "Hello, World!")
  %".10" = bitcast [4 x i8]* @"38bf9022-7033-48f7-8652-3793fa34da56" to i8*
  %"temp_str.1" = alloca [14 x i8]
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"temp_str.1"
  %".12" = getelementptr [14 x i8], [14 x i8]* %"temp_str.1", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".10", i8* %".12")
  ; C Syntax: printf("%s\n", "Hello, World!");
  ; C Syntax: printf("%s\n", "Hello, World!")
  %".16" = bitcast [4 x i8]* @"45b0b333-32da-469f-8c11-8b250d417bbe" to i8*
  %"temp_str.2" = alloca [14 x i8]
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"temp_str.2"
  %".18" = getelementptr [14 x i8], [14 x i8]* %"temp_str.2", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".16", i8* %".18")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"f2986cbc-b07e-44f2-933e-8e4fa65e3c10" = constant [4 x i8] c"%s\0a\00"
@"38bf9022-7033-48f7-8652-3793fa34da56" = constant [4 x i8] c"%s\0a\00"
@"45b0b333-32da-469f-8c11-8b250d417bbe" = constant [4 x i8] c"%s\0a\00"