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
        times = 0
        for i in nums:
            if i != last:
                nums[cnt] = i
                last = i
                cnt += 1
                times = 0
            else:
                if times == 0:
                    times += 1
                    nums[cnt] = i
                    cnt += 1
                last = i
        return cnt