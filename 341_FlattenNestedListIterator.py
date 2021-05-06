# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    
    def __init__(self, nestedList):
        # we can flatten the nested list first in here
        def flatten(nl):
            temp = []
            for i in nl:
                if i.isInteger():
                    temp.append(i.getInteger())
                else:
                    temp.extend(flatten(i.getList()))
            return temp
        
        self.n = deque(flatten(nestedList))
        
        
    def next(self):
        return self.n.popleft()

    def hasNext(self):
        return self.n

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())




