class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        last = [1]
        for i in xrange(1, rowIndex + 1):
            tmp = [1]
            for j in xrange(1, i):
                tmp.append(last[j - 1] + last[j])
            tmp.append(1)
            last = tmp
        return last
print Solution().getRow(3)