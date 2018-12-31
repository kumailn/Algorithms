
class TreeNode {
  dynamic val;
  TreeNode left, right;
  TreeNode(this.val);

  @override
    String toString() {
      return val.toString();
    }
}

class ListNode {
  dynamic val;
  ListNode next;
  ListNode(this.val);

  @override
    String toString() {
      return val.toString();
    }
}