; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int num = 255;
  %"num" = alloca i32
  ; C Syntax: 255
  store i32 255, i32* %"num"
  ; C Syntax: float pi = 3.14159;
  %"pi" = alloca float
  ; C Syntax: 3.14159
  store float 0x400921fa00000000, float* %"pi"
  ; C Syntax: char ch = 'A';
  %"ch" = alloca i8
  ; C Syntax: 'A'
  store i8 65, i8* %"ch"
  ; C Syntax: char* str = "Hello, World!";
  %"str" = alloca i8*
  ; C Syntax: "Hello, World!"
  %"str_array" = alloca [14 x i8]
  store [14 x i8] [i8 72, i8 101, i8 108, i8 108, i8 111, i8 44, i8 32, i8 87, i8 111, i8 114, i8 108, i8 100, i8 33, i8 0], [14 x i8]* %"str_array"
  %".14" = getelementptr [14 x i8], [14 x i8]* %"str_array", i32 0, i32 0
  store i8* %".14", i8** %"str"
  ; C Syntax: printf("Decimal: %d\n", num);
  ; C Syntax: printf("Decimal: %d\n", num)
  %".18" = bitcast [13 x i8]* @"11bc41bf-3e2d-4389-a884-c9ea1e856849" to i8*
  %".19" = load i32, i32* %"num"
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".18", i32 %".19")
  ; C Syntax: printf("Hexadecimal: %x\n", num);
  ; C Syntax: printf("Hexadecimal: %x\n", num)
  %".23" = bitcast [17 x i8]* @"51a2338b-a497-4eae-8954-36140b9b66e0" to i8*
  %".24" = load i32, i32* %"num"
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %".24")
  ; C Syntax: printf("Pi: %.2f\n", pi);
  ; C Syntax: printf("Pi: %.2f\n", pi)
  %".28" = bitcast [10 x i8]* @"2d6c0da9-36fe-46cb-a530-ed9a171f5872" to i8*
  %".29" = load float, float* %"pi"
  %".30" = fpext float %".29" to double
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".28", double %".30")
  ; C Syntax: printf("Character: %c\n", ch);
  ; C Syntax: printf("Character: %c\n", ch)
  %".34" = bitcast [15 x i8]* @"f76d0abb-5cd5-4b53-a4e0-48e3960a6cf2" to i8*
  %".35" = load i8, i8* %"ch"
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".34", i8 %".35")
  ; C Syntax: printf("String: %s\n", str);
  ; C Syntax: printf("String: %s\n", str)
  %".39" = bitcast [12 x i8]* @"266122a1-5972-4ef0-a1b5-d70329dd5f22" to i8*
  %".40" = load i8*, i8** %"str"
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".39", i8* %".40")
  ; C Syntax: printf("Print 100%% complete\n");
  ; C Syntax: printf("Print 100%% complete\n")
  %".44" = bitcast [22 x i8]* @"6d915fcb-fd03-4989-afdd-48b0c867a4ca" to i8*
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"11bc41bf-3e2d-4389-a884-c9ea1e856849" = constant [13 x i8] c"Decimal: %d\0a\00"
@"51a2338b-a497-4eae-8954-36140b9b66e0" = constant [17 x i8] c"Hexadecimal: %x\0a\00"
@"2d6c0da9-36fe-46cb-a530-ed9a171f5872" = constant [10 x i8] c"Pi: %.2f\0a\00"
@"f76d0abb-5cd5-4b53-a4e0-48e3960a6cf2" = constant [15 x i8] c"Character: %c\0a\00"
@"266122a1-5972-4ef0-a1b5-d70329dd5f22" = constant [12 x i8] c"String: %s\0a\00"
@"6d915fcb-fd03-4989-afdd-48b0c867a4ca" = constant [22 x i8] c"Print 100%% complete\0a\00"