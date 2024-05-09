; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"MONDAY" = global i32 0
@"TUESDAY" = global i32 1
define i32 @"main"()
{
entry:
  ; C Syntax: enum Days today = MONDAY;
  %"today" = alloca i32
  ; C Syntax: MONDAY
  %".4" = load i32, i32* @"MONDAY"
  store i32 %".4", i32* %"today"
  ; C Syntax: enum Days tomorrow = today + 1;
  %"tomorrow" = alloca i32
  ; C Syntax: today + 1
  %".8" = load i32, i32* %"today"
  %".9" = add i32 %".8", 1
  store i32 %".9", i32* %"tomorrow"
  ; C Syntax: float td = today;
  %"td" = alloca float
  ; C Syntax: today
  %".13" = load i32, i32* %"today"
  %".14" = sitofp i32 %".13" to float
  store float %".14", float* %"td"
  ; C Syntax: float tm = tomorrow;
  %"tm" = alloca float
  ; C Syntax: tomorrow
  %".18" = load i32, i32* %"tomorrow"
  %".19" = sitofp i32 %".18" to float
  store float %".19", float* %"tm"
  ; C Syntax: printf("%f", td);
  ; C Syntax: printf("%f", td)
  %".23" = bitcast [3 x i8]* @"2ed61117-99ca-44b4-8a51-5c0cf5b98fb1" to i8*
  %".24" = load float, float* %"td"
  %".25" = fpext float %".24" to double
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".23", double %".25")
  ; C Syntax: printf("%c", '\n');
  ; C Syntax: printf("%c", '\n')
  %".29" = bitcast [3 x i8]* @"3de1254e-a158-47e9-afb5-b69ec4f3d013" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i8 10)
  ; C Syntax: printf("%f", tm);
  ; C Syntax: printf("%f", tm)
  %".33" = bitcast [3 x i8]* @"77c076c6-29c5-49f6-922f-2a0ff0342e29" to i8*
  %".34" = load float, float* %"tm"
  %".35" = fpext float %".34" to double
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".33", double %".35")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}

@"2ed61117-99ca-44b4-8a51-5c0cf5b98fb1" = constant [3 x i8] c"%f\00"
@"3de1254e-a158-47e9-afb5-b69ec4f3d013" = constant [3 x i8] c"%c\00"
@"77c076c6-29c5-49f6-922f-2a0ff0342e29" = constant [3 x i8] c"%f\00"