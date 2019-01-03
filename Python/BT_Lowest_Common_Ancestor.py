from _DATATYPES import TreeNode
#Question: Find the lowest common ancestor of two nodes
#Solution: Use a recursive approach to look for both nodes, return null, left or right at each recrusive level
#Difficulty: Easy
#Time Complexity: O(n)

def LCA(root, p, q):
    #If we have found p or q to be the root, or the root is null, return the root
    if not root or root == p or root == q: return root
    #Recursively travel left and then right until we find p or q or null
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    #Return the root if we both left and right aren't null, else return the one thats not null
    return root if left and right else left or right

def main():
    a = TreeNode(6)
    a.left = TreeNode(4)
    a.left.left = TreeNode(3)
    a.left.right = TreeNode(5)
    a.right = TreeNode(7)

    p = a.left.left
    q = a.left.right

    print(LCA(a, p, q).val)

main()