; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

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
  ; C Syntax: ptr++;
  ; C Syntax: ptr++
  %".14" = load i32*, i32** %"ptr"
  %".15" = mul i32 1, 32
  %".16" = getelementptr i32, i32* %".14", i32 %".15"
  store i32* %".16", i32** %"ptr"
  ; C Syntax: // now points to y-
  ; // now points to y
  ; C Syntax: ptr--;
  ; C Syntax: ptr--
  %".22" = load i32*, i32** %"ptr"
  %".23" = mul i32 1, 32
  %".24" = sub i32 0, %".23"
  %".25" = getelementptr i32, i32* %".22", i32 %".24"
  store i32* %".25", i32** %"ptr"
  ; C Syntax: // now points to x-
  ; // now points to x
  ; C Syntax: int is_x = (ptr == &x);
  %"is_x" = alloca i32
  ; C Syntax: (ptr == &x)
  %".31" = load i32*, i32** %"ptr"
  %".32" = load i32, i32* %"x"
  %".33" = ptrtoint i32* %".31" to i32
  %".34" = ptrtoint i32* %"x" to i32
  %".35" = icmp eq i32 %".33", %".34"
  %".36" = zext i1 %".35" to i32
  store i32 %".36", i32* %"is_x"
  ; C Syntax: int is_y = (ptr == &y);
  %"is_y" = alloca i32
  ; C Syntax: (ptr == &y)
  %".40" = load i32*, i32** %"ptr"
  %".41" = load i32, i32* %"y"
  %".42" = ptrtoint i32* %".40" to i32
  %".43" = ptrtoint i32* %"y" to i32
  %".44" = icmp eq i32 %".42", %".43"
  %".45" = zext i1 %".44" to i32
  store i32 %".45", i32* %"is_y"
  ; C Syntax: is_y = (&x != ptr);
  ; C Syntax: is_y
  %".49" = load i32, i32* %"is_y"
  ; C Syntax: (&x != ptr)
  %".51" = load i32, i32* %"x"
  %".52" = load i32*, i32** %"ptr"
  %".53" = ptrtoint i32* %"x" to i32
  %".54" = ptrtoint i32* %".52" to i32
  %".55" = icmp ne i32 %".53", %".54"
  %".56" = zext i1 %".55" to i32
  store i32 %".56", i32* %"is_y"
  ; C Syntax: float* ptr2 = 0;
  %"ptr2" = alloca float*
  ; C Syntax: 0
  store float* null, float** %"ptr2"
  ; C Syntax: ptr2 >= ptr;
  ; C Syntax: ptr2 >= ptr
  %".63" = load float*, float** %"ptr2"
  %".64" = load i32*, i32** %"ptr"
  %".65" = ptrtoint float* %".63" to i32
  %".66" = ptrtoint i32* %".64" to i32
  %".67" = icmp sge i32 %".65", %".66"
  ; C Syntax: ptr2 <= ptr;
  ; C Syntax: ptr2 <= ptr
  %".70" = load float*, float** %"ptr2"
  %".71" = load i32*, i32** %"ptr"
  %".72" = ptrtoint float* %".70" to i32
  %".73" = ptrtoint i32* %".71" to i32
  %".74" = icmp sle i32 %".72", %".73"
  ; C Syntax: ptr > &x;
  ; C Syntax: ptr > &x
  %".77" = load i32*, i32** %"ptr"
  %".78" = load i32, i32* %"x"
  %".79" = ptrtoint i32* %".77" to i32
  %".80" = ptrtoint i32* %"x" to i32
  %".81" = icmp sgt i32 %".79", %".80"
  ; C Syntax: ptr < 32;
  ; C Syntax: ptr < 32
  %".84" = load i32*, i32** %"ptr"
  %".85" = ptrtoint i32* %".84" to i32
  %".86" = icmp slt i32 %".85", 32
  ; C Syntax: int num_skip_elements = 4;
  %"num_skip_elements" = alloca i32
  ; C Syntax: 4
  store i32 4, i32* %"num_skip_elements"
  ; C Syntax: ptr = ptr + 4*num_skip_elements;
  ; C Syntax: ptr
  %".92" = load i32*, i32** %"ptr"
  ; C Syntax: ptr + 4*num_skip_elements
  %".94" = load i32*, i32** %"ptr"
  %".95" = mul i32 16, 32
  %".96" = getelementptr i32, i32* %".94", i32 %".95"
  store i32* %".96", i32** %"ptr"
  ret i32 0
}
