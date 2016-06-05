class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<=0:
            return []
        tri = [[1]]
        numRows-=1
        for i in xrange(1, numRows + 1):
            tri.append([1])
            for j in xrange(1,i):
                tri[i].append(tri[i - 1][j - 1] +tri[i - 1][j])
            tri[i].append(1)
        return tri


print Solution().generate(2)
