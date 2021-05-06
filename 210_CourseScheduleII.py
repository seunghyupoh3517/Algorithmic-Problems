from collections import defaultdict, deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # Topological order - Not fully optimized
        """
        def topologicalSort(vertex, visited, stack):
            visited[vertex] = True
            for neighbor in neighbors[vertex]:
                if visited[neighbor] == False:
                    topologicalSort(neighbor, visited, stack)
            stack.insert(0, vertex)

        def detectCycle(stack):
            for i in range(numCourses):
                for neighbor in neighbors[i]:
                    pointer = 0 if i not in stack else stack.index(i)
                    pointed = 0 if neighbor not in stack else stack.index(neighbor)
                    # if pointer appears later than pointed then there exists cycle
                    if pointer > pointed:
                        return True
            return False

        neighbors = defaultdict(list)
        for pair in prerequisites:
            if pair[0] == pair[1]:
                return []
            neighbors[pair[1]].append(pair[0])
        
        visited = [False] * numCourses
        stack = []
        for i in range(numCourses):
            if visited[i] == False:
                topologicalSort(i, visited, stack)
        
        # if there is cycle, returned True -> cannot finish course == False
        # if there is no cycle, returned False -> can finish course == True
        if not detectCycle(stack):
            return stack
        else:
            return []
        """

        # O(V + E) / O(V + E) Node Indegree - Outgoing degree
        ind = [[] for _ in range(numCourses)]
        outd = [0] * numCourses
        
        for pre in prerequisites:
            if pre[0] == pre[1]:
                return []
            ind[pre[1]].append(pre[0])
            outd[pre[0]] +=  1
                  
        result, courses = [], deque()
        for i in range(numCourses):
            if outd[i] == 0:
                courses.append(i)
        
        while courses:
            course = courses.popleft()
            result.append(course)
            for i in ind[course]:
                outd[i] -= 1
                if outd[i] == 0:
                    courses.append(i)
        # if there exists cycle (i.e. [0,1] [1,0] can't be done), then it can't be done
        # so need sanity check if the order is finalized
        return result if len(result) == numCourses else []

        """
        The first node in the topological ordering will be the node that doesn't have any incoming edges 
        - Any node that has an in-degree of 0 can start topologically sorted order

        => First process all the nodes/courses with 0 in-degree implying no prerequisite course required.
           Remove all these courses from the graph, along with their outgoing edges, we can find out the courses that should be processed next
           Continuously do this until all the courses have been accounted for 
        """


if __name__ == '__main__':
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    print(Solution().findOrder(numCourses, prerequisites))
        

        