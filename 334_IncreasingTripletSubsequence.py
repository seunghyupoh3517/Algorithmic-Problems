import math
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # With constraints of O(n) time / O(1) space
        """
        Linear scan 
            - while linearing scanning all the values
            1) Find the smallest number
            2) Find the second smallest number
            3) if there's a number bigger than those two, then true
        """
        n = len(nums)
        if n < 3:
            return False
        
        first, second = math.inf, math.inf
        for num in nums:
            # first smallest number
            if num <= first: # Even though first can be changed to non-smallest index but
                # the fact that there was a smallest num with smallest index doesn't change
                first = num
            # second smallest number
            elif num <= second:
                second = num
            # biggest number
            else:
                return True


        return False

    #[20, 100, 10, 12, 5, 13]
if __name__ == '__main__':
    nums = [20, 100, 10, 12, 5, 13]
    print(Solution().increasingTriplet(nums))