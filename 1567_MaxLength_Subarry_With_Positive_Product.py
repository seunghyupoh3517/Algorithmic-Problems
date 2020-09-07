"""https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
Return the maximum length of a subarray with positive product.

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

Input: nums = [-1,2]
Output: 1

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4
"""
# substring, subarray != subset
# substring, subarray only refers to contiguous elements, continous
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use Dynamic Programming to keep track of max length of subarray ending with index i with positive or negative product => dp[2] : dp[0] = pos, dp[1] = neg
        # 0 represents at index i, its not pos, not neg
        
        n = len(nums)
        dp = [0] * 2

        # if first element
        if nums[0] > 0:
            dp[0] = 1
        elif nums[0] < 0:
            dp[1] = 1

        count = dp[0] # count when positive product
        for i in range(1, n): # first index counted already
            curr = nums[i]
            temp = [0] * 2
            # three cases(previous current = result product): pos pos = pos, pos neg or neg pos = neg, neg neg = pos
            if curr > 0:
                # pos pos = pos
                temp[0] = dp[0] + 1
                # neg pos = neg
                if dp[1] > 0: 
                    temp[1] = max(temp[1], dp[1] + 1) 

            elif curr < 0:
                # pos neg = neg
                temp[1] = dp[0] + 1
                # neg neg = pos
                if dp[1] > 0: 
                    temp[0] = max(temp[0], dp[1] + 1)
            dp = temp
            count = max(count, dp[0])

        return count

if __name__ == '__main__':
    nums = [1,-2,-3,4]
    print(Solution().getMaxLen(nums))
    nums = [0,1,-2,-3,-4]
    print(Solution().getMaxLen(nums))
    nums = [-1,-2,-3,0,1]
    print(Solution().getMaxLen(nums))
    nums = [-1,2]
    print(Solution().getMaxLen(nums))
    nums = [1,2,3,5,-6,4,0,10]
    print(Solution().getMaxLen(nums))


