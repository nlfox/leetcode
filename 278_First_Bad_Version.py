# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 2:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n + 1
        while left <= right:
            medium = (left + right) / 2
            if isBadVersion(medium) and isBadVersion(medium - 1):
                right = medium - 1
            elif not isBadVersion(medium):
                left = medium + 1
            else:
                return medium
        return medium


print Solution().firstBadVersion(3)
