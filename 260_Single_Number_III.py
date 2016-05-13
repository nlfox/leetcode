class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if dic.has_key(i):
                dic.pop(i)
            else:
                dic[i] = 1
        return [i[0] for i in dic.items()]


print Solution().singleNumber([1, 2, 1, 3, 2, 5])
