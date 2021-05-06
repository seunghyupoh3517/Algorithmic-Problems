class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        stack = []
        def dfs(temp):
            if len(temp) == len(nums):
                stack.append(temp)
                return
            
            
            \
        



       dfs([])
       return stack
        
if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permute(nums))