class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        c = len(nums)
        d = {}
        res = []
        for i in xrange(2 ** c):
            mask = bin(i)[2:].zfill(c)
            col = []
            for i, v in enumerate(nums):
                if mask[i] == '1':
                    col.append(v)
            if d.has_key(str(col)):
                continue
            else:
                d[str(col)] = True
                res.append(col)
        return res


print Solution().subsetsWithDup([4,4,4,1,4])
