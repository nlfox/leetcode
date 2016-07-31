class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = [0] * len(nums)
        self.bit = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.update(i, v)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        v = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= len(self.nums):
            self.bit[i] += v
            i += (i & -i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i - 1)

    def sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s

