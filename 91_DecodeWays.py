class Solution(object):
    def numDecodings(self, s):
        """
        s = "226" n = 3
             2 2 6 s[0] + s[1] + s[2] 
             2 26  s[0] + s[1:3]
             22 6  s[0:2] + s[2]
        
        s = "06"
             x    -> if s[0] == '0' x check the first index because even if there is consecutive
                     number after 0, 0 still wouldn't count as char, it would have done counted into
                  -> '0' always have to come ahead with '1' or '2'
                  
        From the example above, there will be overlapping subproblems to compute and in order to 
        compute efficiently, I can think of storing the result of subproblems using memoization.
        And after I compute to prior subproblem from the left index, I will recursively call the 
        helper function with updated index and count the total number of possible output.
            -> send to index + 1, index + 2 since each char could be 1 or 2 digts of numbers
            
            result += 1
            - when reach to the end of the s, index == n - 1
        """
        n = len(s)
        if not s or s[0] == '0':
            return 0
        
        memo = [-float('inf')] * (n+1)
        def dp(index, s):
            # Base condtion
            if memo[index] >= 0:
                return memo[index]
            
            if index == n:
                return 1 
            
            if s[index] == '0':
                return 0
            
                # already checked whether it's 0 or not 
            if index == n-1:
                return 1
            
            # Sending to +1 or +2 updated indices
            ans = dp(index+1, s) 
            if int(s[index:index+2]) <= 26:
                ans += dp(index+2,s)
            memo[index] = ans
            # return the final count
            return ans
        
        return dp(0, s)
            