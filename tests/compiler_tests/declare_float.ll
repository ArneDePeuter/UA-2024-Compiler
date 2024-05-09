; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: float a = 1;
  %"a" = alloca float
  ; C Syntax: 1
  %".4" = sitofp i32 1 to float
  store float %".4", float* %"a"
  ; C Syntax: printf("%d", (int) a);
  ; C Syntax: printf("%d", (int) a)
  %".8" = bitcast [3 x i8]* @"1518bb72-c2b9-4c6f-8891-d2766ea50a46" to i8*
  %".9" = load float, float* %"a"
  %".10" = fptosi float %".9" to i32
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".10")
  ret i32 0
}

@"1518bb72-c2b9-4c6f-8891-d2766ea50a46" = constant [3 x i8] c"%d\00"