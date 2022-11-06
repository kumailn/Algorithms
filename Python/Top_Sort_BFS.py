from typing import List
from collections import defaultdict


def topSort(numNodes: int, edges: List[int]) -> List[int]:
    graph = defaultdict(list)
    # indegrees is simply the number of incoming arrows at each node
    indegrees = {}
    result = []

    for pre, nxt in edges:
        graph[pre].append(nxt)
        if pre not in indegrees: indegrees[pre] = 0
        if nxt not in indegrees: indegrees[nxt] = 0
        indegrees[nxt] += 1

    # get all nodes with 0 incoming edges, we know these have no prerequisites and so we can start with them
    queue = [node for node in indegrees if indegrees[node] == 0]

    while queue:
        node = queue.pop()
        result.append(node)

        # go through all nodes that depend on the current node and decrement their indegrees by 1
        # because the current node is being removed from the graph
        for nxt in graph[node]:
            indegrees[nxt] -= 1
            # if a nodes indegrees ever becomes 0 we know it has no more dependencies left in the graph, enqueue it
            if indegrees[nxt] == 0: queue.append(nxt)

    # if we don't have exactly the all the nodes in the output, there was a cycle somewhere
    return result if len(result) == numNodes else None

def main():
    graph = [["A", "B"], ["B", "C"], ["C", "D"], ["B", "G"]]
    print(topSort(5, graph))

main()
