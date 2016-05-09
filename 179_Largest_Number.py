class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        numStr = [str(i) for i in nums]
        dic = {str(i): [] for i in xrange(10)}
        for i in numStr:
            dic[i[0]].append(i)
        pass


print Solution().largestNumber([3, 30, 34, 5, 9])
