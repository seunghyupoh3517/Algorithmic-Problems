class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # DFS: We can vvisit every connected node to with DFS
        # - keep track of nodes that have been visited
        # - increment province as DFS represent a connected components
        
        province = 0
        # in order to keep track of visited vertices - no duplicate
        visited = set()

        def helper(node):
            for vertex, check in enumerate(isConnected[node]):
                # check == 1 connected, == 0 not connected
                if check and vertex not in visited:
                    visited.add(vertex)
                    helper(vertex)

        # check each inner nested list which is representation of each vertex
        for i in range(len(isConnected)):
            if i not in visited:
                # update the visited using DFS 
                helper(i)
                province += 1

        return province

        
if __name__ == '__main__':
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))