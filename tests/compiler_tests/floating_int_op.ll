; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int i1 = 10, i2= 3;
  %"i1" = alloca i32
  ; C Syntax: 10
  store i32 10, i32* %"i1"
  %"i2" = alloca i32
  ; C Syntax: 3
  store i32 3, i32* %"i2"
  ; C Syntax: float f1 = 10.0, f2 = 3.0;
  %"f1" = alloca float
  ; C Syntax: 10.0
  store float 0x4024000000000000, float* %"f1"
  %"f2" = alloca float
  ; C Syntax: 3.0
  store float 0x4008000000000000, float* %"f2"
  ; C Syntax: printf("%d", i1 + i2);
  ; C Syntax: printf("%d", i1 + i2)
  %".14" = bitcast [3 x i8]* @"f2392837-6f3f-4af0-8754-0c0bee1c63e8" to i8*
  %".15" = load i32, i32* %"i1"
  %".16" = load i32, i32* %"i2"
  %".17" = add i32 %".15", %".16"
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".17")
  ; C Syntax: printf("%d", i1 - i2);
  ; C Syntax: printf("%d", i1 - i2)
  %".21" = bitcast [3 x i8]* @"68ebd854-7ad5-45c2-a988-10469ec3b6f3" to i8*
  %".22" = load i32, i32* %"i1"
  %".23" = load i32, i32* %"i2"
  %".24" = sub i32 %".22", %".23"
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".21", i32 %".24")
  ; C Syntax: printf("%d", i1 * i2);
  ; C Syntax: printf("%d", i1 * i2)
  %".28" = bitcast [3 x i8]* @"662fff32-5814-42ca-9455-17ccff5a596a" to i8*
  %".29" = load i32, i32* %"i1"
  %".30" = load i32, i32* %"i2"
  %".31" = mul i32 %".29", %".30"
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".28", i32 %".31")
  ; C Syntax: printf("%d", i1 / i2);
  ; C Syntax: printf("%d", i1 / i2)
  %".35" = bitcast [3 x i8]* @"949246b0-c679-495f-8f17-9280304dd9ea" to i8*
  %".36" = load i32, i32* %"i1"
  %".37" = load i32, i32* %"i2"
  %".38" = sdiv i32 %".36", %".37"
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".35", i32 %".38")
  ; C Syntax: printf("%d", i1 % i2);
  ; C Syntax: printf("%d", i1 % i2)
  %".42" = bitcast [3 x i8]* @"2091a34e-589e-44c3-88af-fd71840a987c" to i8*
  %".43" = load i32, i32* %"i1"
  %".44" = load i32, i32* %"i2"
  %".45" = srem i32 %".43", %".44"
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".42", i32 %".45")
  ; C Syntax: printf("%f", f1 + f2);
  ; C Syntax: printf("%f", f1 + f2)
  %".49" = bitcast [3 x i8]* @"dfdac2a8-d498-4419-aada-9782c7d7967b" to i8*
  %".50" = load float, float* %"f1"
  %".51" = load float, float* %"f2"
  %".52" = fadd float %".50", %".51"
  %".53" = fpext float %".52" to double
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".49", double %".53")
  ; C Syntax: printf("%f", f1 - f2);
  ; C Syntax: printf("%f", f1 - f2)
  %".57" = bitcast [3 x i8]* @"c212713c-6d99-4208-aaef-6f4f2aefd880" to i8*
  %".58" = load float, float* %"f1"
  %".59" = load float, float* %"f2"
  %".60" = fsub float %".58", %".59"
  %".61" = fpext float %".60" to double
  %".62" = call i32 (i8*, ...) @"printf"(i8* %".57", double %".61")
  ; C Syntax: printf("%f", f1 * f2);
  ; C Syntax: printf("%f", f1 * f2)
  %".65" = bitcast [3 x i8]* @"11288793-c1d8-4fcf-8134-e385d0672980" to i8*
  %".66" = load float, float* %"f1"
  %".67" = load float, float* %"f2"
  %".68" = fmul float %".66", %".67"
  %".69" = fpext float %".68" to double
  %".70" = call i32 (i8*, ...) @"printf"(i8* %".65", double %".69")
  ; C Syntax: printf("%f", f1 / f2);
  ; C Syntax: printf("%f", f1 / f2)
  %".73" = bitcast [3 x i8]* @"f8ffac6e-14fe-427e-8ad6-ce181cbaded2" to i8*
  %".74" = load float, float* %"f1"
  %".75" = load float, float* %"f2"
  %".76" = fdiv float %".74", %".75"
  %".77" = fpext float %".76" to double
  %".78" = call i32 (i8*, ...) @"printf"(i8* %".73", double %".77")
  ret i32 0
}

@"f2392837-6f3f-4af0-8754-0c0bee1c63e8" = constant [3 x i8] c"%d\00"
@"68ebd854-7ad5-45c2-a988-10469ec3b6f3" = constant [3 x i8] c"%d\00"
@"662fff32-5814-42ca-9455-17ccff5a596a" = constant [3 x i8] c"%d\00"
@"949246b0-c679-495f-8f17-9280304dd9ea" = constant [3 x i8] c"%d\00"
@"2091a34e-589e-44c3-88af-fd71840a987c" = constant [3 x i8] c"%d\00"
@"dfdac2a8-d498-4419-aada-9782c7d7967b" = constant [3 x i8] c"%f\00"
@"c212713c-6d99-4208-aaef-6f4f2aefd880" = constant [3 x i8] c"%f\00"
@"11288793-c1d8-4fcf-8134-e385d0672980" = constant [3 x i8] c"%f\00"
@"f8ffac6e-14fe-427e-8ad6-ce181cbaded2" = constant [3 x i8] c"%f\00"