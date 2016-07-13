class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = nums[0]-1
        cnt = 0
        for i in nums:
            if i != last:
                nums[cnt] = i
                last = i
                cnt += 1
            else:
                last = i
        return cnt