class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        # Try to place the Q in each row in possible columns
        # if there is no place to place Q then return to previous step 
        # if number of placement == n, then create output string 
        def backtracking(queens):
            # represent Q placement in list: index - row, value - column 
            # i.e. [1,3,2,0] row:0 column:1 - row:1 column:3 - row:2 column:2 - row:3 column:0
            if len(queens) == n:
                # generate output string and update result
                temp = []
                for queen in queens:
                    row = '.' * queen + 'Q' + '.' * (n-1-queen)
                    temp.append(row)
                result.append(temp)
                return 

            # Need to place the queen
            for queen in getPosition(queens):
                backtracking(queens + [queen]) # placement of column 

        # find possible column to place Q / limit the same column, diagonal
        def getPosition(queens):
            exclude = set() # limited on the column 
            rows = len(queens) # length of queens represent which row currently at
            # then check all the restriction from all the Q I have placed from the first row to current row
            for row in range(rows):
                queen = queens[row]
                # column
                exclude.add(queen)
                # diagonal 
                exclude.add(queen + rows - row)
                exclude.add(queen - rows + row)

            return set(range(n)) - exclude

        backtracking([])
        return result

        # Backtracking O(N!)
        """
        1) Start in the leftmost column - place queens one by one in different columns
        2) If all queens are place: return True
        3) Try all rows in the current column
           Perform followings for every tried row
            - If queen can be placed in the row then mark [row, column] as part of the solution
            - recursively check if placing queen leads to a solution                      ^ 
            - if placing the queen in [row, column] leads to a solution, return True      |
            - if not, unmark [row, column] (backtrack) and go back to first step ----------
        4) If all rows have been tried and nothing worked: return False, trigger backtracking
        """

        
        def isValid(location, queens):
            row, col = location
            for queen in queens:
                x, y = queen
                if abs(row - x) == abs(col - y):
                    return False
                if row == x or col == y:
                    return False
            return True

        def solve(matrix, n, column, queens, result):
            if column == n:
                result.append([''.join(reversed(row)) for row in matrix])
                return True
            
            for i in range(n):
                r = False
                if isValid((i, column), queens):
                    matrix[i][column] = 'Q'
                    queens.append((i, column))
                    r = solve(matrix, n, column + 1, queens, result) or r
                    matrix[i][column] = '.'
                    queens.remove((i, column))
            return r

        matrix = [["." for _ in range(n)] for _ in range(n)]
        queens, result = [], []
        solve(matrix, n, 0, queens, result)

        return result
        


        
if __name__ == '__main__':
    n = 4
    print(Solution().solveNQueens(n))