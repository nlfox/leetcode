class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix[0])
        height = len(matrix)
        row_to_del = [False] * height
        col_to_del = [False] * width
        for i, arr in enumerate(matrix):
            for j, val in enumerate(arr):
                if val == 0:
                    row_to_del[i] = True
                    col_to_del[j] = True
        for i, v in enumerate(row_to_del):
            if v:
                matrix[i] = [0] * width
        for i, v in enumerate(col_to_del):
            if v:
                for j in xrange(height):
                    matrix[j][i] = 0
