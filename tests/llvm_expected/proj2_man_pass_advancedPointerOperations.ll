; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; int x = 4;
  %"x" = alloca i32
  store i32 4, i32* %"x"
  ; int y = 5;
  %"y" = alloca i32
  store i32 5, i32* %"y"
  ; int* ptr = &x;
  %"ptr" = alloca i32*
  %".7" = load i32, i32* %"x"
  store i32* %"x", i32** %"ptr"
  ; C Syntax: ptr++;
  %".10" = load i32*, i32** %"ptr"
  %".11" = getelementptr i32, i32* %".10", i32 1
  ; // now points to y
  ; C Syntax: ptr--;
  %".14" = load i32*, i32** %"ptr"
  %".15" = getelementptr i32, i32* %".14", i32 -1
  ; // now points to x
  ; int is_x = (ptr == &x);
  %"is_x" = alloca i32
  %".18" = load i32*, i32** %"ptr"
  %".19" = load i32, i32* %"x"
  %".20" = ptrtoint i32* %".18" to i64
  %".21" = ptrtoint i32* %"x" to i64
  %".22" = icmp eq i64 %".20", %".21"
  %".23" = zext i1 %".22" to i32
  store i32 %".23", i32* %"is_x"
  ; int is_y = (ptr == &y);
  %"is_y" = alloca i32
  %".26" = load i32*, i32** %"ptr"
  %".27" = load i32, i32* %"y"
  %".28" = ptrtoint i32* %".26" to i64
  %".29" = ptrtoint i32* %"y" to i64
  %".30" = icmp eq i64 %".28", %".29"
  %".31" = zext i1 %".30" to i32
  store i32 %".31", i32* %"is_y"
  %".33" = load i32, i32* %"is_y"
  %".34" = load i32, i32* %"x"
  %".35" = load i32*, i32** %"ptr"
  %".36" = ptrtoint i32* %"x" to i64
  %".37" = ptrtoint i32* %".35" to i64
  %".38" = icmp ne i64 %".36", %".37"
  %".39" = alloca i32
  %".40" = sext i1 %".38" to i32
  store i32 %".40", i32* %".39"
  ; float* ptr2 = 0;
  %"ptr2" = alloca double*
  store double* null, double** %"ptr2"
  ; C Syntax: ptr2 >= ptr;
  %".45" = load double*, double** %"ptr2"
  %".46" = load i32*, i32** %"ptr"
  %".47" = ptrtoint double* %".45" to i64
  %".48" = ptrtoint i32* %".46" to i64
  %".49" = icmp uge i64 %".47", %".48"
  ; C Syntax: ptr2 <= ptr;
  %".51" = load double*, double** %"ptr2"
  %".52" = load i32*, i32** %"ptr"
  %".53" = ptrtoint double* %".51" to i64
  %".54" = ptrtoint i32* %".52" to i64
  %".55" = icmp ule i64 %".53", %".54"
  ; C Syntax: ptr > &x;
  %".57" = load i32*, i32** %"ptr"
  %".58" = load i32, i32* %"x"
  %".59" = ptrtoint i32* %".57" to i64
  %".60" = ptrtoint i32* %"x" to i64
  %".61" = icmp ugt i64 %".59", %".60"
  ; C Syntax: ptr < 32;
  %".63" = load i32*, i32** %"ptr"
  %".64" = ptrtoint i32* %".63" to i64
  %".65" = zext i32 32 to i64
  %".66" = icmp ult i64 %".64", %".65"
  ; int num_skip_elements = 4;
  %"num_skip_elements" = alloca i32
  store i32 4, i32* %"num_skip_elements"
  %".69" = load i32*, i32** %"ptr"
  %".70" = load i32*, i32** %"ptr"
  %".71" = load i32, i32* %"num_skip_elements"
  %".72" = mul i32 4, %".71"
  %".73" = getelementptr i32, i32* %".70", i32 %".72"
  %".74" = ptrtoint i32* %".73" to i32
  store i32 %".74", i32* %".69"
  ret i32 0
}
