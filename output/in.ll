; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: struct ListNode node1 = {1, 0};
  %"node1" = alloca %"struct.ListNode"
  ; C Syntax: {1, 0}
  ; C Syntax: 1
  %".5" = insertvalue %"struct.ListNode" zeroinitializer, i32 1, 0
  ; C Syntax: 0
  %".7" = insertvalue %"struct.ListNode" %".5", %"struct.ListNode"* null, 1
  store %"struct.ListNode" %".7", %"struct.ListNode"* %"node1"
  ; C Syntax: struct ListNode node2 = {3, &node1};
  %"node2" = alloca %"struct.ListNode"
  ; C Syntax: {3, &node1}
  ; C Syntax: 3
  %".12" = insertvalue %"struct.ListNode" zeroinitializer, i32 3, 0
  ; C Syntax: &node1
  %".14" = load %"struct.ListNode", %"struct.ListNode"* %"node1"
  %".15" = insertvalue %"struct.ListNode" %".12", %"struct.ListNode"* %"node1", 1
  store %"struct.ListNode" %".15", %"struct.ListNode"* %"node2"
  ; C Syntax: printf("%d", (*node2.next_ptr).value);
  ; C Syntax: printf("%d", (*node2.next_ptr).value)
  ; C Syntax: (*node2.next_ptr).value
  ; C Syntax: *node2.next_ptr
  %".21" = load %"struct.ListNode", %"struct.ListNode"* %"node2"
  %".22" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node2", i32 0, i32 1
  %".23" = load %"struct.ListNode"*, %"struct.ListNode"** %".22"
  %".24" = load %"struct.ListNode", %"struct.ListNode"* %".23"
  %".25" = getelementptr %"struct.ListNode", %"struct.ListNode"* %".23", i32 0, i32 0
  %".26" = load i32, i32* %".25"
  %".27" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_11_4" to i8*), i32 %".26")
  ; C Syntax: printf("%d", node1.value);
  ; C Syntax: printf("%d", node1.value)
  ; C Syntax: node1.value
  %".31" = load %"struct.ListNode", %"struct.ListNode"* %"node1"
  %".32" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node1", i32 0, i32 0
  %".33" = load i32, i32* %".32"
  %".34" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_12_4" to i8*), i32 %".33")
  ; C Syntax: (*node2.next_ptr).value = 3;
  ; C Syntax: (*node2.next_ptr).value
  ; C Syntax: *node2.next_ptr
  %".38" = load %"struct.ListNode", %"struct.ListNode"* %"node2"
  %".39" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node2", i32 0, i32 1
  %".40" = load %"struct.ListNode"*, %"struct.ListNode"** %".39"
  %".41" = load %"struct.ListNode", %"struct.ListNode"* %".40"
  %".42" = getelementptr %"struct.ListNode", %"struct.ListNode"* %".40", i32 0, i32 0
  %".43" = load i32, i32* %".42"
  ; C Syntax: 3
  store i32 3, i32* %".42"
  ; C Syntax: printf("%d", (*node2.next_ptr).value);
  ; C Syntax: printf("%d", (*node2.next_ptr).value)
  ; C Syntax: (*node2.next_ptr).value
  ; C Syntax: *node2.next_ptr
  %".50" = load %"struct.ListNode", %"struct.ListNode"* %"node2"
  %".51" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node2", i32 0, i32 1
  %".52" = load %"struct.ListNode"*, %"struct.ListNode"** %".51"
  %".53" = load %"struct.ListNode", %"struct.ListNode"* %".52"
  %".54" = getelementptr %"struct.ListNode", %"struct.ListNode"* %".52", i32 0, i32 0
  %".55" = load i32, i32* %".54"
  %".56" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_14_4" to i8*), i32 %".55")
  ; C Syntax: printf("%d", node1.value);
  ; C Syntax: printf("%d", node1.value)
  ; C Syntax: node1.value
  %".60" = load %"struct.ListNode", %"struct.ListNode"* %"node1"
  %".61" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node1", i32 0, i32 0
  %".62" = load i32, i32* %".61"
  %".63" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_15_4" to i8*), i32 %".62")
  ret i32 0
}

@"printf_format_11_4" = internal constant [3 x i8] c"%d\00"
@"printf_format_12_4" = internal constant [3 x i8] c"%d\00"
@"printf_format_14_4" = internal constant [3 x i8] c"%d\00"
@"printf_format_15_4" = internal constant [3 x i8] c"%d\00"