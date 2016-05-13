class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if dic.has_key(i):
                dic.pop(i)
            else:
                dic[i] = 1
        return dic.items()[0][0]
print Solution().singleNumber([1,2,4,3,1,2,3])