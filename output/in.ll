; ModuleID = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  ; C Syntax: char str1[5];
  %"str1" = alloca [5 x i8]
  store [5 x i8] zeroinitializer, [5 x i8]* %"str1"
  ; C Syntax: char str2[5];
  %"str2" = alloca [5 x i8]
  store [5 x i8] zeroinitializer, [5 x i8]* %"str2"
  ; C Syntax: printf("Enter first name and lastname: ");
  ; C Syntax: printf("Enter first name and lastname: ")
  %".8" = bitcast [32 x i8]* @"3ca9924a-4a39-46fb-9bcd-b6df02e64f8f" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8")
  ; C Syntax: scanf("%s %s", str1, str2);
  ; C Syntax: scanf("%s %s", str1, str2)
  %".12" = bitcast [6 x i8]* @"0f55629b-7552-46ee-9689-06c395092ec6" to i8*
  ; C Syntax: str1
  %".14" = getelementptr [5 x i8], [5 x i8]* %"str1", i32 0, i32 0
  ; C Syntax: str2
  %".16" = getelementptr [5 x i8], [5 x i8]* %"str2", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"scanf"(i8* %".12", i8* %".14", i8* %".16")
  ; C Syntax: printf("Hello %s %s\n", str1, str2);
  ; C Syntax: printf("Hello %s %s\n", str1, str2)
  %".20" = bitcast [13 x i8]* @"aaea4caa-8208-4e24-ad60-4b1dbd9dd1f1" to i8*
  ; C Syntax: str1
  %".22" = getelementptr [5 x i8], [5 x i8]* %"str1", i32 0, i32 0
  ; C Syntax: str2
  %".24" = getelementptr [5 x i8], [5 x i8]* %"str2", i32 0, i32 0
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".20", i8* %".22", i8* %".24")
  ; C Syntax: str1[0] = 'J';
  ; C Syntax: str1[0]
  ; C Syntax: 0
  %".29" = getelementptr [5 x i8], [5 x i8]* %"str1", i32 0, i32 0
  %".30" = load i8, i8* %".29"
  ; C Syntax: 'J'
  store i8 74, i8* %".29"
  ; C Syntax: printf("Hello %s %s\n", str1, str2);
  ; C Syntax: printf("Hello %s %s\n", str1, str2)
  %".35" = bitcast [13 x i8]* @"7a8ddeb2-4538-47c3-8df8-3416d4f7e561" to i8*
  ; C Syntax: str1
  %".37" = getelementptr [5 x i8], [5 x i8]* %"str1", i32 0, i32 0
  ; C Syntax: str2
  %".39" = getelementptr [5 x i8], [5 x i8]* %"str2", i32 0, i32 0
  %".40" = call i32 (i8*, ...) @"printf"(i8* %".35", i8* %".37", i8* %".39")
  ; C Syntax: return(0);
  ; C Syntax: (0)
  ret i32 0
}

@"3ca9924a-4a39-46fb-9bcd-b6df02e64f8f" = constant [32 x i8] c"Enter first name and lastname: \00"
@"0f55629b-7552-46ee-9689-06c395092ec6" = constant [6 x i8] c"%s %s\00"
@"aaea4caa-8208-4e24-ad60-4b1dbd9dd1f1" = constant [13 x i8] c"Hello %s %s\0a\00"
@"7a8ddeb2-4538-47c3-8df8-3416d4f7e561" = constant [13 x i8] c"Hello %s %s\0a\00"