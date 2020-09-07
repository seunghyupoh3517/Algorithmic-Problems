""" https://leetcode.com/problems/sort-colors/
A.K.A. Dutch National Flag Problem Solution
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
class Solution(object):
    def sortColors(self, nums, start, end):
        # move current pointer along the array and swap with pointer to 0 and 2 - 0 to the front, 2 to the last
        # this algorithm only applies to this particular setup of the problem, three flags where we can ignore 1
        # idea: choose two lowest, highest value of flag along the array once then pass it to the recursive call with updated pointers p0, p2
        # p0 + #lowest value, p2 - #highest value
        if not(start == end - 1):
            p0, p2 = self.idea(nums, start, end)
            self.sortColors(nums, p0, p2)
        
    def idea(self, nums, start, end):
        curr = 0
        p0 = start
        p2 = end

        if(p0 == 0):
            compare1 = 0
        elif(p0 == 2):
            compare1 = 1

        if(p2 == 9):
            compare2 = 4
        elif(p2 == 7):
            compare2 = 3

        while curr <= p2:
            if nums[curr] == compare1:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == compare2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

        return p0, p2

        """
        Orignial Solution for the Original Problem
        def sortColors(self, nums):
            p0 = curr = 0
            p2 = len(nums) - 1
            while curr <= p2:
                if nums[curr] == compare1:
                    nums[p0], nums[curr] = nums[curr], nums[p0]
                    p0 += 1
                    curr += 1
                elif nums[curr] == compare2:
                    nums[curr], nums[p2] = nums[p2], nums[curr]
                    p2 -= 1
                else:
                    curr += 1
        """
if __name__ == '__main__':
    nums = [2,0,4,1,1,0,3,3,4,2]
    start = 0
    end = len(nums) - 1
    print(nums)
    Solution().sortColors(nums, start, end)
    print(nums)
