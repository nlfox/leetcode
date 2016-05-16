# class Solution(object):
#     def bulbSwitch(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         bulbs = [True for i in xrange(n)]
#         for i in xrange(2, n + 1):
#             for j in xrange(1, n / i+1):
#                 bulbs[i * j - 1] = not bulbs[i * j - 1]
#
#         return bulbs.count(True)
# for i in xrange(1,100):
#     print i,Solution().bulbSwitch(i)

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(__import__("math").ceil((1 + n) ** 0.5 - 1))


print Solution().bulbSwitch(8)
