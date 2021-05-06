class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # DFS (Recursion) + Memoization
        """ 
        (i) at each node, can go four directions, left, right, up, down
            - cannot go over the boundary 
            - can strictly go to increasing node
        (ii) path has to be the longest path 
        
        i.e.    9 9 4     at each node can do 1 + max(up, down, left, right)
                6 6 8 =>  path of from greatest to smallest, decreasing path
                2 1 1         
                output = 4 [1,2,6,9]
        """
        if not matrix or not matrix[0]:
            return 0
        
        # numbers of row - column, numbers of column - row, memoization to avoid solving overlapped subproblem 
        N, M = len(matrix), len(matrix[0])
        memo = [[0] * M for i in range(N)]

        def dfs(row, column):
            # if the node not visited 
            if not memo[row][column]:
                # then need to find the direction, decresing node - comparison
                value = matrix[row][column]
                
            # Search directions to go decreasing path and check boundaries
            
                # up
                if row-1 >= 0 and value > matrix[row-1][column]:
                    up = dfs(row-1, column)
                else:
                    up = 0
                # down
                if row+1 < N and value > matrix[row+1][column]:
                    down = dfs(row+1, column)
                else: 
                    down = 0
                # left
                if column-1 >= 0 and value > matrix[row][column-1]:
                    left = dfs(row, column-1)
                else:
                    left = 0
                # right
                if column+1 < M and value > matrix[row][column+1]:
                    right = dfs(row, column+1)
                else: 
                    right = 0

                memo[row][column] = 1 + max(up, down, left, right)
            return memo[row][column]
            

        res = []
        for i in range(N):
            for j in range(M):
                res.append(dfs(i, j))

        return max(res)

if __name__ == '__main__':
    matrix = [[1,2]]
    print(Solution().longestIncreasingPath(matrix))