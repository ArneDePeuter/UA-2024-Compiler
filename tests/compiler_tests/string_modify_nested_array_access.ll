; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
  %"a" = alloca [2 x [3 x i32]]
  ; C Syntax: {{1, 2, 3}, {4, 5, 6}}
  ; C Syntax: {1, 2, 3}
  ; C Syntax: 1
  ; C Syntax: 2
  ; C Syntax: 3
  ; C Syntax: {4, 5, 6}
  ; C Syntax: 4
  ; C Syntax: 5
  ; C Syntax: 6
  store [2 x [3 x i32]] [[3 x i32] [i32 1, i32 2, i32 3], [3 x i32] [i32 4, i32 5, i32 6]], [2 x [3 x i32]]* %"a"
  ; C Syntax: printf("%d", a[1][2]);
  ; C Syntax: printf("%d", a[1][2])
  %".15" = bitcast [3 x i8]* @"f398b5f3-9f5e-4f12-98cc-e6b4e4a16e3e" to i8*
  %".16" = load [2 x [3 x i32]], [2 x [3 x i32]]* %"a"
  %".17" = getelementptr [2 x [3 x i32]], [2 x [3 x i32]]* %"a", i32 0, i32 1
  %".18" = load [3 x i32], [3 x i32]* %".17"
  %".19" = getelementptr [3 x i32], [3 x i32]* %".17", i32 0, i32 2
  %".20" = load i32, i32* %".19"
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".20")
  ; C Syntax: a[1][2] = 7;
  ; C Syntax: a[1][2]
  %".24" = load [2 x [3 x i32]], [2 x [3 x i32]]* %"a"
  %".25" = getelementptr [2 x [3 x i32]], [2 x [3 x i32]]* %"a", i32 0, i32 1
  %".26" = load [3 x i32], [3 x i32]* %".25"
  %".27" = getelementptr [3 x i32], [3 x i32]* %".25", i32 0, i32 2
  %".28" = load i32, i32* %".27"
  ; C Syntax: 7
  store i32 7, i32* %".27"
  ; C Syntax: printf("%d", a[1][2]);
  ; C Syntax: printf("%d", a[1][2])
  %".33" = bitcast [3 x i8]* @"f7f5e9fa-8463-4e60-894b-a326b680f21e" to i8*
  %".34" = load [2 x [3 x i32]], [2 x [3 x i32]]* %"a"
  %".35" = getelementptr [2 x [3 x i32]], [2 x [3 x i32]]* %"a", i32 0, i32 1
  %".36" = load [3 x i32], [3 x i32]* %".35"
  %".37" = getelementptr [3 x i32], [3 x i32]* %".35", i32 0, i32 2
  %".38" = load i32, i32* %".37"
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".33", i32 %".38")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"f398b5f3-9f5e-4f12-98cc-e6b4e4a16e3e" = constant [3 x i8] c"%d\00"
@"f7f5e9fa-8463-4e60-894b-a326b680f21e" = constant [3 x i8] c"%d\00"