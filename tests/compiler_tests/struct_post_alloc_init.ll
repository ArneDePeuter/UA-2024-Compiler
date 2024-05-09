; ModuleID = ""

%"struct.Point" = type {i32, i32}
declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: struct Point p;
  %"p" = alloca %"struct.Point"
  store %"struct.Point" zeroinitializer, %"struct.Point"* %"p"
  ; C Syntax: p.x = 1;
  ; C Syntax: p.x
  %".6" = load %"struct.Point", %"struct.Point"* %"p"
  %".7" = getelementptr %"struct.Point", %"struct.Point"* %"p", i32 0, i32 0
  %".8" = load i32, i32* %".7"
  ; C Syntax: 1
  store i32 1, i32* %".7"
  ; C Syntax: p.y = 2;
  ; C Syntax: p.y
  %".13" = load %"struct.Point", %"struct.Point"* %"p"
  %".14" = getelementptr %"struct.Point", %"struct.Point"* %"p", i32 0, i32 1
  %".15" = load i32, i32* %".14"
  ; C Syntax: 2
  store i32 2, i32* %".14"
  ; C Syntax: int total = p.x + p.y;
  %"total" = alloca i32
  ; C Syntax: p.x + p.y
  %".20" = load %"struct.Point", %"struct.Point"* %"p"
  %".21" = getelementptr %"struct.Point", %"struct.Point"* %"p", i32 0, i32 0
  %".22" = load i32, i32* %".21"
  %".23" = load %"struct.Point", %"struct.Point"* %"p"
  %".24" = getelementptr %"struct.Point", %"struct.Point"* %"p", i32 0, i32 1
  %".25" = load i32, i32* %".24"
  %".26" = add i32 %".22", %".25"
  store i32 %".26", i32* %"total"
  ; C Syntax: printf("%d", total);
  ; C Syntax: printf("%d", total)
  %".30" = bitcast [3 x i8]* @"c450c025-f5f2-4397-97dd-3769b68974bb" to i8*
  %".31" = load i32, i32* %"total"
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".30", i32 %".31")
  ret i32 0
}

@"c450c025-f5f2-4397-97dd-3769b68974bb" = constant [3 x i8] c"%d\00"