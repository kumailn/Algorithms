import './_DATATYPES.dart';

ListNode addNums(ListNode l1, ListNode l2) {
  dynamic val1, val2, carry;
  ListNode number = ListNode(null);
  ListNode origin = number;
  val1 = l1.val;  
  val2 = l2.val;
  carry = 0;
  while(l1 != null || l2 != null ||carry != 0){
    if(l1 != null) val1 = l1.val;
    else val1 = 0;

    if(l2 != null) val2 = l2.val;
    else val2 = 0;

    number.next = ListNode((val1 + val2 + carry) % 10);
    carry = (val1 + val2 + carry) ~/ 10;
    number = number.next;
  }
  return origin.next;
}
 
void main() {
  var a = ListNode(1);

  var b = ListNode(4);

  print(addNums(a, b));
}