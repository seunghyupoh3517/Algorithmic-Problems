import functools
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        
        # Dynamic Programming 
        """
        Split jobdifficulty into #d of subarrays and find the min of sum of the largest integers in each subarray.
        We compute  all the combinations

        [6, 5, 4, 3, 2] d = 3 -> directed ayaclic graph and we can use dynamic programming recursion approach
        #1      #2      #3    day1 6, 2days 5432 - day1 6, day2 5, day3 432 / day1 6, day2 54, day3 32
        6       5       4     day1 65, 2days 432
        65      54      43    day1 654, 2days 32
        654     543     432   ...
        6543    5432         
        65432           3
                4       32
                43    
                432     2

                3
                32

                2   
   
        Ans = dp(d, 0)
        Dp(d,i):from ith job, find the minimum sum of max value in each d# of subarrays
        Guess: find maximum value from the ssubarray
        Recurrence: min( max(jobdifficulty[j:n-d+1] + dp(d-1,j+1)) )
                    # number of days
                    for i in range(0, n-d+1) 
                        for j in range(i, n-d+1)
        """

        # Dynamic Programming Top down approach with memoization O(n^2d) / O(nd)
        
        numjobs = len(jobDifficulty)
        if numjobs < d:
            return -1

        memo = {}
        def dp(days, cut):
            print(days, cut)
            # if its already in memo, retrieve the subproblem result
            if (days, cut) in memo:
                return memo[(days, cut)]
            # if one day left to consider, then the maximum difficulty of the array
            if days == 1: 
                return max(jobDifficulty[cut:]) # to find the minimum sum
            
            maxsofar = 0
            answer = float('inf')
            # numjobs - day + 1 have left days with one each job which means putting upuntil the maximum jobs in a day
            for i in range(cut, numjobs - days + 1):
                maxsofar = max(jobDifficulty[i], maxsofar)
                # day - 1 since one day is filled with the answer
                # j + 1 now we have put that job into the days, no longer in consideraion, next
                answer = min(answer, maxsofar + dp(days-1, i+1))

            memo[(days, cut)] = answer
            return answer
    
        return dp(d,0)    
        

        # Using LRU cache instead of memoization - import functools
        """
        numjobs = len(jobDifficulty)
        if numjobs < d:
            return -1

        @functools.lru_cache
        def dp(days, cut):
            # if one day left to consider, then the maximum difficulty of the array
            if days == 1: 
                return max(jobDifficulty[cut:]) # to find the minimum sum
            
            maxsofar = 0
            answer = float('inf')
            # numjobs - day + 1 have left days with one each job which means putting upuntil the maximum jobs in a day
            for i in range(cut, numjobs - days + 1):
                maxsofar = max(jobDifficulty[i], maxsofar)
                # day - 1 since one day is filled with the answer
                # j + 1 now we have put that job into the days, no longer in consideraion, next
                answer = min(answer, maxsofar + dp(days-1, i+1))
            return answer

        return dp(d,0)
        """

        # Bottom up approach
        """
        numjobs = len(jobDifficulty)
        if numjobs < d:
            return -1

        dp = [[float('inf')] * numjobs + [0] for i in range(d+1)]

        for day in range(1, d+1):
            right = numjobs - day + 1
            for cut in range(right):
                maxsofar = 0
                answer  = float('inf')
                for i in range(cut, right):
                    maxsofar = max(maxsofar, jobDifficulty[i])
                    answer = min(answer, maxsofar + dp[day-1][i+1])
                dp[day][cut] = answer

        return dp[d][0]
        """
        
if __name__ == '__main__':
        jobDifficulty = [6,5,4,3,2,1]
        d = 3
        print(Solution().minDifficulty(jobDifficulty, d))