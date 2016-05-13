class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if dic.has_key(i):
                if dic[i] == 2:
                    dic.pop(i)
                else:
                    dic[i] += 1
            else:
                dic[i] = 1
        return dic.items()[0][0]


print Solution().singleNumber([2, 2, 2, 5, 3, 3, 3])
