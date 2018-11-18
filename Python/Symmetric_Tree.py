from _DATATYPES import *

#Question: Determine if a tree is symmetric
#Solution: Recursively call mirroring nodes
#Difficulty: Easy


def isSymmetric(root):
    #If node is null then tree is symmetric
    if not root: return True
    #Define resursive helper function that takes in two nodes and compares their values
    def help(l, r):
        #If both nodes are null return True (this is a base case)
        if not l and not r: return True
        #If only one of the nodes is null return false as tree is imbalanced, or values of aren't the same (another base case)
        if not l or not r or l.val != r.val: return False
        #Otherwise call same function on the inner two nodes (lefts right and rights left) and outer two nodes (rights right and lefts left)
        return help(l.left, r.right) and help(l.right, r.left)
    #Call helper on the first pair of children
    return help(root.left, root.right)
    
