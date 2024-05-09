; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char c[2][3] = {{'a', 'b', 'c'}, {'d', 'e', 'f'}};
  %"c" = alloca [2 x [3 x i8]]
  ; C Syntax: {{'a', 'b', 'c'}, {'d', 'e', 'f'}}
  ; C Syntax: {'a', 'b', 'c'}
  ; C Syntax: 'a'
  ; C Syntax: 'b'
  ; C Syntax: 'c'
  ; C Syntax: {'d', 'e', 'f'}
  ; C Syntax: 'd'
  ; C Syntax: 'e'
  ; C Syntax: 'f'
  store [2 x [3 x i8]] [[3 x i8] [i8 97, i8 98, i8 99], [3 x i8] [i8 100, i8 101, i8 102]], [2 x [3 x i8]]* %"c"
  ; C Syntax: printf("%c", c[0][0]);
  ; C Syntax: printf("%c", c[0][0])
  %".15" = bitcast [3 x i8]* @"13129597-2785-4348-9091-409f3c90e507" to i8*
  %".16" = load [2 x [3 x i8]], [2 x [3 x i8]]* %"c"
  %".17" = getelementptr [2 x [3 x i8]], [2 x [3 x i8]]* %"c", i32 0, i32 0
  %".18" = load [3 x i8], [3 x i8]* %".17"
  %".19" = getelementptr [3 x i8], [3 x i8]* %".17", i32 0, i32 0
  %".20" = load i8, i8* %".19"
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".15", i8 %".20")
  ; C Syntax: c[0][0] = 'x';
  ; C Syntax: c[0][0]
  %".24" = load [2 x [3 x i8]], [2 x [3 x i8]]* %"c"
  %".25" = getelementptr [2 x [3 x i8]], [2 x [3 x i8]]* %"c", i32 0, i32 0
  %".26" = load [3 x i8], [3 x i8]* %".25"
  %".27" = getelementptr [3 x i8], [3 x i8]* %".25", i32 0, i32 0
  %".28" = load i8, i8* %".27"
  ; C Syntax: 'x'
  store i8 120, i8* %".27"
  ; C Syntax: printf("%c", c[0][0]);
  ; C Syntax: printf("%c", c[0][0])
  %".33" = bitcast [3 x i8]* @"9f053411-1564-429e-9231-7771001a7bbe" to i8*
  %".34" = load [2 x [3 x i8]], [2 x [3 x i8]]* %"c"
  %".35" = getelementptr [2 x [3 x i8]], [2 x [3 x i8]]* %"c", i32 0, i32 0
  %".36" = load [3 x i8], [3 x i8]* %".35"
  %".37" = getelementptr [3 x i8], [3 x i8]* %".35", i32 0, i32 0
  %".38" = load i8, i8* %".37"
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".33", i8 %".38")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"13129597-2785-4348-9091-409f3c90e507" = constant [3 x i8] c"%c\00"
@"9f053411-1564-429e-9231-7771001a7bbe" = constant [3 x i8] c"%c\00"