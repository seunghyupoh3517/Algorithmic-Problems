# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
    
        """ O(nlogn) n: all numbers of intervals / O(n)
        Each employee has non-overlapping, sorted intervals - one employee can have multiple intervals, all intervals not yet sorted
        Return the common, positive free time in sorted order
        schedule = [
                    [[1,2],[5,6]],
                    [[1,3]],
                    [[4,10]]
                    ]
            1) Flatten out the schedule first
            2) then merge all the intervals
            3) return the gap in the intervals - before the min start time, after the max end time could be achieved
        """

        sch = []
        for employee in schedule:
            for interval in employee:
                sch.append((interval.start, interval.end))
        # sort the flatten schedule with start time
        sch.sort()

        n, i = len(sch), 0
        # merge the overlapping intervals, end i > start i+1
        while  i < n-1:
            if sch[i].end >= sch[i+1].start:
                sch[i].end = (sch[i].end if sch[i].end >= sch[i+1].end else sch[i+1].end)
                del(sch[i+1])
                n -= 1
                i -= 1
            i+=1
        
        # find the gap in the intervals
        res = []
        for i in range(len(sch)-1):
            res.append((sch[i].end, sch[i+1].start))

        return res

if __name__ == '__main__':

    schedule = [
                    [[1,3],[6,7]],
                    [[2,4]],
                    [[2,5],[9,12]]
                ]
    sch = []
    """
    for employee in schedule:
        for interval in employee:
            sch.append([interval[0],interval[1]])
    sch.sort()
    
    n, i = len(sch), 0
        # merge the overlapping intervals, end i > start i+1
    while  i < n-1:
        if sch[i][1] >= sch[i+1][0]:
            sch[i][1] = (sch[i][1]  if sch[i][1] >= sch[i+1][1] else sch[i+1][1])
            del(sch[i+1])
            n -= 1
            i -= 1
        i+=1
    
    res = []
    for i in range(len(sch)-1):
        res.append((sch[i][1], sch[i+1][0]))
    print(res)
    """
    