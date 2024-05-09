; ModuleID = ""

%"struct.ListNode" = type {i32, %"struct.ListNode"*}
declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

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
  %".19" = bitcast [3 x i8]* @"133b01da-34d5-46f7-9c85-5bff3aa5fe60" to i8*
  %".20" = load %"struct.ListNode", %"struct.ListNode"* %"node1"
  %".21" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node1", i32 0, i32 0
  %".22" = load i32, i32* %".21"
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".22")
  ; C Syntax: node2.next_ptr->value = 3;
  ; C Syntax: node2.next_ptr->value
  %".26" = load %"struct.ListNode", %"struct.ListNode"* %"node2"
  %".27" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node2", i32 0, i32 1
  %".28" = load %"struct.ListNode"*, %"struct.ListNode"** %".27"
  %".29" = load %"struct.ListNode", %"struct.ListNode"* %".28"
  %".30" = getelementptr %"struct.ListNode", %"struct.ListNode"* %".28", i32 0, i32 0
  %".31" = load i32, i32* %".30"
  ; C Syntax: 3
  store i32 3, i32* %".30"
  ; C Syntax: printf("%d", node1.value);
  ; C Syntax: printf("%d", node1.value)
  %".36" = bitcast [3 x i8]* @"2304092e-d3ab-497e-b99c-660f08702564" to i8*
  %".37" = load %"struct.ListNode", %"struct.ListNode"* %"node1"
  %".38" = getelementptr %"struct.ListNode", %"struct.ListNode"* %"node1", i32 0, i32 0
  %".39" = load i32, i32* %".38"
  %".40" = call i32 (i8*, ...) @"printf"(i8* %".36", i32 %".39")
  ret i32 0
}

@"133b01da-34d5-46f7-9c85-5bff3aa5fe60" = constant [3 x i8] c"%d\00"
@"2304092e-d3ab-497e-b99c-660f08702564" = constant [3 x i8] c"%d\00"