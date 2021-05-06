class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Math O(n)
        """
        in each move: increment 1 on (n-1) elements -> make all elements equal
            - increment (n-1) elements is same as decrement 1 element
            - need to decrement each maximum value to minimum value
            - iterate to make num to minimum, result += (num - minimum)
        """
        if min(nums)==max(nums):
            return 0

        res = 0
        minimum = min(nums)
        for num in nums:
                add  = num - minimum
                res += add
        return res

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().minMoves(nums))