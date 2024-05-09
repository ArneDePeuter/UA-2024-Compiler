; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int x = 5;
  %"x" = alloca i32
  ; C Syntax: 5
  store i32 5, i32* %"x"
  ; C Syntax: float f = x;
  %"f" = alloca float
  ; C Syntax: x
  %".7" = load i32, i32* %"x"
  %".8" = sitofp i32 %".7" to float
  store float %".8", float* %"f"
  ; C Syntax: int z = -32682;
  %"z" = alloca i32
  ; C Syntax: -32682
  %".12" = sub i32 0, 32682
  store i32 %".12", i32* %"z"
  ; C Syntax: f = 33.0 * z + x;
  ; C Syntax: f
  %".16" = load float, float* %"f"
  ; C Syntax: 33.0 * z + x
  %".18" = load i32, i32* %"z"
  %".19" = sitofp i32 %".18" to float
  %".20" = fmul float 0x4040800000000000, %".19"
  %".21" = load i32, i32* %"x"
  %".22" = sitofp i32 %".21" to float
  %".23" = fadd float %".20", %".22"
  store float %".23", float* %"f"
  ; C Syntax: z = f * 0.7;
  ; C Syntax: z
  %".27" = load i32, i32* %"z"
  ; C Syntax: f * 0.7
  %".29" = load float, float* %"f"
  %".30" = fmul float %".29", 0x3fe6666660000000
  %".31" = fptosi float %".30" to i32
  store i32 %".31", i32* %"z"
  ; C Syntax: int k = 'a' + 'z';
  %"k" = alloca i32
  ; C Syntax: 'a' + 'z'
  %".35" = add i8 97, 122
  %".36" = zext i8 %".35" to i32
  store i32 %".36", i32* %"k"
  ret i32 0
}
