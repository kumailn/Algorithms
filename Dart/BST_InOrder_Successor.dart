import './_DATATYPES.dart';
//Question: Given the root node of a tree, find the in order successor of that node
//Solution: Find the first node that is not smaller than the given one
//Difficulty: Easy

TreeNode inorderSuccessor(TreeNode root, TreeNode p){
    if (root == null) return null;
    dynamic successor = null;
    while (root != null){
      if (root.val > p.val) {
        successor = root;
        root = root.left;
      } 
      else root = root.right;
    }
    return successor;
}

main(List<String> args) {
  var a = TreeNode(6);
    a.left = TreeNode(4);
    a.left.right = TreeNode(5);
    a.left.left = TreeNode(3);
    print(inorderSuccessor(a, TreeNode(4)));
}