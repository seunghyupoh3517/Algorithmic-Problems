""" https://leetcode.com/problems/subarray-product-less-than-k/
Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        # enumerate() adds a counter to an iterable and returs it in a form of enumerate object
        # the enumerate object can be used in for loops or converted into list of tuples
        # for index, value in enumearte(nums): index 0 value 10, index 1 value 5 ...
        """ Using BruteForce Power Set Enumeration -> Not correct for this problem
        if k < 1:
            return 0

        n = len(nums)
        p_n = pow(2,n)
        
        count = 0
        for i in range(1, p_n):
            numbers =[]
            sum = 1
            for j in range(n):
                if(i & (1 << j)):
                    sum = sum * nums[j]
                    numbers.append(nums[j])
            
            if sum < k:
                print(numbers)
                count += 1

        

        return count
        """
        
        # Subarray is different with the Subset, it only cotains contiguous elements
        # {1, 2, 3} => {1} {2} {3} {1,2} {2,3} {1,2,3}

        if k < 1:
            return 0
        # thinking it as a sliding window as subarray only takes contiguous elements
        # index - left + 1 contains all the subarray could've created within each window size

        product = 1
        count = left = 0
        for index, value in enumerate(nums):
            product *= value
            while product >= k:
                product /= nums[left]
                left +=1
            count += index - left + 1

        return count
        # O(n)

if __name__ == '__main__':
    k = 100
    nums = [10, 5, 2, 6]
    print(Solution().numSubarrayProductLessThanK(nums, k))