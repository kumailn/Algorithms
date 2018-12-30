import './_DATATYPES.dart';

bool hasPathSum(TreeNode root, num sum) {
  List<num> allSums = [];
  void sumHelper(TreeNode root, num currentSum) {
    if (root.left == null && root.right == null) allSums.add(root.val + currentSum);
    if (root.left != null) sumHelper(root.left, currentSum + root.val);
    if (root.right != null) sumHelper(root.right, currentSum + root.val);
  }
  sumHelper(root, 0);
  return allSums.contains(sum);
}

main(List<String> args) {
  TreeNode a = TreeNode(5);
  a.left = TreeNode(3);
  a.right = TreeNode(3);

  print(hasPathSum(a, 8));
}