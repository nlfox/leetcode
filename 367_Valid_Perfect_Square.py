class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = (left + right) / 2
            r = mid * mid
            if r < num:
                left = mid + 1
            elif r > num:
                right = mid - 1
            else:
                return True
        return False
