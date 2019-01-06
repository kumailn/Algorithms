def hasCycle(edges, numEdges):
    #Initialize a graph that stores the neighbor of each node
    graph = {i:[] for i in list(range(numEdges))}
    #Populate the graph so that the 'children' of each node are stored with the parent as the key
    for x, y in edges: graph[x] += [y]
    #Create three sets, one to store all unvisited nodes, one to store nodes curently visiting, one to store completely visited ones
    unvisited = list(range(numEdges))
    visiting = set()
    completelyVisited = set()
    
    #While we still have nodes that are unvisited
    while unvisited:
        #We graph a random node from the unvisited collection to run a DFS on
        currentNode = unvisited[0]
        #If a call to the depth first seach returns true then we know this graph has a cycle and can return true
        if depthFirstSearch(currentNode, unvisited, visiting, completelyVisited, graph): return True
    #If no call to the depth first search returns true then we can return False that there is no cycle in this graph
    return False

#Define our helper depth first search for a cycle
def depthFirstSearch(currentNode, unvisited, visiting, completelyVisited, graph):
        #Firstly, we need to move the current node we're at from unvisited and to visiting
        unvisited.remove(currentNode)
        visiting.add(currentNode)
        #Now for each of this nodes adjacent neighbors we need to run this DFS again
        for neighbor in graph[currentNode]:
            #If that neighbor has already been completely visited, we can skip tis particular neighbor
            if neighbor in completelyVisited: continue
            #If this neighbor is already a node we're visiting then return true that this has a cycle! Because we've circled back to a parent node
            if neighbor in visiting: return True
            #If any its neighbors have a cycle return true as well
            if depthFirstSearch(neighbor, unvisited, visiting, completelyVisited, graph): return True
        #Finally remove this current node from visiting and add it to completely visited
        visiting.remove(currentNode)
        completelyVisited.add(currentNode)

def main():
    print(hasCycle([[1, 0], [0, 2]], 3))

main()