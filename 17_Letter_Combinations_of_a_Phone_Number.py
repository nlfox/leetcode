class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits = list(digits)
        m = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        resList = [m[digits[0]]]
        for i in xrange(1, len(digits)):
            resList.append([])
            for j in xrange(len(resList[i - 1])):
                s = resList[i - 1][j]
                resList[i] += [s + v for v in m[digits[i]]]
        return resList[len(digits)-1]


s = Solution()
print s.letterCombinations("9")
