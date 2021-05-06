class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Brute Force O(n^2) / O(1) space
        """
        prices = 7 1 5 3 4 6
                 0 1 2 3 4 5 6
        dp[] = maximum difference on the index
        dp = [0 -1 5 1 3 2]
        find the maximumm difference of each element
        """

        """
        n = len(prices)
        max_diff = 0
        for i in range(n-1):
            for j in range(i+1, n):
                diff = prices[j] - prices[i]
                max_diff = max(max_diff, diff)
        return max_diff
        """

        # One pass O(n) / O(1) 
        """
                    7 1 5 3 4 6
        min_price = 7 1 1 1 1 1
        max_profit= 0 0 4 4 4 5
        """

        """
        min_price, max_profit = float('inf'), 0
        for num in prices:
            if num < min_price:
                min_price = num
            elif num - min_price > max_profit:
                max_profit = num - min_price
        return max_profit
        """

        # Dynamic Programming / O(n) time, O(1) Space
        """
        DP depending on the previous profit, profit[today] = prices[today] - prices[previous day] // calculates the profit of difference between today and yesterday
                                                           + profit[yesterday] // calculates the maximum profit have earned until yesterday
        Today we sell, profit = today's trading profit                                   
                      7 1 5 3 4 6
        profit      =   0 4 2 3 5
        max_profit  =   0 4 4 4 5
        prev_profit =   0 4 2 3 5
        """
        max_profit, prev_profit = 0, 0
        for i in range(1, len(prices)):
            profit = max(prices[i] - prices[i-1] + prev_profit, 0)
            max_profit = max(max_profit, profit)
            prev_profit = profit

        return max_profit

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 4, 6]
    print(Solution().maxProfit(prices))