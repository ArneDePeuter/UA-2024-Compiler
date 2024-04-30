; ModuleID = ""

%"struct.ListNode" = type {i32, %"struct.ListNode"*}
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
  ; C Syntax: printf("%d", node1.value);
  ; C Syntax: printf("%d", node1.value)
  ; C Syntax: node1.value
  %".20" = load %"struct.ListNode", %"struct.ListNode"* %"node1"
  %".21" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node1", i32 0, i32 0
  %".22" = load i32, i32* %".21"
  %".23" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_10_4" to i8*), i32 %".22")
  ; C Syntax: (*node2.next_ptr).value = 3;
  ; C Syntax: (*node2.next_ptr).value
  ; C Syntax: *node2.next_ptr
  %".27" = load %"struct.ListNode", %"struct.ListNode"* %"node2"
  %".28" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node2", i32 0, i32 1
  %".29" = load %"struct.ListNode"*, %"struct.ListNode"** %".28"
  %".30" = load %"struct.ListNode", %"struct.ListNode"* %".29"
  %".31" = getelementptr %"struct.ListNode", %"struct.ListNode"* %".29", i32 0, i32 0
  %".32" = load i32, i32* %".31"
  ; C Syntax: 3
  store i32 3, i32* %".31"
  ; C Syntax: printf("%d", node1.value);
  ; C Syntax: printf("%d", node1.value)
  ; C Syntax: node1.value
  %".38" = load %"struct.ListNode", %"struct.ListNode"* %"node1"
  %".39" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node1", i32 0, i32 0
  %".40" = load i32, i32* %".39"
  %".41" = call i32 (i8*, ...) @"printf"(i8* bitcast ([3 x i8]* @"printf_format_12_4" to i8*), i32 %".40")
  ret i32 0
}

@"printf_format_10_4" = internal constant [3 x i8] c"%d\00"
@"printf_format_12_4" = internal constant [3 x i8] c"%d\00"