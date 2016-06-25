class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.res = []
        self.rec(0, 0, 0, "")
        return self.res

    def rec(self, cnt, ind, left, string):
        if ind == self.n:
            self.res.append(string + left * ")")
            return
        if cnt == self.n * 2:
            return
        self.rec(cnt + 1, ind + 1, left + 1, string + "(")
        if left > 0:
            self.rec(cnt + 1, ind, left - 1, string + ")")


print Solution().generateParenthesis(3)
