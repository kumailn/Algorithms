#Question: Given the root of a tree, find the minimum dept the tree goes
#Solution: Use a BFS traversal to find the first leaf node of the tree
#Difficulty: Easy

def minDepth(root):
        #Define queue, current queue and a mindepth variable
        queue = [root]; current = []; mindepth = 0
        #If our current node is null, the depth is 0, so return 0
        if not root: return mindepth
        #As long as our queue exists
        while queue:
            #For every element in our queue
            for i in queue:
                #If we have reached a leaf node, we can return 1+mindepth
                if not i.left and not i.right: return mindepth + 1
                #Else we append the left and right children to our queue (See BFS traversal)
                if i.left: current.append(i.left)
                if i.right: current.append(i.right)
            #Set queue to current queue, current to empty list and add one to our mindepth because we're now on a new level
            queue = current
            current = []
            mindepth += 1
        return mindepth