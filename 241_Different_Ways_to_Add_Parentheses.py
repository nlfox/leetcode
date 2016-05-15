class Solution(object):
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                res += [eval(str(k) + input[i] + str(j)) for k in res1 for j in res2]
        return res


print Solution().diffWaysToCompute("12+22*3")
