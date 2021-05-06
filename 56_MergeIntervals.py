class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        """ 
        intervals = [start, end]
        - Sort with the starting time
        - So that I can check the overlapping intervals: finish(i) > start(i+1)
        - if contiguous intervals are overlapping, then merge into one interval with
        [start i, finish i+1] 
        - then done
        """
        # O(nlogn) / O(n) - Python built in sorting (Merge Sort) requires O(n) space complexity as well
        if not intervals:
            return []
        # sort the intervals with the start time
        intervals = sorted(intervals, key = lambda x:x[0])
        
        # to avoid index out of range use while, i, n
        i, n = 0, len(intervals)
        while i < n-1:
            # if they overlap - we can merge this two consecutive intervals
            if intervals[i][1] >= intervals[i+1][0]:
                # then I should delete one interval and update the other interval
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                del (intervals[i+1])
                # if delete one interval from the intervals then decrement the length and the pointer
                n -= 1
                i -= 1
            i += 1

        return intervals

if __name__ == '__main__':
    intervals = [[1,4],[0,2],[3,5]]
    print(Solution().merge(intervals))