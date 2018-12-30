import './_DATATYPES.dart';

bool isValidBST(TreeNode root, {double maxVal = double.infinity, double minVal = double.negativeInfinity}) {
  if (root == null) return true;
  if (root.val >= maxVal || root.val <= minVal) return false;
  return isValidBST(root.left, maxVal: root.val, minVal: minVal) && isValidBST(root.right, minVal: root.val, maxVal: maxVal);
}

main(List<String> args) {
  TreeNode a = TreeNode(5.0);
  a.left = TreeNode(3.0);
  a.left.right = TreeNode(4.0);
  a.right = TreeNode(11.0);
  a.right.left = TreeNode(7.0);

  TreeNode b = TreeNode(5.0);
  b.left = TreeNode(4.0);

  print(isValidBST(a));
}