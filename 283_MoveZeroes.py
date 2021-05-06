class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # del, insert method can take more time complexity, O(n^2) / O(1) space 
        """
        idx = 0
        for counter, num in enumerate(nums):
            if num != 0:
                del nums[counter]
                nums.insert(idx, num)
                idx += 1
        return nums
        """

        # O(n) / O(1)
        # keeping track of index of 0 value - then swap with non 0 value
        zero = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

        return nums


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes(nums))