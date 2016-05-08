class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, v in enumerate(nums):
            if d.has_key(v):
                d[v] += [i]
            else:
                d[v] = [i]
        for i, v in enumerate(nums):
            d[v].pop(0)
            if d.has_key(target - v) and d[target - v] != []:
                return [i] + d[target - v]
            else:
                d[v] = [i] + d[v]


print Solution().twoSum([3,2,4], target=6)
