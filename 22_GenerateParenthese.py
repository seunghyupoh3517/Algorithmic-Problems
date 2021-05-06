class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Backtracking
        # Only add when we know the string will be remain valid
        # Keep tracking the number of openning and closing brackets
        # Check the condition and pass with appended (, ) to next backtracking
        # Pruning is with two conditions to validate
        result = []
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(''.join(s))
                return 
            
            if left < n:
                s.append('(')
                backtrack(s, left+1, right)
                s.pop()

            if right < left:   
                s.append(')')
                backtrack(s, left, right+1)
                s.pop()

        backtrack([], 0, 0)
        return result

if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))