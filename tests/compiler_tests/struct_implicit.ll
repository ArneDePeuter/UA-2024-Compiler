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
  %".6" = bitcast [3 x i8]* @"079a81c8-0399-47c2-b0c7-739f2257b9bc" to i8*
  %".7" = load %"struct.Point", %"struct.Point"* %"p"
  %".8" = getelementptr %"struct.Point", %"struct.Point"* %"p", i32 0, i32 0
  %".9" = load i32, i32* %".8"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".9")
  ; C Syntax: printf("%d", p.y);
  ; C Syntax: printf("%d", p.y)
  %".13" = bitcast [3 x i8]* @"66b2d7e5-7a7b-4d5a-a943-54b53962f295" to i8*
  %".14" = load %"struct.Point", %"struct.Point"* %"p"
  %".15" = getelementptr %"struct.Point", %"struct.Point"* %"p", i32 0, i32 1
  %".16" = load i32, i32* %".15"
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %".16")
  ret void
}

@"079a81c8-0399-47c2-b0c7-739f2257b9bc" = constant [3 x i8] c"%d\00"
@"66b2d7e5-7a7b-4d5a-a943-54b53962f295" = constant [3 x i8] c"%d\00"
define i32 @"main"()
{
entry:
  ; C Syntax: printPoint((struct Point){'a', 'b'});
  ; C Syntax: printPoint((struct Point){'a', 'b'})
  ; C Syntax: 'a'
  %".5" = zext i8 97 to i32
  %".6" = insertvalue %"struct.Point" zeroinitializer, i32 %".5", 0
  ; C Syntax: 'b'
  %".8" = zext i8 98 to i32
  %".9" = insertvalue %"struct.Point" %".6", i32 %".8", 1
  call void @"printPoint"(%"struct.Point" %".9")
  ret i32 0
}
