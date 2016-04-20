import copy


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        dic = {}
        self.count = 0
        self.graph = {}
        width = len(board[0])
        length = len(board)
        self.wordLen = len(word)
        self.word = list(word)

        self.visited = [[0 for i in xrange(width)] for j in xrange(length)]
        self.board = [list(i) for i in board]
        for i in xrange(0, length):
            for j in xrange(0, width):
                self.graph[(i, j)] = []
                if (i > 0 and i <= length - 1):
                    self.graph[(i, j)].append((i - 1, j))
                if (i >= 0 and i < length - 1):
                    self.graph[(i, j)].append((i + 1, j))
                if (j > 0 and j <= width - 1):
                    self.graph[(i, j)].append((i, j - 1))
                if (j >= 0 and j < width - 1):
                    self.graph[(i, j)].append((i, j + 1))

                if dic.has_key(board[i][j]):
                    dic[board[i][j]].append((i, j))
                else:
                    dic[board[i][j]] = [(i, j)]
        if (dic.has_key(self.word[0])):
            for i in dic[self.word[0]]:
                self.visited[i[0]][i[1]] = 1
                if self.bfs(i[0], i[1], 0):
                    return True
                self.visited[i[0]][i[1]] = 0
        return False

    def bfs(self, x, y, count):
        count += 1
        if count >= self.wordLen:
            return True
        for i in self.graph[(x, y)]:
            if (self.board[i[0]][i[1]] == self.word[count] and self.visited[i[0]][i[1]] != 1):
                self.visited[i[0]][i[1]] = 1
                if self.bfs(i[0], i[1], count):
                    return True
                else:
                    self.visited[i[0]][i[1]] = 0
        return False


s = Solution()
print s.exist(["CAA", "AAA", "BCD"], "AAB")
