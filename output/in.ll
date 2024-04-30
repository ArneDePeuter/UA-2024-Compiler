; ModuleID = ""

%"struct.B" = type {i32}
%"struct.A" = type {i32, i8, %"struct.B"}
declare i32 @"printf"(i8* %".1", ...)

define void @"printA"(%"struct.A" %".1")
{
entry:
  %"a" = alloca %"struct.A"
  store %"struct.A" %".1", %"struct.A"* %"a"
  ; C Syntax: //    printf("%d", a.numarray[0]);-
  ; //    printf("%d", a.numarray[0]);
  ; C Syntax: //    printf("%d", a.numarray[1]);-
  ; //    printf("%d", a.numarray[1]);
  ; C Syntax: //    printf("%d", a.numarray[2]);-
  ; //    printf("%d", a.numarray[2]);
  ; C Syntax: printf("%d", a.num);
  ; C Syntax: printf("%d", a.num)
  ; C Syntax: a.num
  %".13" = load %"struct.A", %"struct.A"* %"a"
  %".14" = getelementptr %"struct.A", %"struct.A"* %"a", i32 0, i32 0
  %".15" = load i32, i32* %".14"
  %".16" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_15_4" to i8*), i32 %".15")
  ; C Syntax: printf("%c", a.character);
  ; C Syntax: printf("%c", a.character)
  ; C Syntax: a.character
  %".20" = load %"struct.A", %"struct.A"* %"a"
  %".21" = getelementptr %"struct.A", %"struct.A"* %"a", i32 0, i32 1
  %".22" = load i8, i8* %".21"
  %".23" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_16_4" to i8*), i8 %".22")
  ; C Syntax: printf("%d", a.b.num);
  ; C Syntax: printf("%d", a.b.num)
  ; C Syntax: a.b.num
  %".27" = load %"struct.A", %"struct.A"* %"a"
  %".28" = getelementptr %"struct.A", %"struct.A"* %"a", i32 0, i32 2
  %".29" = load %"struct.B", %"struct.B"* %".28"
  %".30" = getelementptr %"struct.B", %"struct.B"* %".28", i32 0, i32 0
  %".31" = load i32, i32* %".30"
  %".32" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_17_4" to i8*), i32 %".31")
  ret void
}

@"printf_format_15_4" = internal constant [3 x i8] c"%d\00"
@"printf_format_16_4" = internal constant [3 x i8] c"%c\00"
@"printf_format_17_4" = internal constant [3 x i8] c"%d\00"
define i32 @"main"()
{
entry:
  ; C Syntax: struct A a1 = {10, 'a', {1}};
  %"a1" = alloca %"struct.A"
  ; C Syntax: {10, 'a', {1}}
  ; C Syntax: 10
  ; C Syntax: 'a'
  ; C Syntax: 1
  store %"struct.A" {i32 10, i8 97, %"struct.B" {i32 1}}, %"struct.A"* %"a1"
  ; C Syntax: printA((struct A){10,  'a', {1}});
  ; C Syntax: printA((struct A){10,  'a', {1}})
  ; C Syntax: (struct A){10,  'a', {1}}
  ; C Syntax: 10
  ; C Syntax: 'a'
  ; C Syntax: 1
  call void @"printA"(%"struct.A" {i32 10, i8 97, %"struct.B" {i32 1}})
  ; C Syntax: printA(a1);
  ; C Syntax: printA(a1)
  ; C Syntax: a1
  %".18" = load %"struct.A", %"struct.A"* %"a1"
  call void @"printA"(%"struct.A" %".18")
  ; C Syntax: a1.num = 20;
  ; C Syntax: a1.num
  %".22" = load %"struct.A", %"struct.A"* %"a1"
  %".23" = getelementptr %"struct.A", %"struct.A"* %"a1", i32 0, i32 0
  %".24" = load i32, i32* %".23"
  ; C Syntax: 20
  store i32 20, i32* %".23"
  ; C Syntax: printA(a1);
  ; C Syntax: printA(a1)
  ; C Syntax: a1
  %".30" = load %"struct.A", %"struct.A"* %"a1"
  call void @"printA"(%"struct.A" %".30")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
