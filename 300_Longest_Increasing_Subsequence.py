class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        resList = []
        for i in xrange(num_len):
            n = nums[i]
            c = 1
            for j in xrange(i, num_len):
                if nums[j] > n:
                    c += 1
                    n = nums[j]
            resList.append(c)
        return max(resList)


print Solution().lengthOfLIS([10, 9, 2, 5, 3, 4])
