; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; // More complex constant folding example
  ;
  ; C Syntax: const int a = (2 + 3) * (4 << 1) + 1;
  %"a" = alloca i32
  store i32 41, i32* %"a"
  ; // (5 * 8) + 1 = 41 computed at compile time
  ;
  ; // Constant propagation example
  ;
  ; C Syntax: int b = a;
  %"b" = alloca i32
  ; C Syntax: a
  %".12" = load i32, i32* %"a"
  store i32 %".12", i32* %"b"
  ; // 'b' is initialized with the constant value of 'a'
  ;
  ; // Using the constants
  ;
  ; C Syntax: printf("The value of 'a' after more complex constant folding: %d\n", a);
  ; C Syntax: printf("The value of 'a' after more complex constant folding: %d\n", a)
  %".20" = bitcast [58 x i8]* @"eb7d0847-fe07-4ea0-8f9c-8650340c686c" to i8*
  %".21" = load i32, i32* %"a"
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".21")
  ; C Syntax: printf("The value of 'b' after constant propagation from 'a': %d\n", b);
  ; C Syntax: printf("The value of 'b' after constant propagation from 'a': %d\n", b)
  %".25" = bitcast [58 x i8]* @"6c417ee3-8619-4647-99f5-bf5390be4ed5" to i8*
  %".26" = load i32, i32* %"b"
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".25", i32 %".26")
  ; // Further complex constant folding
  ;
  ; C Syntax: const int c = (a * 20) / 2;
  %"c" = alloca i32
  ; C Syntax: (a * 20) / 2
  ; C Syntax: a * 20
  %".33" = load i32, i32* %"a"
  %".34" = mul i32 %".33", 20
  %".35" = sdiv i32 %".34", 2
  store i32 %".35", i32* %"c"
  ; // Calculation is done at compile time
  ;
  ; C Syntax: printf("The value of 'c' after further complex constant folding: %d\n", c);
  ; C Syntax: printf("The value of 'c' after further complex constant folding: %d\n", c)
  %".41" = bitcast [61 x i8]* @"f969320e-b554-42a1-a16d-65ea3af4fb9a" to i8*
  %".42" = load i32, i32* %"c"
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".41", i32 %".42")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"eb7d0847-fe07-4ea0-8f9c-8650340c686c" = constant [58 x i8] c"The value of 'a' after more complex constant folding: %d\0a\00"
@"6c417ee3-8619-4647-99f5-bf5390be4ed5" = constant [58 x i8] c"The value of 'b' after constant propagation from 'a': %d\0a\00"
@"f969320e-b554-42a1-a16d-65ea3af4fb9a" = constant [61 x i8] c"The value of 'c' after further complex constant folding: %d\0a\00"