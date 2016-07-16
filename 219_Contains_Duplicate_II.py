class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, v in enumerate(nums):
            if d.has_key(v):
                if (i - d[v]) <= k:
                    return True
                else:
                    d[v] = i
            else:
                d[v] = i
        return False
