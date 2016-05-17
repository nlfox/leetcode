class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        c = len(nums)
        res=[]
        for i in xrange(2 ** c):
            mask = bin(i)[2:].zfill(c)
            col=[]
            for i,v in enumerate(nums):
                if mask[i]=='1':
                    col.append(v)
            res.append(col)
        return res



print Solution().subsets([4,1,0])
