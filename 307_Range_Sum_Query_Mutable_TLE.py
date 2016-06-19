class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.len = len(nums)
        self.d = []
        last = 0
        for i in nums:
            self.d.append(last)
            last += i
        self.d.append(last)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.nums[i] = val
        last = self.d[i]
        for j in xrange(i+1, self.len + 1):
            last += self.nums[j - 1]
            self.d[j] = last

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.d[j + 1] - self.d[i]



        # Your NumArray object will be instantiated and called as such:


numArray = NumArray([9, -8])
print numArray.update(0, 3)
print numArray.sumRange(1, 1)
print numArray.sumRange(0, 1)
print numArray.update(1, -3)
print numArray.sumRange(0, 1)
