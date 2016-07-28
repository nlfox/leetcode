class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board = [list(i) for i in board]
        # row
        for i in xrange(9):
            d = {}
            for j in xrange(9):
                if board[i][j] != ".":
                    if board[i][j] in d:
                        return False
                    else:
                        d[board[i][j]] = True
        for i in xrange(9):
            d = {}
            for j in xrange(9):
                if board[j][i] != ".":
                    if board[j][i] in d:
                        return False
                    else:
                        d[board[j][i]] = True
        for si,sj in [(i,j) for i in [0,3,6] for j in [0,3,6]]:
            d = {}
            for i in xrange(3):
                for j in xrange(3):
                    if board[si+j][sj+i] != ".":
                        if board[si+j][sj+i] in d:
                            return False
                        else:
                            d[board[si+j][sj+i]] = True
        return True