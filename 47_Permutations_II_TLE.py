class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.numLen = len(nums)
        self.res = []
        self.l = [True] * self.numLen
        self.uni = {}
        self.dfs([])
        return self.res

    def dfs(self, s):
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
            st = str([i for i in s])
            if not self.uni.has_key(st):
                self.uni[st] = True
                self.res.append([i for i in s])
print Solution().permuteUnique([1,1,2])
