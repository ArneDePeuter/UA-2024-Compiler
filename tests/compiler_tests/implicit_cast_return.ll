; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"add"(i32 %".1", i32 %".2")
{
entry:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"b" = alloca i32
  store i32 %".2", i32* %"b"
  ; C Syntax: return a + b;
  ; C Syntax: a + b
  %".8" = load i32, i32* %"a"
  %".9" = load i32, i32* %"b"
  %".10" = add i32 %".8", %".9"
  ret i32 %".10"
}

define i32 @"main"()
{
entry:
  ; C Syntax: int b = 'c';
  %"b" = alloca i32
  ; C Syntax: 'c'
  %".4" = zext i8 99 to i32
  store i32 %".4", i32* %"b"
  ; C Syntax: int c = 2;
  %"c" = alloca i32
  ; C Syntax: 2
  store i32 2, i32* %"c"
  ; C Syntax: char d = add(b, c);
  %"d" = alloca i8
  ; C Syntax: add(b, c)
  %".11" = load i32, i32* %"b"
  %".12" = load i32, i32* %"c"
  %".13" = call i32 @"add"(i32 %".11", i32 %".12")
  %".14" = trunc i32 %".13" to i8
  store i8 %".14", i8* %"d"
  ; C Syntax: printf("%c", d);
  ; C Syntax: printf("%c", d)
  %".18" = bitcast [3 x i8]* @"f50558ac-00f4-437b-b099-c05b966175d8" to i8*
  %".19" = load i8, i8* %"d"
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".18", i8 %".19")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"f50558ac-00f4-437b-b099-c05b966175d8" = constant [3 x i8] c"%c\00"