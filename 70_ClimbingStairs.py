class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Dynamic Progamming with Top-Down Approach with Memoization 
        # when n == 1 and n == 2 base condition stored in dp array
        # keep augmenting the elements into and return the last node 
        # O(n) time / O(n+1) Spce

        if n == 1:
            return 1
        elif n == 2:
            return 2

        dp_memo = [0] * (n+1)
        dp_memo[1] = 1
        dp_memo[2] = 2
    
        for i in range(3, len(dp_memo)):   
            dp_memo[i] = dp_memo[i-1] + dp_memo[i-2]   

        return dp_memo[n]

if __name__ == '__main__':
    n = 4
    print(Solution().climbStairs(n))
