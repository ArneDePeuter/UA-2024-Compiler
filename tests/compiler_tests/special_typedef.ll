; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: const ConstInt* b = 0;
  %"b" = alloca i32*
  ; C Syntax: 0
  store i32* null, i32** %"b"
  ; C Syntax: printf("%x", b);
  ; C Syntax: printf("%x", b)
  %".7" = bitcast [3 x i8]* @"744cfd61-bec8-4184-897e-e04671068686" to i8*
  %".8" = load i32*, i32** %"b"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".7", i32* %".8")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"744cfd61-bec8-4184-897e-e04671068686" = constant [3 x i8] c"%x\00"