
def distance(nodes, pointFrom, pointTo):
    graph = {i:[] for i in list(set([n for m in nodes for n in m]))}
    for x, y in nodes: graph[x] += [y]; graph[y] += [x]

    queue, currentQueue, visited = [pointFrom], [], []

    count = 1

    while queue:
        for node in queue:
            visited += [node]
            currentQueue += [adjacentNode for adjacentNode in graph[node] if adjacentNode not in visited]
            if pointTo in currentQueue: return count
        count += 1
        queue, currentQueue = currentQueue, []

    return count    

print(distance([['A', 'B'], ['C', 'F'], ['B', 'F']], 'A', 'C'))