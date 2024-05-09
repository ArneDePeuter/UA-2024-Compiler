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
  ; C Syntax: printf("%s", str);
  ; C Syntax: printf("%s", str)
  %".7" = bitcast [3 x i8]* @"b275e679-668b-4e37-b753-c88c92079ff8" to i8*
  %".8" = load [14 x i8], [14 x i8]* %"str"
  %"temp_str" = alloca [14 x i8]
  store [14 x i8] %".8", [14 x i8]* %"temp_str"
  %".10" = getelementptr [14 x i8], [14 x i8]* %"temp_str", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".7", i8* %".10")
  ; C Syntax: str[0] = 'S';
  ; C Syntax: str[0]
  %".14" = load [14 x i8], [14 x i8]* %"str"
  %".15" = getelementptr [14 x i8], [14 x i8]* %"str", i32 0, i32 0
  %".16" = load i8, i8* %".15"
  ; C Syntax: 'S'
  store i8 83, i8* %".15"
  ; C Syntax: printf("%s", str);
  ; C Syntax: printf("%s", str)
  %".21" = bitcast [3 x i8]* @"f21c28a0-fae8-4413-823c-fd5b91ca599b" to i8*
  %".22" = load [14 x i8], [14 x i8]* %"str"
  %"temp_str.1" = alloca [14 x i8]
  store [14 x i8] %".22", [14 x i8]* %"temp_str.1"
  %".24" = getelementptr [14 x i8], [14 x i8]* %"temp_str.1", i32 0, i32 0
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".21", i8* %".24")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"b275e679-668b-4e37-b753-c88c92079ff8" = constant [3 x i8] c"%s\00"
@"f21c28a0-fae8-4413-823c-fd5b91ca599b" = constant [3 x i8] c"%s\00"