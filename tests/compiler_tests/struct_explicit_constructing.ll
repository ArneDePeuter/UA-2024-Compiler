; ModuleID = ""

%"struct.Point" = type {i32, i32}
declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define void @"printPoint"(%"struct.Point" %".1")
{
entry:
  %"p" = alloca %"struct.Point"
  store %"struct.Point" %".1", %"struct.Point"* %"p"
  ; C Syntax: printf("%d", p.x);
  ; C Syntax: printf("%d", p.x)
  %".6" = bitcast [3 x i8]* @"44ab924f-2197-4661-bf0b-b19ae25f6342" to i8*
  %".7" = load %"struct.Point", %"struct.Point"* %"p"
  %".8" = getelementptr %"struct.Point", %"struct.Point"* %"p", i32 0, i32 0
  %".9" = load i32, i32* %".8"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".9")
  ; C Syntax: printf("%d", p.y);
  ; C Syntax: printf("%d", p.y)
  %".13" = bitcast [3 x i8]* @"ed5ba73d-64f1-4b33-a917-8fbb4fb4792f" to i8*
  %".14" = load %"struct.Point", %"struct.Point"* %"p"
  %".15" = getelementptr %"struct.Point", %"struct.Point"* %"p", i32 0, i32 1
  %".16" = load i32, i32* %".15"
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %".16")
  ret void
}

@"44ab924f-2197-4661-bf0b-b19ae25f6342" = constant [3 x i8] c"%d\00"
@"ed5ba73d-64f1-4b33-a917-8fbb4fb4792f" = constant [3 x i8] c"%d\00"
define i32 @"main"()
{
entry:
  ; C Syntax: printPoint((struct Point){1, 2});
  ; C Syntax: printPoint((struct Point){1, 2})
  ; C Syntax: 1
  %".5" = insertvalue %"struct.Point" zeroinitializer, i32 1, 0
  ; C Syntax: 2
  %".7" = insertvalue %"struct.Point" %".5", i32 2, 1
  call void @"printPoint"(%"struct.Point" %".7")
  ret i32 0
}
