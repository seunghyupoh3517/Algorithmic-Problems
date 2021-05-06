class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Built in sorting algorihm takes O(nlogn) time / space O(n) 
        # Without using the sorting algorithm
        """
        nums1 = nums1[:m] + nums2
        nums1.sort()

        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()
        """

        # Pointers from the beginning O(n+m) / O(m)
        """
        nums1_copy = nums1[:m]
        p1, p2 = 0, 0
        for p in range(n+m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
        """

        # Pointers from the end (O(n+m)) / O(1)
        p1, p2 = m-1, n-1
        # 1 2 3 | p1 0 0 0 p
        # 2 5 6 | p2

        for p in range(n+m-1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p]  = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

        return nums1

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    print(Solution().merge(nums1,m,nums2,n))