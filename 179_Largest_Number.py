# class Solution:
#     # @param {integer[]} nums
#     # @return {string}
#     def largestNumber(self, nums):
#         numStr = [str(i) for i in nums]
#         dic = {str(i): [] for i in xrange(10)}
#         for i in numStr:
#             dic[i[0]].append(i)
#
#         def cmpNum(s1, s2):
#             ls1 = len(s1)
#             ls2 = len(s2)
#             num = max(ls1, ls2) - 1
#             for i in xrange(num):
#                 if ls1 <= (i + 1):
#                     ts1 = 0
#                 else:
#                     ts1 = ord(s1[i + 1]) - ord(s1[i])
#                 if ls2 <= (i + 1):
#                     ts2 = 0
#                 else:
#                     ts2 = ord(s2[i + 1]) - ord(s2[i])
#                 if ts1 != ts2:
#                     return ts1 - ts2
#
#             return 0
#
#         res = ""
#         for i in range(10)[::-1]:
#             dic[str(i)].sort(cmp=cmpNum, reverse=True)
#             res += ''.join(dic[str(i)])
#         if set(list(res)) == set(['0']):
#             return "0"
#         return res
# wrong!!!
class Solution:
    def largestNumber(self, nums):
        ret = ''.join(sorted([str(x) for x in nums], cmp=lambda x, y: cmp(y + x, x + y)))
        return ret if ret[0] != '0' else "0"


print Solution().largestNumber([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247])
