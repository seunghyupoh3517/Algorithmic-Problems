class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # O(n) / O(n)
        """
        - making two array of containing all the left sum and right sum 
        - if there are matching sum then that's the pivot index, otherwise, -1
        0  1  8  11 17 22
        27 20 17 11 6  0
        """

        """
        if not nums:
            return -1

        n, sum = len(nums), 0
        left, right = [0] * n,  [0] * n
        for i in range(1, n):
            sum += nums[i-1]
            left[i] = sum
        

        sum = 0
        for i in range(n-2,-1,-1):
            sum += nums[i+1]
            right[i]= sum
        

        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1
        """

        # O(n) / O(1)
        """
        Using the total sum and do the comparison while iterating the nums
        """
        total_sum, l_sum = sum(nums), 0
        for i, val in enumerate(nums):
            if l_sum == total_sum - val - l_sum:
                return i 
            l_sum += val
        return -1    
        

if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    print(Solution().pivotIndex(nums))