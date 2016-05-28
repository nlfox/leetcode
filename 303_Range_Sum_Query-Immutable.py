class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        d = [0] if nums else []
        for i in xrange(len(nums)):
            d.append(d[i] + nums[i])
        self.d = d

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.d:
            return 0
        return self.d[j + 1] - self.d[i]



        # Your NumArray object will be instantiated and called as such:


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 2)
print numArray.sumRange(0, 5)
