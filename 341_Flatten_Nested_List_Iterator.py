# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
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
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.arr = []
        self.parseNested(nestedList)
        self.max = len(self.arr)
        self.cur = 0

    def parseNested(self, nestedList):
        for i in nestedList:
            if i.isInteger():
                self.arr.append(i.getInteger())
            else:
                self.parseNested(i.getList())

    def next(self):
        """
        :rtype: int
        """
        res = self.arr[self.cur]
        self.cur += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if (self.cur >= self.max):
            return False
        return True

        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())