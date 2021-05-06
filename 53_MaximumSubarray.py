class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Dynamic Programming O(n) / O(1)
        """
        In order to find the largest sum, will have to check all the sum and keep update the maximum sum
        
        for i = 1:
            curr = max(1, 1+2) = 3 / is currnt or adding new element bigger
            max = max(3, 1) = 3 / is new result or current max bigger
            ....
        At each index decide which is bigger
            - current element or
            - previous subarray + current element  -> previous subarray dp
        then keep track of the maximum sum
        """

        """
        curr_subarray, max_subarray = nums[0], nums[0]
        for num in nums[1:]:
            # which would be better, starting with new element or adding the next element
            curr_subarray = max(num, curr_subarray + num)
            max_subarray = max(curr_subarray, max_subarray)

        return max_subarray
        """

        # Divide and Conquer O(nlogn) / O(logn)
        """
        Split up the input into smallr chunk till they are small enough to solve then
        combine the solution to get the final overall solution
        Divide - left side subarray
               - right side subarray
               - combination of elements from the both sides
        """
        
        def backtracking(nums, left, right):
            if left > right:
                return float('-inf')
            
            curr_subarray, left_sum, right_sum = 0,0,0
            mid = (left+right)//2

            # from mid to left part, elements from the left side
            for i in range(mid-1, left-1, -1):
                curr_subarray += nums[i]
                left_sum = max(curr_subarray, left_sum)

            # from mid to right part, elements from the right side
            curr_subarray = 0
            for i in range(mid+1, right+1):         
                curr_subarray += nums[i]
                right_sum = max(curr_subarray, right_sum)   
            
            # the maximum subarray contained elements from the both side - connected to the middle
            combined_sum = nums[mid] + left_sum + right_sum

            # find the best left half, right half sum
            left_half = backtracking(nums, left, mid-1)
            right_half = backtracking(nums, mid+1, right)

            return max(left_half, right_half, combined_sum)

        res = backtracking(nums, 0, len(nums)-1)
        return res

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))