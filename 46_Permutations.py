class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.numLen = len(nums)
        self.res = []
        self.l = [True] * self.numLen
        self.dfs([])
        return self.res

    def dfs(self,s):
        flag = True
        for i in xrange(self.numLen):
            if self.l[i]:
                flag = False
                self.l[i] = False
                s += [self.nums[i]]
                self.dfs(s)
                s.pop()
                self.l[i] = True
        if flag:
            self.res.append([i for i in s])

print Solution().permute([1])