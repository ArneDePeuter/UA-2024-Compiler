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
  ; C Syntax: int d = add(b, c);
  %"d" = alloca i32
  ; C Syntax: add(b, c)
  %".11" = load i32, i32* %"b"
  %".12" = load i32, i32* %"c"
  %".13" = call i32 @"add"(i32 %".11", i32 %".12")
  store i32 %".13", i32* %"d"
  ; C Syntax: printf("%d", d);
  ; C Syntax: printf("%d", d)
  %".17" = bitcast [3 x i8]* @"1ae033d2-bb9f-42db-a3d1-b405ff8574f9" to i8*
  %".18" = load i32, i32* %"d"
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %".18")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"1ae033d2-bb9f-42db-a3d1-b405ff8574f9" = constant [3 x i8] c"%d\00"