class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        zeroCount = 0
        zeroIdx = 0
        res = []
        for i, v in enumerate(nums):
            if v == 0:
                zeroCount += 1
                zeroIdx = i
                continue
            total *= v
        if zeroCount > 1:
            return [0 for i in xrange(len(nums))]
        elif zeroCount == 1:
            res = [0 for i in xrange(len(nums))]
            res[zeroIdx] = total
            return res
        else:
            for i in nums:
                res.append(total / i if i != 0 else 0)
            return res


print Solution().productExceptSelf([1, 0])
