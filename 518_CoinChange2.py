class Solution(object):
    def change(self, amount, coins):
        # Dynamic programming O(N_lengthofCoinsArray X amount) Time - / O(amount) Space
        # If combination not possible 0 
        """
            amount = 5, coins = [1, 2, 5]
            output = 4 
                        5
                    -1       -2      -5
                    4       3        0

                -1  -2    -1  -2
                3   2     2   1

            -1  -2  -1  -2
            2   1   1   0

            - At each amount, we have at most 3 choices and can dedcut the amount of choices
            - Overlapping sub-amounts, can save computing time if we saved the result of sub problems
            - Memoizaton 

        If total amount is 0 then 1, no coins

        """
        if not coins: # amount == 0 there is one way (not choosing)
            return 0

        memo = [0] * (amount + 1)
        memo[0] = 1
        for coin in coins:
            # for each coin till amount => adding up combinations with each coins,
            # first with 1 coins, second with 1,2 coins, third, wiith 1,2,5 coins
            for i in range(coin, amount+1):
                memo[i] += memo[i - coin]
                print(memo[i])
       
        return memo[amount]


    
if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))



