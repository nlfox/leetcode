class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, 0
        while True:
            while height[left] != 0:
                left += 1
            right = left + 1
            while height[right] < height[left]:
                right += 1
