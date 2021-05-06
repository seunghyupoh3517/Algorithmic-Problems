from collections import defaultdict, deque
class Solution(object):
    def canFinish(self, numCourses,  prerequisites):
        """
        numCourses - # courses i have to take
        prerequisites[i] = [ai, bi] must take course bi first in order to take ai
        Return boolean whether we can finish all courses or not

        ex) num = 2, pre = [ [1, 0] ]
            True - take 0 and then 1

            num = 2, pre = [ [1, 0] [0, 1] ]
            False - take 0 and then 1, take 1 and then 0 which is impossible

            num = 5, pre = [ [1, 0], [2, 1], [3, 4], [3, 2]]
            True - take 0 1 2 4 3 

        # Topological Sorting 
            - Consider the prerequisites as directed edges
            - pre is pointing the course, pre has to come first
            - if topological sorting doesn't work, there is a cycle
            - perform topological sorting then detect cycle
            i.e. 0 -> 1, 1 -> 2, 4 -> 3, 2 -> 3   
        """
        def topologicalSort(index, visited, order):
            visited[index] = True
            for neighbor in neighbors[index]:
                if visited[neighbor] == False:
                    topologicalSort(neighbor, visited,order)
            order.insert(0, index)
        
        # [0, 1] [1, 2] [1, 3] order: 3 2 1 0 / 2 3 1 0
        # neighbor: [ [], [0], [1], [1] ]
        def detectCycle(order):
            for i in range(numCourses):
                for neighbor in neighbors[i]:
                    pointer = 0 if i not in order else order.index(i)
                    pointed = 0 if neighbor not in order else order.index(neighbor)
                
                # pointer should be in front of pointed in order not to have cycle
                    if pointer > pointed:
                         return True
            return False
        
        # Creating neighbor dictionary, visited list
        neighbors = defaultdict(list)
        visited = [False] * numCourses
        for pre in prerequisites:
            # Edge case - one cannot have oneself as prerequisite
            if pre[0] == pre[1]:
                return False
            neighbors[pre[1]].append(pre[0])
        
        # Topological sort and store sorting order
        order = []
        for i in range(numCourses):
            if visited[i] == False:
                topologicalSort(i, visited, order)
                
        # If the sorted order has cycle, then False, else True    
        return not detectCycle(order)

        

        # O(|E| + |V|) / O(|E| + |V|) : E = number of dependencies, V = number of courses
        """
        Take all the coures without any prerequisite first - repeat this step until there is no more courses
        and if the # of taken courses == numCourses, then true else false
            - list to keep track how many prerequisite courses each course has left
                - can prioritize to take course without any prerequisite, needed[course_i] == 0, then take it 
            - list of list to keep track of list of courses that requires course_i then after taking course_i, we can 
            deduct 1 from # of courses needed on the list of courses
            - need to keep track of what course is about to be taken and then check its list of list
            
        i.e. numCourses = 4 [0, 1] [1, 2] [1, 3]
        => list: [1, 2, 0, 0]
            for pre in prerequisites:
                if pre[0] == pre[1]: -> edge case, if one requires oneself, can never be done
                    return False
                list[pre[0]] += 1
                
        list of list:  [ [],[0],[1],[1] ]
            for pre in prerequisites:
                listoflist[pre[1]].append(pre[0])
        """

        """
        preCourse = [[] for _ in range(numCourses)]
        num_preCourse = [0] * numCourses 
        
        for pre in prerequisites:
            if pre[0] == pre[1]:
                return False
            preCourse[pre[1]].append(pre[0])
            num_preCourse[pre[0]] += 1
        
        # Course without prerequisite for the first
        takeCourse = deque()
        for i in range(numCourses):
            if num_preCourse[i] == 0:
                takeCourse.append(i)
                
        count = 0
        while takeCourse:
            # take the course
            course = takeCourse.popleft()
            count += 1
            
            for i in preCourse[course]:
                num_preCourse[i] -= 1
                if num_preCourse[i] == 0:
                    takeCourse.append(i)
        
        return count == numCourses
        """
        
if __name__ == '__main__':
    numCourses = 20
    prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    print(Solution().canFinish(numCourses, prerequisites))