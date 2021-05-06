class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS O(N*M) / constant space 
        def dfs(grid, row, column):
            # Have to check all four directions - beware of boundary
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] != '1':
                return
            grid[row][column] = '0'
            dfs(grid, row-1, column)
            dfs(grid, row+1, column)
            dfs(grid, row, column-1)
            dfs(grid, row, column+1)

        M = len(grid)
        N = len(grid[0])
        island = 0
        # Using DFS on 1s and update the grid
        for row in range(M):
            for column in range(N):
                if grid[row][column] == '1':
                    dfs(grid, row, column)
                # With updated grid, we can increment the island whenever we run dfs
                # 1s will be substitute with 0s
                    island += 1
        
        return island


if __name__ == '__main__':
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]
    print(Solution().numIslands(grid))