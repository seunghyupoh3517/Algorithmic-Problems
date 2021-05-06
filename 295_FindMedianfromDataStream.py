import heapq
class MedianFinder(object):
    # Min heap + Max heap 
    """ 
    Maintain the sorted order in the list, then sort the incoming data from the data stream as well
        - Median value (in list size even: mean of two middle value, odd: middle value)
    
    """

    def __init__(self):
        self.minheap = heapq()
        self.maxheap = heapq()

    def addNum(self, num):
        

    def findMedian(self):
        


    # Follow up
    """
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

    """