; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int a = 0;
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %".4" = load i32, i32* %"a"
  %".5" = icmp slt i32 %".4", 10
  br i1 %".5", label %"w_body", label %"w_after"
w_body:
  ; int b = 0;
  %"b" = alloca i32
  store i32 0, i32* %"b"
  %".9" = load i32, i32* %"b"
  %".10" = icmp slt i32 %".9", 4
  br i1 %".10", label %"w_body.1", label %"w_after.1"
w_after:
  ret i32 0
w_body.1:
  ; C Syntax: printf("%d", b);
  ; printf("%d", b)
  %".14" = load i32, i32* %"b"
  %".15" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_6_12" to i8*), i32 %".14")
  %".16" = load i32, i32* %"b"
  %".17" = load i32, i32* %"b"
  %".18" = add i32 %".17", 1
  %".19" = alloca i32
  store i32 %".18", i32* %".19"
  %".21" = load i32, i32* %".19"
  %".22" = icmp slt i32 %".21", 4
  br i1 %".22", label %"w_body.1", label %"w_after.1"
w_after.1:
  %".24" = load i32, i32* %"a"
  %".25" = load i32, i32* %"a"
  %".26" = add i32 %".25", 1
  %".27" = alloca i32
  store i32 %".26", i32* %".27"
  %".29" = load i32, i32* %".27"
  %".30" = icmp slt i32 %".29", 10
  br i1 %".30", label %"w_body", label %"w_after"
}

@"printf_format_6_12" = constant [3 x i8] c"%d\0a"
declare i32 @"printf"(i8* %".1", ...)
