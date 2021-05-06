class Solution(object):
    def productExceptSelf(self, nums):
        # Without using division, solve in O(n) time, O(1) space
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Without restriction, O(n) time, O(n) space
        """
        result = []
        multi = 1
        for i in range(len(nums)):
            multi *= nums[i]
        for i in range(len(nums)):
            result.append(int(multi/nums[i]))
        return result
        """

        # With restriction - associating with two arrays L, R : all the value multiplied before, after i index, O(n) time, O(n) space
        """
        n = len(nums)
        L, R, result = [0] * n, [0] * n, [0] * n

        L[0] = 1
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]

        R[n-1] = 1
        for i in reversed(range(len(nums)-1)):
            R[i] = R[i+1] * nums[i+1]
            
        for i in range(len(nums)):
            result[i] = L[i] * R[i]
        return result
        """

        # + with O(1) space (output array doesn't add)
        n = len(nums)
        result = [0] * n
        
        result[0] = 1
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
        R = 1
        for i in reversed(range(n)):
            result[i] *= R
            R *= nums[i]
        
        return result
        

if __name__ == '__main__':

    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))