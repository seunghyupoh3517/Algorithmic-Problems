class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # O(2^n) time / O(1) space - Brute force 
        # Finding all the positive integers from 1, smallest positive integer
        """
        res = 1
        for i in range(len(nums)):
            if res not in nums:
                return res
            else:
                res += 1
        return res
        """

        # Finding right index to right value == finding value it's right index O(n) / O(1)
        # i.e. index 2 to have value 2, index 3 to have value 3
        # if there's non-corresponding value in index, that's the smallest missing positive integer
        """
        val    -1 2  1  3  4 6
        index   1 2  3  4  5 6
        ->      1 2 -1  3  4 5
        ->      1 2  3 -1  4 6 
        ->      1 2  3  4 -1 6
        ->      1 2  3  4 -1 6 then all the value is in right index except the missing smallest positivie integer
        """
        n = len(nums)
        for i in range(n): # will have from 1 to n + 1
            # index0: 1, index1: 2,  index2: 3 ...
            #  this will be correct position index if the nums[i] have correct value for it
            correctPosition = nums[i] - 1 
            # ignore the value that is out of boundaries
            # keep swaping - sending the value to its index unless the value is out of boundary
            while 1 <= nums[i] <= n and nums[i] != nums[correctPosition]:
                nums[i], nums[correctPosition] = nums[correctPosition], nums[i]
                correctPosition = nums[i] - 1
        
        # Return the first value that is not corresponding to the index 
        for i in range(n):
            if nums[i] != (i+1):
                return i+1

        # If not returned anything, all the smallest possible within the nums length is cotained
        # then return the next positive value
        return n + 1

if __name__ == '__main__':
    nums = [-1, 2, 1, 3, 4, 6]
    print(Solution().firstMissingPositive(nums))
    