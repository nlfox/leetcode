class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            if d.has_key(i):
                d[i] += 1
            else:
                d[i] = 1
        res=sorted(d.items(),key=lambda d:d[1],reverse=True)
        return [i[0] for i in res[0:k]]


print Solution().topKFrequent([1,1,1,2,2,3], 2)
