class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(set(nums))
        nums.sort()
        maxCnt = 1
        cnt = 1
        for i in xrange(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > maxCnt:
                maxCnt = cnt
        return maxCnt


print Solution().longestConsecutive([1,2,0,1])
