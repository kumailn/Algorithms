def sol(t):
  def helper(r, l):
    if not r.left and not r.right: 
      print(l + [r.val])
    if r.left: 
      l.append(r.val)
      helper(r.left, l)
      if l: del l[-1]
    if r.right:
      l.append(r.val)
      helper(r.right, l)
      if l: del l[-1]
  l = []
  helper(t, l)
  return 
    
def main():
  a = TreeNode("A")
  a.left = TreeNode("B")
  a.right = TreeNode("C")
  a.left.left = TreeNode("E")
  a.left.right = TreeNode("F")
  a.right.left = TreeNode("D")
  a.right.right = TreeNode("G")
  sol(a)
  
main()




          A
  B             C
  
D    E     F        G

A->B->D PRINT ABD
