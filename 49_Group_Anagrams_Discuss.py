class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for item in sorted(strs):
            sortedItem = ''.join(sorted(item))
            dic[sortedItem] = dic.get(sortedItem, []) + [item]
        return dic.values()



print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
