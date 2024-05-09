; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char str[] = "Hello, World!";
  %"str" = alloca [14 x i8]
  ; C Syntax: "Hello, World!"
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"str"
  ; C Syntax: char *ptr = str;
  %"ptr" = alloca i8*
  ; C Syntax: str
  %".7" = load [14 x i8], [14 x i8]* %"str"
  %".8" = getelementptr [14 x i8], [14 x i8]* %"str", i32 0, i32 0
  store i8* %".8", i8** %"ptr"
  ; C Syntax: printf("%s", ptr);
  ; C Syntax: printf("%s", ptr)
  %".12" = bitcast [3 x i8]* @"3b1c3219-a120-4c34-a053-9b9872ae489c" to i8*
  %".13" = load i8*, i8** %"ptr"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".12", i8* %".13")
  ; C Syntax: ptr[7] = 'P';
  ; C Syntax: ptr[7]
  %".17" = load i8*, i8** %"ptr"
  %".18" = getelementptr i8, i8* %".17", i32 7
  %".19" = load i8, i8* %".18"
  ; C Syntax: 'P'
  store i8 80, i8* %".18"
  ; C Syntax: printf("%s", ptr);
  ; C Syntax: printf("%s", ptr)
  %".24" = bitcast [3 x i8]* @"2d9b5820-25d5-4fb7-bc2f-8b3d787107f7" to i8*
  %".25" = load i8*, i8** %"ptr"
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".24", i8* %".25")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"3b1c3219-a120-4c34-a053-9b9872ae489c" = constant [3 x i8] c"%s\00"
@"2d9b5820-25d5-4fb7-bc2f-8b3d787107f7" = constant [3 x i8] c"%s\00"