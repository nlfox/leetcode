class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        d = [0] * (target + 1)
        for n in filter(lambda a: a <= len(nums), nums):
            d[n] = 1
        for i in xrange(1, target + 1):
            for n in nums:
                if n >= i:
                    break
                d[i] += d[i - n]
        return d[target]
