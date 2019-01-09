from _DATATYPES import TreeNode
#Question: Traverse a tree level by level
#Solution: Typical Breadth First Search (BFS)
#Difficulty: Easy

def levelOrder(root):
        #Return empty list if the root node is null
        if not root: return []
        #vaiable to hold final result, queue of nodes and current level of tree
        order, queue, nextQueue = [], [root], []
        #While the queue is not empty
        while queue:
            #For every node in the queue
            for node in range(len(queue)):
                #If that node has a left child, append to current list, then same for right child
                if queue[node].left: nextQueue += [queue[node].left]
                if queue[node].right: nextQueue += [queue[node].right]
            #Now we append the current queue to the order (the lambda is just there to turn the TreeNode objects to their values)
            order += [list(map(lambda x: x.val, queue))]
            queue, nextQueue = nextQueue, []
        return order
        
def main():
    tree = TreeNode(6)
    tree.left = TreeNode(3)
    tree.right = TreeNode(12)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(14)

    print(levelOrder(tree))

main()
