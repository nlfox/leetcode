class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        strs.sort()
        for i in strs:
            r = list(i)
            r.sort()
            r=''.join(r)
            if d.has_key(r):
                d[r].append(i)
            else:
                d[r] =[i]
        res=[]
        for i in d.itervalues():
            res.append(i)
        return res



print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
