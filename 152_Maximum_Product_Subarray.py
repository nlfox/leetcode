class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenNums = len(nums)
        if not nums:
            return 0
        if lenNums == 1:
            return nums[0]
        pMax = nums[0]
        nMax = nums[0]
        m = nums[0]
        for i in xrange(1,lenNums):
            if nums[i] < 0:
                pMax, nMax = nMax, pMax
            pMax = max(nums[i], nums[i] * pMax)
            nMax = min(nums[i], nums[i] * nMax)
            m = max(pMax, m)
        return m
print Solution().maxProduct([1,2,3,-1,2,4])