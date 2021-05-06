class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        Return all the power sets without duplicate subsets
        """
        res = []
        nums.sort()
        
        def dfs(idx, path):
            res.append(path)
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i]==nums[i-1]:
                    continue
                dfs(i+1, path + [nums[i]])
        
        dfs(0, [])
        return res
        """
        res = [[]] -> dfs(1, [] + [1]) res = [[], [1]] -> ....
                   -> dfs(2, [] + [2]) res = [[], [2]]  
                   -> continue
        """

if __name__ == '__main__':
    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums))