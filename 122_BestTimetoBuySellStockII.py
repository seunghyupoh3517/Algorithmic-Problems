class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # O(n) / O(1)
        """ Multiple transcation is allowed, buy sell can't be done simultaneously
        Keep adding the profit obtained from every consecutive transaction  
        profit = sell - buy 

                 7 1 5 3 4 6
        profit:  0 0 4 0 1 2 sum = 7

        Why would sum of consecutive transaction profit can be the maximum?
            1 10 8 20
            b      s = 19
            b s b  s = 9 + 12 = 21 
            no matter how big difference is between 20 and 1, adding all the difference would be bigger
        """
        profit, max_profit = 0, 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = prices[i] - prices[i-1]
                max_profit += profit
        return max_profit

if __name__ == '__main__':
    prices = [1,2,3,4,7]
    print(Solution().maxProfit(prices))