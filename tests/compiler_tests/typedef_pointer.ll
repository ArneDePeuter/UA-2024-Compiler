; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: bool b = 0;
  %"b" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"b"
  ; C Syntax: b = 1;
  ; C Syntax: b
  %".7" = load i32, i32* %"b"
  ; C Syntax: 1
  store i32 1, i32* %"b"
  ; C Syntax: bool* b_ptr = &b;
  %"b_ptr" = alloca i32*
  ; C Syntax: &b
  %".12" = load i32, i32* %"b"
  store i32* %"b", i32** %"b_ptr"
  ; C Syntax: *b_ptr = 0;
  ; C Syntax: *b_ptr
  %".16" = load i32*, i32** %"b_ptr"
  %".17" = load i32, i32* %".16"
  ; C Syntax: 0
  store i32 0, i32* %".16"
  ; C Syntax: printf("%d", b);
  ; C Syntax: printf("%d", b)
  %".22" = bitcast [3 x i8]* @"c450d828-9999-4b3e-9f29-a06d613231b8" to i8*
  %".23" = load i32, i32* %"b"
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %".23")
  ret i32 0
}

@"c450d828-9999-4b3e-9f29-a06d613231b8" = constant [3 x i8] c"%d\00"