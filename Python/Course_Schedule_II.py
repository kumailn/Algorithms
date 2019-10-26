# Question(#210): Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# Difficulty: Medium
# What do I learn from this question? How to implement a general topological sort with cycle checking

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
    # Construct the graph by creating a map where each course maps to a list of its prereqs
    graph = {course: [] for course in range(numCourses)}
    for a, b in prerequisites: graph[a] += [b]
    
    def depthFirst(course, visiting):
        nonlocal order, graph, visited
        
        # If we've fully visited the course before we can skip it, if we were visiting it 
        # and have come across it again then we know there was a cycle, so return False
        if course in visited: return True
        if course in visiting: return False
        
        # This is where the DFS starts, so we indicate we are now visiting the current node
        visiting.add(course)
        
        # For every course in the prereq of the current course, we conduct a DFS again, returning
        # false if our DFS detects a cycle
        for prereq in graph[course]:
            if not depthFirst(prereq, visiting): return False
        
        # We now add the current course to visited, indicating we've traversed all it's prereqs
        # We also add the current course to order, because the first time we reach here in our 
        # recursion stack will be when we reach a course with no prerequisutes
        visited.add(course)
        order += [course]
        return True
    
    visited, order = set(), []
    
    # Run our DFS on every node in the graph, since our DFS actually returns a boolean 
    # we can embed cycle checking in the DFS itself and based on that return an empty list 
    # if a cycle exists in the graph
    for course in graph:
        if not (depthFirst(course, set())): return []
        
    return order
        