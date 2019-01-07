#Question: Given a list of course prerequisites, determine if it is possible to complete all the courses
#Solution: Determine if the graph has a Cycle

def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites: return True
        graph = {i:[] for i in list(range(numCourses))}
        for x, y in prerequisites: graph[y] += [x]
        def depthFirst(current, unvisited, visiting, completelyVisited, graph):
            visiting.add(current); unvisited.remove(current)
            for neighbor in graph[current]:
                if  neighbor in completelyVisited: continue
                if neighbor in visiting: return True
                if depthFirst(neighbor, unvisited, visiting, completelyVisited, graph): return True
            completelyVisited.add(current); visiting.remove(current)
            return False
            
        unvisited = list(range(numCourses))
        visiting = set()
        completelyVisited = set()
        while unvisited:
            currentNode = unvisited[0]
            if depthFirst(currentNode, unvisited, visiting, completelyVisited, graph): return False
        return True