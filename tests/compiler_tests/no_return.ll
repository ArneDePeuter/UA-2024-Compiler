; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i8 @"char_func"(i8 %".1")
{
entry:
  %"c" = alloca i8
  store i8 %".1", i8* %"c"
  ret i8 0
}

define i32 @"int_func"(i32 %".1")
{
entry:
  %"i" = alloca i32
  store i32 %".1", i32* %"i"
  ret i32 0
}

define float @"float_func"(float %".1")
{
entry:
  %"f" = alloca float
  store float %".1", float* %"f"
  ret float 0.0
}

define void @"void_func"()
{
entry:
  ret void
}

define i32* @"int_ptr_func"(i32* %".1")
{
entry:
  %"i" = alloca i32*
  store i32* %".1", i32** %"i"
  ret i32* null
}

define i32 @"main"()
{
entry:
  ; C Syntax: char_func('a');
  ; C Syntax: char_func('a')
  %".4" = call i8 @"char_func"(i8 97)
  ; C Syntax: int_func(1);
  ; C Syntax: int_func(1)
  %".7" = call i32 @"int_func"(i32 1)
  ; C Syntax: float_func(1.0);
  ; C Syntax: float_func(1.0)
  %".10" = call float @"float_func"(float 0x3ff0000000000000)
  ; C Syntax: void_func();
  ; C Syntax: void_func()
  call void @"void_func"()
  ; C Syntax: int i = 1;
  %"i" = alloca i32
  ; C Syntax: 1
  store i32 1, i32* %"i"
  ; C Syntax: int_ptr_func(&i);
  ; C Syntax: int_ptr_func(&i)
  %".19" = load i32, i32* %"i"
  %".20" = call i32* @"int_ptr_func"(i32* %"i")
  ; C Syntax: return 0;
  ; C Syntax: 0
  ret i32 0
}
