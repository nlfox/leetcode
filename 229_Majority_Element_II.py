class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        r = []
        n = len(nums) / 3
        if n==0:
            return list(set(nums))
        for i in nums:
            if d.has_key(i):
                d[i] += 1
                if d[i] == n + 1:
                    r.append(i)
            else:
                d[i] = 1
        return r
