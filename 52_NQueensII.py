class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []
        def backtracking(queens):
            if len(queens) == n:
                temp = []
                for queen in queens:
                    string = '.' * queen + 'Q' + '.' * (n-1-queen)
                    temp.append(string)
                result.append(temp)
                return 

            for queen in getPosition(queens):
                backtracking(queens + [queen])


        def getPosition(queens):
            exclude = set()
            rows = len(queens)
            for row in range(rows):
                queen = queens[row]
                exclude.add(queen)
                exclude.add(queen + rows - row)
                exclude.add(queen - rows + row)

            return set(range(n)) - exclude


        backtracking([])
        return len(result)