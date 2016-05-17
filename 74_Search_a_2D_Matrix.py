class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowLen = len(matrix[0])
        rowCount = len(matrix)
        idx = 0
        flag = False
        for i in xrange(rowCount):
            if matrix[i][0] <= target:
                idx = i
                flag = True
        if flag == False:
            return False

        low = 0
        high = rowLen - 1
        while low <= high:
            mid = (low + high) / 2
            if target == matrix[idx][mid]:
                return True
            else:
                if target < matrix[idx][mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False


print Solution().searchMatrix([
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 12)
