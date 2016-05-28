class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1

s=[1, 2, 3, 4, 5, 6, 7]
Solution().rotate(s, 3)
print s
