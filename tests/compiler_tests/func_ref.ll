; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"make_ptr_null"(i32* %".1")
{
entry:
  %"ptr" = alloca i32*
  store i32* %".1", i32** %"ptr"
  ; C Syntax: *ptr = 0;
  ; C Syntax: *ptr
  %".6" = load i32*, i32** %"ptr"
  %".7" = load i32, i32* %".6"
  ; C Syntax: 0
  store i32 0, i32* %".6"
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

define i32 @"main"()
{
entry:
  ; C Syntax: int a = 1;
  %"a" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"a"
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".7" = bitcast [3 x i8]* @"11358178-a650-4cbd-b970-1cdd3bdc8a49" to i8*
  %".8" = load i32, i32* %"a"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".8")
  ; C Syntax: make_ptr_null(&a);
  ; C Syntax: make_ptr_null(&a)
  %".12" = load i32, i32* %"a"
  %".13" = call i32 @"make_ptr_null"(i32* %"a")
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".16" = bitcast [3 x i8]* @"6ada16ef-55e6-4ecd-a79e-018464655601" to i8*
  %".17" = load i32, i32* %"a"
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %".17")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"11358178-a650-4cbd-b970-1cdd3bdc8a49" = constant [3 x i8] c"%d\00"
@"6ada16ef-55e6-4ecd-a79e-018464655601" = constant [3 x i8] c"%d\00"