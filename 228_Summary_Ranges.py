class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        lenNum = len(nums)
        if lenNum == 0:
            return []
        res = []
        last = nums[0]
        start = 0
        for i in xrange(1, lenNum):
            if nums[i] == last + 1:
                last = nums[i]
                continue
            else:
                gap = i - start
                if gap > 1:
                    res.append(str(nums[start]) + "->" + str(nums[i - 1]))
                else:
                    res.append(str(nums[i - 1]))
                start = i
                last = nums[i]
        if lenNum - start == 1:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[lenNum - 1]))
        return res


print Solution().summaryRanges([-1, 1, 2, 4, 5, 7, 8, 9])
