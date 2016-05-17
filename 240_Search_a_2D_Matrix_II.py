class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowLen = len(matrix[0])
        rowCount = len(matrix)
        startList = []
        for i in xrange(rowCount):
            if matrix[i][0] < target:
                startList.append(i)
            elif matrix[i][0] == target:
                return True
        flag = False
        for i in startList:
            if matrix[i][rowLen - 1] < target:
                startList[i] = "-1"
                flag = True
        if flag:
            startList.remove(-1)
        print startList
        for i in startList:
            low = 0
            high = rowLen - 1
            while low <= high:
                mid = (low + high) / 2
                if target == matrix[i][mid]:
                    return True
                else:
                    if target < matrix[i][mid]:
                        high = mid - 1
                    else:
                        low = mid + 1

        return False


print Solution().searchMatrix([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 5)
