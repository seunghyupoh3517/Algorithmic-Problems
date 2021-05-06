class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Without Time constraints O(N) Time / O(1) Space
        # O(n) / O(n)
        """ 
        Without time complexity, I can solve it with dictionary
        
        dictionary = Counter(nums)
        return max(dictionary, key = dictionary.get)
        """

        # With Time constraints O(N) Time / O(1) Space
        """ Boyer-Moore Voting Algorithm
            - Since the majortiy element exists - checking whether the 
            majority is more than n/2
        """
        counter, candidate = 0, None
        for num in nums:
            # choose the candidate
            if counter == 0:
                candidate = num
            # if the current number is the candidate 
            # then increment the candidate, else decrement
            # and if the counter == 0, change the candidate
            if candidate == num:
                counter += 1
            else:
                counter -= 1
        return candidate

if __name__ == '__main__':
    nums = [3,3,4]
    print(Solution().majorityElement(nums))

