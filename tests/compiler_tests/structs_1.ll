; ModuleID = ""

%"struct.B" = type {i32}
%"struct.A" = type {i32, i8, %"struct.B"}
declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define void @"printA"(%"struct.A" %".1")
{
entry:
  %"a" = alloca %"struct.A"
  store %"struct.A" %".1", %"struct.A"* %"a"
  ; C Syntax: printf("%d", a.num);
  ; C Syntax: printf("%d", a.num)
  %".6" = bitcast [3 x i8]* @"8a7f7bc9-aca3-4723-b2e3-a0e80acee523" to i8*
  %".7" = load %"struct.A", %"struct.A"* %"a"
  %".8" = getelementptr %"struct.A", %"struct.A"* %"a", i32 0, i32 0
  %".9" = load i32, i32* %".8"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".9")
  ; C Syntax: printf("%c", a.character);
  ; C Syntax: printf("%c", a.character)
  %".13" = bitcast [3 x i8]* @"03650a59-0290-41f2-8405-d115cf26394e" to i8*
  %".14" = load %"struct.A", %"struct.A"* %"a"
  %".15" = getelementptr %"struct.A", %"struct.A"* %"a", i32 0, i32 1
  %".16" = load i8, i8* %".15"
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".13", i8 %".16")
  ; C Syntax: printf("%d", a.b.num);
  ; C Syntax: printf("%d", a.b.num)
  %".20" = bitcast [3 x i8]* @"28ae4b7c-d9fe-40f6-ad9b-c408e75834c1" to i8*
  %".21" = load %"struct.A", %"struct.A"* %"a"
  %".22" = getelementptr %"struct.A", %"struct.A"* %"a", i32 0, i32 2
  %".23" = load %"struct.B", %"struct.B"* %".22"
  %".24" = getelementptr %"struct.B", %"struct.B"* %".22", i32 0, i32 0
  %".25" = load i32, i32* %".24"
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".25")
  ret void
}

@"8a7f7bc9-aca3-4723-b2e3-a0e80acee523" = constant [3 x i8] c"%d\00"
@"03650a59-0290-41f2-8405-d115cf26394e" = constant [3 x i8] c"%c\00"
@"28ae4b7c-d9fe-40f6-ad9b-c408e75834c1" = constant [3 x i8] c"%d\00"
define i32 @"main"()
{
entry:
  ; C Syntax: struct A a1 = {10, 'a', {1}};
  %"a1" = alloca %"struct.A"
  ; C Syntax: {10, 'a', {1}}
  ; C Syntax: 10
  %".5" = insertvalue %"struct.A" zeroinitializer, i32 10, 0
  ; C Syntax: 'a'
  %".7" = insertvalue %"struct.A" %".5", i8 97, 1
  ; C Syntax: {1}
  ; C Syntax: 1
  %".10" = insertvalue %"struct.B" zeroinitializer, i32 1, 0
  %".11" = insertvalue %"struct.A" %".7", %"struct.B" %".10", 2
  store %"struct.A" %".11", %"struct.A"* %"a1"
  ; C Syntax: printA((struct A){10,  'a', {1}});
  ; C Syntax: printA((struct A){10,  'a', {1}})
  ; C Syntax: 10
  %".16" = insertvalue %"struct.A" zeroinitializer, i32 10, 0
  ; C Syntax: 'a'
  %".18" = insertvalue %"struct.A" %".16", i8 97, 1
  ; C Syntax: {1}
  ; C Syntax: 1
  %".21" = insertvalue %"struct.B" zeroinitializer, i32 1, 0
  %".22" = insertvalue %"struct.A" %".18", %"struct.B" %".21", 2
  call void @"printA"(%"struct.A" %".22")
  ; C Syntax: printA(a1);
  ; C Syntax: printA(a1)
  %".26" = load %"struct.A", %"struct.A"* %"a1"
  call void @"printA"(%"struct.A" %".26")
  ; C Syntax: a1.num = 20;
  ; C Syntax: a1.num
  %".30" = load %"struct.A", %"struct.A"* %"a1"
  %".31" = getelementptr %"struct.A", %"struct.A"* %"a1", i32 0, i32 0
  %".32" = load i32, i32* %".31"
  ; C Syntax: 20
  store i32 20, i32* %".31"
  ; C Syntax: printA(a1);
  ; C Syntax: printA(a1)
  %".37" = load %"struct.A", %"struct.A"* %"a1"
  call void @"printA"(%"struct.A" %".37")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
