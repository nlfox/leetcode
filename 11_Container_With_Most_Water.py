class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, m = 0, len(height) - 1, 0
        while left < right:
            m = max(m, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m


print Solution().maxArea([5, 2, 12, 1, 5, 3, 4, 11, 9, 4])
