from _DATATYPES import TreeNode
#Question: Traverse a tree level by level in a zig zag order
#Solution: Typical Breadth First Search (BFS) but keep track of zigzag
#Difficulty: Medium 

def zigzagLevelOrder(root):
        #If the root is null, return an empty list
        if not root: return []
        #Create variables r (result), q (queue), and c (current queue)
        r, q, c = [[]], [root], []
        #Keep track of if we're going left or right in our zigzag traversal
        zig = False
        #As long as the queue is not empty
        while q:
            #For each item in the queue
            for i in q:
                #Append item to the end of the result list
                r[-1] += [i.val]
                #If left and right children exist, add them to current queue in order of left to right
                if i.left: c += [i.left]
                if i.right: c += [i.right]
            #Reset queue to current queue and current queue to an empty list
            q, c = c, []
            #If we're going right to left, reverse the last item in our results list
            if zig:
                r[-1] = r[-1][::-1]
            #Negate out boolen so we go the opposite direction next time
            zig = not zig
            #If our queue still is non null, add an empty list to our result because we sill have entries to fill
            if q: r += [[]]
        return r