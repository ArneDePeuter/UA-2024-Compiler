; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int integer = 5;
  %"integer" = alloca i32
  store i32 5, i32* %"integer"
  ; int* int_ptr = &integer;
  %"int_ptr" = alloca i32*
  %".5" = load i32, i32* %"integer"
  store i32* %"integer", i32** %"int_ptr"
  ; int ** ptr_ptr = &int_ptr;
  %"ptr_ptr" = alloca i32**
  %".8" = load i32*, i32** %"int_ptr"
  store i32** %"int_ptr", i32*** %"ptr_ptr"
  ; int **another_pointer = ptr_ptr;
  %"another_pointer" = alloca i32**
  %".11" = load i32**, i32*** %"ptr_ptr"
  store i32** %".11", i32*** %"another_pointer"
  ; int z = integer + 5;
  %"z" = alloca i32
  %".14" = load i32, i32* %"integer"
  %".15" = add i32 %".14", 5
  store i32 %".15", i32* %"z"
  %".17" = load i32*, i32** %"int_ptr"
  %".18" = load i32, i32* %"z"
  %".19" = ptrtoint i32* %"z" to i32
  store i32 %".19", i32* %".17"
  ; int* pointer = &z;
  %"pointer" = alloca i32*
  %".22" = load i32, i32* %"z"
  store i32* %"z", i32** %"pointer"
  ; int x = *pointer;
  %"x" = alloca i32
  %".25" = load i32*, i32** %"pointer"
  %".26" = load i32, i32* %".25"
  store i32 %".26", i32* %"x"
  ; int** x_ptr = &int_ptr;
  %"x_ptr" = alloca i32**
  %".29" = load i32*, i32** %"int_ptr"
  store i32** %"int_ptr", i32*** %"x_ptr"
  ret i32 0
}
