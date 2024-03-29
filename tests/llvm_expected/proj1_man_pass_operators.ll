; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  ; C Syntax: 1 + 1;
  %".3" = add i32 1, 1
  ; C Syntax: 0 - 6985;
  %".5" = sub i32 0, 6985
  ; C Syntax: 5 * 63;
  %".7" = mul i32 5, 63
  ; C Syntax: 99 / 3622;
  %".9" = sdiv i32 99, 3622
  ; C Syntax: 3 > 1;
  %".11" = icmp sgt i32 3, 1
  ; C Syntax: 3 < 1;
  %".13" = icmp slt i32 3, 1
  ; C Syntax: 8897 == 45647897;
  %".15" = icmp eq i32 8897, 45647897
  ; C Syntax: +487897;
  ; C Syntax: -5;
  %".18" = sub i32 0, 5
  ; C Syntax: 1 && 656;
  %".20" = and i32 1, 656
  ; C Syntax: 989 || 68779;
  %".22" = or i32 989, 68779
  ; C Syntax: !65465;
  %".24" = xor i32 65465, -1
  ; C Syntax: 1 + (3 * 6) / (1+ 3);
  %".26" = mul i32 3, 6
  %".27" = add i32 1, 3
  %".28" = sdiv i32 %".26", %".27"
  %".29" = add i32 1, %".28"
  ; C Syntax: 1+3+5*(62/3);
  %".31" = add i32 1, 3
  %".32" = sdiv i32 62, 3
  %".33" = mul i32 5, %".32"
  %".34" = add i32 %".31", %".33"
  ; C Syntax: 5 * +9;
  %".36" = mul i32 5, 9
  ; C Syntax: 33 * -5;
  %".38" = sub i32 0, 5
  %".39" = mul i32 33, %".38"
  ; C Syntax: ((-6)) * ((( 5 + 32 / (6532))));
  %".41" = sub i32 0, 6
  %".42" = sdiv i32 32, 6532
  %".43" = add i32 5, %".42"
  %".44" = mul i32 %".41", %".43"
  ; C Syntax: 1 >= 3;
  %".46" = icmp sge i32 1, 3
  ; C Syntax: 695 <= 44878;
  %".48" = icmp sle i32 695, 44878
  ; C Syntax: 98333 != 6565911;
  %".50" = icmp ne i32 98333, 6565911
  ; C Syntax: 55 % 963;
  %".52" = srem i32 55, 963
  ; C Syntax: 45 << 4;
  %".54" = shl i32 45, 4
  ; C Syntax: -33 >> -4;
  %".56" = sub i32 0, 33
  %".57" = sub i32 0, 4
  %".58" = ashr i32 %".56", %".57"
  ; C Syntax: 1 & 8784573;
  %".60" = and i32 1, 8784573
  ; C Syntax: 898 | 98;
  %".62" = or i32 898, 98
  ; C Syntax: !-97435345;
  %".64" = sub i32 0, 97435345
  %".65" = xor i32 %".64", -1
  ; C Syntax: 9787 ^ -9987;
  %".67" = sub i32 0, 9987
  %".68" = xor i32 9787, %".67"
  ret i32 0
}
