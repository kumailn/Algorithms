def findOrder(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #Graph of courses directed to their prerequisites 
        prereqs = {i:[] for i in range(numCourses)}
        #Graph of courses pointing from prerequisites to next courses
        dependants = {i:[] for i in range(numCourses)}
        
        #Populate both graphs
        for x, y in prerequisites: 
            prereqs[x] += [y]
            dependants[y] += [x]
        
        #Initialize a stack populated with courses without any prerequisites
        stack = [course for course in range(numCourses) if not prereqs[course]]
        order = []

        #As long as the stack is not empty 
        while stack:
            #Remove the last course from the stack
            topCourse = stack.pop()
            #Add the course to the order list as this course has no prerequisites
            order += [topCourse]
            #Now we can go through all of this courses dependants (ie courses which are available to take after this one)
            for dependantCourse in dependants[topCourse]:
                #Remove top course from the prerequisite of the dependant course as it's already been added to our ordering
                prereqs[dependantCourse].remove(topCourse)
                #If dependant course has no unvisited prerequisites then add it to the stack 
                if not prereqs[dependantCourse]: stack += [dependantCourse]
            #Delete the topCourse rom the graph of prerequisites as all of its prerequisites must of been added to the stack now
            del prereqs[topCourse]
        #If the graph of prerequisites is not empty by now, then there is no order of courses that are possible to take 
        return order if not prereqs else []

def main():
    print(findOrder(4, [[1,0],[2,0],[3,1],[3,2], [0, 3]]))
        
main()