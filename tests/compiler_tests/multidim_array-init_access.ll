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
  ; C Syntax: c[0][0] = 'x';
  ; C Syntax: c[0][0]
  %".15" = load [2 x [3 x i8]], [2 x [3 x i8]]* %"c"
  %".16" = getelementptr [2 x [3 x i8]], [2 x [3 x i8]]* %"c", i32 0, i32 0
  %".17" = load [3 x i8], [3 x i8]* %".16"
  %".18" = getelementptr [3 x i8], [3 x i8]* %".16", i32 0, i32 0
  %".19" = load i8, i8* %".18"
  ; C Syntax: 'x'
  store i8 120, i8* %".18"
  ; C Syntax: printf("%c", c[0][0]);
  ; C Syntax: printf("%c", c[0][0])
  %".24" = bitcast [3 x i8]* @"dbf8d7c9-e6f4-44d9-9256-8b2078cdfc5d" to i8*
  %".25" = load [2 x [3 x i8]], [2 x [3 x i8]]* %"c"
  %".26" = getelementptr [2 x [3 x i8]], [2 x [3 x i8]]* %"c", i32 0, i32 0
  %".27" = load [3 x i8], [3 x i8]* %".26"
  %".28" = getelementptr [3 x i8], [3 x i8]* %".26", i32 0, i32 0
  %".29" = load i8, i8* %".28"
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".24", i8 %".29")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"dbf8d7c9-e6f4-44d9-9256-8b2078cdfc5d" = constant [3 x i8] c"%c\00"