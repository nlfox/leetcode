class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=[0,0,0]
        for i in nums:
            n[i]+=1
        p = 0
        for i in xrange(n[0]):
            nums[p]=0
            p+=1
        for i in xrange(n[1]):
            nums[p]=1
            p+=1
        for i in xrange(n[2]):
            nums[p]=2
            p+=1