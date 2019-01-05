import '_DATATYPES.dart';

List<int> inorder(TreeNode root) {
  List<int> depthFirst(TreeNode root, List<int> order) {
    if (root.left != null) depthFirst(root.left, order);
    order.add(root.val);
    if (root.right != null) depthFirst(root.right, order);
    return order;
  }
  return depthFirst(root, []);
}

List<int> inorder2(TreeNode root){
  List<TreeNode> stack = [];
  List<int> result = [];
  while(stack.isNotEmpty || root != null) {
    if (root != null) {
      stack.add(root);
      root = root.left;
    }
    else{
      TreeNode top = stack.removeLast();
      result.add(top.val);
      root = top.right;
    }
  }
  return result;
}

main(List<String> args) {
  var node = new TreeNode(5);
  node.left = TreeNode(3);
  node.left.right = TreeNode(4);
  node.right = TreeNode(7);

  print(inorder(node));
  print(inorder2(node));
}