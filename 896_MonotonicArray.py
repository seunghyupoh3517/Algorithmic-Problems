import math
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        # Can solve in one pass O(n) / O(1)
        # Just need to check it is monotonic, doesn't matter whether inc, dec
        inc, dec = True, True
        for i in range(len(A)-1):
            # monotonic increasing <-> strictly decreasing
            if A[i] > A[i+1]:
                inc = False
            # monotonic decreasing <-> strictly increasing
            if A[i] < A[i+1]:
                dec = False
        return (inc or dec)

if __name__ == '__main__':
    A = [1,2,2,3]
    print(Solution().isMonotonic(A))