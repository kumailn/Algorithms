import './_DATATYPES.dart';

bool isSymmetric(TreeNode root) {
  bool symmetricHelper(TreeNode left, TreeNode right) {
    if (left == null && right == null) return true;
    if (left == null || right == null) return false;
    return left.val == right.val ? true : false;
  }
  return symmetricHelper(root.left, root.right);
}

main(List<String> args) {
  TreeNode a = TreeNode(5);
  a.left = TreeNode(3);
  a.right = TreeNode(3);

  print(isSymmetric(a));
}