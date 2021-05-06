class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Cascadng O(N 2^N) / O(N 2^N)
        """
        [ [] ]
        [ [] [1] ]
        [ [] [1] [2] [1, 2] ]
        [ [] [1] [2] [1, 2] [3] [1, 3] [2, 3] [1, 2, 3] ]
        
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]

        return output
        """

        # Backtrackng O(N 2^N) / O(N)
        """
        1 2 3 iterate over all possible length from 0 to n
        subsets of length 1: 1    /  2   /    3 
        subsets of length 2: 1 2  /  2 3 / 1  3
        subsets of length 3: 1 2 3
        """
    
        def backtrack(first, curr):
            # if the combination is done, legth of subsets
            if len(curr) == k:
                output.append(curr[:])
                return 
            # backtracking applies when the subset is complete
            # pop it and try other element
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n+1):
            # sending to the backtracking to find the subsets of all the length
            # length 0, 1, 2, 3
            backtrack(0, []) 

        return output

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))
