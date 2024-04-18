; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int a = 0;
  %"a" = alloca i32
  ; C Syntax: 0
  store i32 0, i32* %"a"
  ; C Syntax: {-        a++;-        {-            a--;-        }-    }
  ; C Syntax: a++;
  ; C Syntax: a++
  %".8" = load i32, i32* %"a"
  %".9" = add i32 %".8", 1
  store i32 %".9", i32* %"a"
  ; C Syntax: {-            a--;-        }
  ; C Syntax: a--;
  ; C Syntax: a--
  %".14" = load i32, i32* %"a"
  %".15" = sub i32 %".14", 1
  store i32 %".15", i32* %"a"
  ; C Syntax: printf("%d", a);
  ; C Syntax: printf("%d", a)
  %".19" = load i32, i32* %"a"
  %".20" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_9_4" to i8*), i32 %".19")
  ret i32 0
}

@"printf_format_9_4" = constant [3 x i8] c"%d\0a"