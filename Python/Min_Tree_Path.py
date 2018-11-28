#Question: Given a tree (Not necessairly a BST), determing the shortest path of any complete branch, where the values of the node determine the path lengths 
#

def get_cheapest_cost(rootNode):
  minval = float('inf')
  def helper(root, minval):
    if not root.children: return 0
    for i in root.children:
      val = i.cost + helper(i, minval)
      if val < minval: minval = val
    return minval
  return helper(rootNode, minval)