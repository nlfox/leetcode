class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        cnt, maxNum, i = 0, 0, 0
        while maxNum < n:
            if i < len(nums) and nums[i] <= maxNum + 1:
                maxNum += nums[i]
                i += 1
            else:
                maxNum += maxNum + 1
                cnt += 1
        return cnt


print Solution().minPatches([1, 4], 32)
