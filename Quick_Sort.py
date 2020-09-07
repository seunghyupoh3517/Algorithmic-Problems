""" Quick Sort O(n^2)
Choose pivot as last index, low index as 0 and high index as n-2
While low index value < pivot - move low index to right, high index value > pivot - move high index to left
if they stop at where left value > pivot, high value < pivot then swap those two
Keep itereating those two steps until low = high, then swap that index with pivot 
"""
class Solution(object):
    def partition(self, nums, start, end):
        swap = end
        pivot = nums[swap]
        low = start
        high = end - 1
        
        while True:
            while(low <= high and nums[low] <= pivot):
                low += 1
            while(low <= high and nums[high] >= pivot):
                high -= 1
            if(low <= high):
                nums[low], nums[high] = nums[high], nums[low]
            else:
                break
        nums[swap], nums[low] = nums[low], nums[swap]

        return low
     

    def quickSort(self, nums, start, end):
        if start < end:
            p = Solution().partition(nums, start, end)
            self.quickSort(nums, start, p-1)
            self.quickSort(nums, p+1, end)
        
""" Randomized Quick Sort O(nlogn) 
Before doing quick sort, we randomly pick index m between 0 to (n-1). Then sawp with it Arr[0], Arr[m]. Then choose Arr[0] (which was Arr[m]) as pivot.
Then execute Quick sort, exactly same => by probablistic analysis, it can achieve O(nlogn). -> Mostly, to avoid when the input array is already sorted 
which will be the worst case and the randomized choice will have  the effect of rendering the worst case.
"""
import random
class RandomSolution(object):
    def randomPartition(self, nums, start, end):
        # random.randrange()
        randpivot = random.randrange(start, end)
        nums[start], nums[randpivot] = nums[randpivot], nums[start]
        return self.partition(nums, start ,end)

    def partition(self, nums, start, end):
        swap = end
        pivot = nums[swap]
        low = start
        high = end - 1
        
        while True:
            while(low <= high and nums[low] <= pivot):
                low += 1
            while(low <= high and nums[high] >= pivot):
                high -= 1
            if(low <= high):
                nums[low], nums[high] = nums[high], nums[low]
            else:
                break
        nums[swap], nums[low] = nums[low], nums[swap]

        return low
     
    
    def quickSort(self, nums, start, end):
        if start < end:
            p = RandomSolution().randomPartition(nums, start, end)
            self.quickSort(nums, start, p-1)
            self.quickSort(nums, p+1, end)

""" https://leetcode.com/problems/sort-an-array/discuss/277127/7-line-quicksort-to-write-in-interviews-python
Simple quick sort for the interviews - not super efficeint as we would use it in the production code but simple and logically great to explain it easily
As the space complexity can be O(n) or even to O(n^2) - Quicksort requires less space than Merge Sort; thus, not good way of doing this, not efficient but simple fast way to show that I know how quick sort can be done and how it could be done
with in-plcae quicksorting
"""
class Reference(object):
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        # random.choice() from the list, any sequences
        pivot = random.choice(nums)
        # left part list - element less than pivot / right partlist - element greater than pivot
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]

        return self.quicksort(lt) + eq + self.quicksort(gt)

if __name__ == '__main__':
    nums = [2,4,5,8,1,3,6,9,10,7] 
    n = len(nums)
    print(nums)
    Solution().quickSort(nums, 0, n-1)
    print(nums)

    print ('Randomized Quicksort')
    nums = [2,4,5,8,1,3,6,9,10,7]  
    print (nums)
    RandomSolution().quickSort(nums, 0, n-1)
    print (nums)

    print ('Reference')
    nums = [2,4,5,8,1,3,6,9,10,7]  
    print (nums)
    print(Reference().quicksort(nums))
    