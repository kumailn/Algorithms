import 'dart:math';
import './_DATATYPES.dart';

num bstDepth(TreeNode root) {
  if (root == null) return 0;
  return 1 + max(bstDepth(root.left), bstDepth(root.right));
}

void main() {
  var a = TreeNode(1);
  a.left = TreeNode(2);
  a.right = TreeNode(3);
  a.left.left = TreeNode(4);
  
  print(bstDepth(a));
}