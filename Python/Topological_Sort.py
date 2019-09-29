from typing import List

def topSort(numEdges: int, edges: List[int]) -> List[int]:
    graph = {}
    def depthFirst(current, visited, visitedNodes, graph):
        visited.add(current)
        for edge in graph[current]:
            if not (edge in visited):
                depthFirst(edge, visited, visitedNodes, graph)
        visitedNodes.append(current)

    # Populate the graph
    for i in range(numEdges): graph[i] = []
    for x, y in edges: graph[y] = [x]

    visited = set(); result = []
    for node in graph:
        if not (node in visited):
            visitedNodes = []
            depthFirst(node, visited, visitedNodes, graph)
            for node2 in visitedNodes: result.insert(0, node2)
    return result

def main():
    graph = [[0, 5], [5, 0], [0, 4], [1, 4], [2, 5], [3, 2], [1, 3]]
    print(topSort(6, graph))

main()