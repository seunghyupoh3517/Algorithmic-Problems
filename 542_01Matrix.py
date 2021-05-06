from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        # BFS approach
        """
        From 0 in each cell, we don't need to update the matrix 
        With nested for loop iteration, when we find cell containing 1, we can apply BFS on those cells
        """
        
        R, C = len(matrix), len(matrix[0])
        queue = deque()
        visited = set()
        # Instead invoking BFS for each 1 cell, flip the problem to start from 0 to get to closest 1
        # => This allows to run a single BFS that emerges from different places, all 0 in the matrix
        # => so first all the 0 and distance in the queue and append to visited
        # if not visited, they are all 1 cell
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))


        while queue:
            r, c, d = queue.popleft()
            # in four directions
            for nr, nc in ((r-1,c), (r,c-1), (r+1,c), (r,c+1)):
                # boundary check and when on 1 cell and if its not visited
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == 1 and (nr, nc) not in visited:
                    matrix[nr][nc] = d + 1
                    queue.append((nr, nc, d+1))
                    visited.add((nr, nc))

        return  matrix
        # O(r, c) / O(r, c)

if __name__ == '__main__':
    input = [
                [0,0,0],
                [0,1,0],
                [1,1,1]
            ]

    print(Solution().updateMatrix(input))