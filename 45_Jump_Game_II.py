class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        p = 0
        m = 0
        mi = 0
        step = 0
        while p < l-1:
            for i in xrange(1,nums[p]+1):
                if p+i >= l-1:
                    return step+1
                if nums[p+i]+i >= m:
                    m = nums[p+i]+i
                    mi = i
            p = p+mi
            mi = p
            m = 0
            step += 1
        return step