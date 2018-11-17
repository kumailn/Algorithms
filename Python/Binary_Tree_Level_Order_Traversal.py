#Question: Traverse a tree level by level
#Solution: Typical Breadth First Search (BFS)

def levelOrder(self, root):
        #Return empty list if the root node is null
        if not root: return []
        #vaiable to hold final result, queue of nodes and current level of tree
        r, q, c = [[]], [root], []
        #While the queue is not empty
        while q:
            #For every node in the queue
            for i in range(len(q)):
                #Append the node to the last list in the result list
                r[-1] += [q[i].val]
                #If that node has a left child, append to current list, then same for right child
                c = c + [q[i].left] if q[i].left else c
                c = c + [q[i].right] if q[i].right else c
            #Let queue be the current traversal level nodes, and current level resets to empty list
            q, c = c, []
            #Append empty list to result (for next level) if queue is non empty
            r = r + [[]] if q else r
        return r
        