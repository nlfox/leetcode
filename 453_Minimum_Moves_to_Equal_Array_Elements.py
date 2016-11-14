class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = min(nums)
        return sum(map(lambda a:a-x,nums))
