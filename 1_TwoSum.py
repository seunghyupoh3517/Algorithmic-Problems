class Solution(object):
    # excatly one solution, not use the same element twice
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Brute force 
        """
        output = []
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    return output
                else:
                    j+=1
        O(n^2)
        """

        # Using Dictionary (== hash table)
        # O(n): Dictionary look up O(1) * n

        output = {}
        for counter, val in enumerate(nums):
            x = target - val
            if x in output:
                return [output[x], counter]
            else:
                output[val] = counter
                

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target))

        
        
