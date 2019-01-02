#Question: Given the number of nodes in a graph and the edges, determing if the graph is also a tree
#Solution: Determine if the graph has any clycles in it (using union-find), if it does, it can't be a tree
#Difficulty: Medium

def validTree(n, edges):
    #Create a list where each item is the parent of itself
    parent = list(range(n))
    #Helper function to find the greatest parent of a node
    def findParent(x): 
        #If the node is it's own parent return itself, otherwise find parent of parent[node]
        return x if parent[x] is x else findParent(parent[x])
    for edge in edges:
        #x is parent of edge_from y is parent of edge_to
        x, y = findParent(edge[0]), findParent(edge[1])
        #If both the edge_from and edge_to have the same parent they create a cycle that goes from edge_from to parent to edge_to, so the graph can't be a tree
        if x is y: return False
        #Otherwise set the parent of the edge_from to be edge_to, note you could also do this the other way around
        parent[x] = y
    #Make sure that number of edges is 1 less than number of nodes to ensure nothing is in a cycle, and no less, otherwise there will be multiple trees
    #(Because if we had 2 nodes and 2 edges, there would be a cycle, so ensure there is no cycle the number of edges is 1 less than the number of nodes)
    return len(edges) == n - 1

def main():
    a = [[0,1], [0,2], [0,3], [1,4]]
    an = 5

    b = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    bn = 5

    print(validTree(an, a))
    print(validTree(bn, b))
main()