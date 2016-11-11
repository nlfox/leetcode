import itertools


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = {}
        r=[]
        for i in itertools.permutations(nums):
            if str(i) in m:
                pass
            else:
                m[str(i)]=1
                r+=[list(i)]
        return r