class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        nums = [1, 2, 3, 4]
        output = [1, 1+2, 1+2+3, 1+2+3+4]
        """ 
        # Brute force O(n^2) / O(1)
        """
        for i in range(len(nums)-1, -1, -1):
            sum = 0
            for j in range(i-1, -1,-1):
                sum += nums[j]
            nums[i] += sum
        return nums
        """

        # Linear O(n) / O(1)
        temp = nums[0]
        for i in range(1, len(nums)):
            nums[i] += temp
            temp = nums[i]

        return nums
if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().runningSum(nums))