#Question: Given a list of courses and their prerequisites, and time needed to complete each course, find the min time to complete all courses
#Solution: Use Khans algorithm to perform a top sort, updating a store of time needed for each course, 
# the time for each course is the max of itself or the time needed to complete the previous course + time for this course
#Difficulty: Hard 

from typing import List
from collections import defaultdict

def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    indegrees = {}
    graph = defaultdict(list)
    timeToCourse = [0] + time
    
    for prev, nxt in relations:
        indegrees[prev] = 0
        indegrees[nxt] = 0
        
    for prev, nxt in relations:
        indegrees[nxt] += 1
        graph[prev].append(nxt)
                
    # get all courses without any prerequisites 
    q = [course for course, ins in indegrees.items() if ins == 0]

    while q:
        course = q.pop()
        for nxt in graph[course]:
            # time to the next course is either the max of itself (ie we got to the nxt course through another path in the graph), or this path, which is 
            # currentCourseTime + timeToPrevious course takes more time, the max of either is the bottleneck
            timeToCourse[nxt] = max(timeToCourse[nxt], timeToCourse[course] + time[nxt-1])
            indegrees[nxt] -= 1
            if indegrees[nxt] == 0: q.append(nxt)
            
    return max(timeToCourse)