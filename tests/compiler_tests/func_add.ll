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
  ; C Syntax: int b = 1;
  %"b" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"b"
  ; C Syntax: int c = 2;
  %"c" = alloca i32
  ; C Syntax: 2
  store i32 2, i32* %"c"
  ; C Syntax: int d = add(b, c);
  %"d" = alloca i32
  ; C Syntax: add(b, c)
  %".10" = load i32, i32* %"b"
  %".11" = load i32, i32* %"c"
  %".12" = call i32 @"add"(i32 %".10", i32 %".11")
  store i32 %".12", i32* %"d"
  ; C Syntax: printf("%d", d);
  ; C Syntax: printf("%d", d)
  %".16" = bitcast [3 x i8]* @"685bba5e-4f83-406c-becd-acc9fe53afe3" to i8*
  %".17" = load i32, i32* %"d"
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %".17")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"685bba5e-4f83-406c-becd-acc9fe53afe3" = constant [3 x i8] c"%d\00"