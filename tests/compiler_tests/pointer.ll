; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: int x = 4;
  %"x" = alloca i32
  ; C Syntax: 4
  store i32 4, i32* %"x"
  ; C Syntax: int y = 5;
  %"y" = alloca i32
  ; C Syntax: 5
  store i32 5, i32* %"y"
  ; C Syntax: int* ptr = &x;
  %"ptr" = alloca i32*
  ; C Syntax: &x
  %".10" = load i32, i32* %"x"
  store i32* %"x", i32** %"ptr"
  ; C Syntax: printf("%d", *ptr);
  ; C Syntax: printf("%d", *ptr)
  %".14" = bitcast [3 x i8]* @"0a6a5939-2a8e-48fe-a8d3-38dd6c210f11" to i8*
  %".15" = load i32*, i32** %"ptr"
  %".16" = load i32, i32* %".15"
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".16")
  ; C Syntax: ptr++;
  ; C Syntax: ptr++
  %".20" = load i32*, i32** %"ptr"
  %".21" = mul i32 1, 32
  %".22" = getelementptr i32, i32* %".20", i32 %".21"
  store i32* %".22", i32** %"ptr"
  ; C Syntax: ptr--;
  ; C Syntax: ptr--
  %".26" = load i32*, i32** %"ptr"
  %".27" = mul i32 1, 32
  %".28" = sub i32 0, %".27"
  %".29" = getelementptr i32, i32* %".26", i32 %".28"
  store i32* %".29", i32** %"ptr"
  ; C Syntax: printf("%d", *ptr);
  ; C Syntax: printf("%d", *ptr)
  %".33" = bitcast [3 x i8]* @"5cc48953-a484-47bd-a867-58ce2c291acf" to i8*
  %".34" = load i32*, i32** %"ptr"
  %".35" = load i32, i32* %".34"
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".33", i32 %".35")
  ret i32 0
}

@"0a6a5939-2a8e-48fe-a8d3-38dd6c210f11" = constant [3 x i8] c"%d\00"
@"5cc48953-a484-47bd-a867-58ce2c291acf" = constant [3 x i8] c"%d\00"