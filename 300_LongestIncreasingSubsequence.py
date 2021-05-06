import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Brute force / DFS with cache O(2^N)
        # Every element has two options of being part of the subsequence or not 
        
        # Dynamic Programming (Sub-probleming) / O(n^2) nested for loop , O(n) dp space complexity
        """
        - the longest increasing subsequene possible upto ith index is independent of the elements which
        will come later on in the array
        - At each index, check the maximum length of increasing subsequence up until ith index
        - then use the info to find max length including i+1th index
            - dp[i] = max(dp[i], 1 + dp[j] (0 <= j < i) )

        Checking 
        nums [10, 9, 2, 5, 3, 7, 101, 18]
        dp   [1,  1, 1, 1, 1, 1,  1,   1]

        at index = 1: 9 < 10
        at index = 2: 2 < 10
                      2 < 9
        at index = 3: 5 < 10
                      5 < 9
                      5 < 2
                      ...
        """

        """
        if not nums:
            return 0

        dp = [1] * len(nums)
        # outer iteration for i index
        for i in range(1, len(nums)):
            # compare all the index to i index element 
            for j in range(i):
                if nums[i] > nums[j]: 
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
        """

        # Dynamic Programming with binary search / O(nlogn) binary search n times, O(n) dp space complexity
        # By using binary search, we can find the correct insertion position
        """
        if not nums:
            return 0

        dp = [nums[0]] # in order to store the increasing subsequent
        # at all the index, try to find 
        for i in range(1, len(nums)):
            left, right = 0, len(dp)-1
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid

            if dp[left] < nums[i]:
                dp.append(nums[i])
            else:
                dp[left] = nums[i]
        return len(dp)
        """

        dp = []
        for element in nums:
            # find the leftmost index where the element could be inserted while having the list sorted
            index = bisect.bisect_left(dp, element)
            # if the index is at the last
            if index == len(dp):
                # getting smaller number which is yet bigger than the one already in it
                dp.append(element)
            # having the smallest value on left 
            else:
                dp[index] = element
        return len(dp)

if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))