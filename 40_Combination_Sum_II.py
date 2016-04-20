class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        end = 0
        self.exist = {}
        d = {0: []}
        for i, num in enumerate(candidates):
            if num > target:
                end = i
                break
            else:
                if self.exist.has_key(num):
                    self.exist[num] += 1
                else:
                    self.exist[num] = 1

        for i in xrange(1, target + 1):
            print i
            d[i] = []
            if self.exist.has_key(i):
                d[i].append([i])
            for j in xrange(1, i):
                for elem in d[j]:
                    arr = [elem + elem1 for elem1 in d[i - j]]
                    for item in arr:
                        if (item!=[] and self.isFull(item)):
                            d[i].append(item)
            d[i] = self.delDupList(d[i])
        return d[target]

    def delDupList(self,ls):
        retList = []
        ret = []
        for l in ls:
            l.sort()
            sL = ','.join([str(i) for i in l])
            if sL not in retList:
                retList.append(sL)

        for i in retList:
            ret.append([int(j) for j in i.split(",")])
        return ret

    def isFull(self, l):
        sT = {}
        for i in l:
            if sT.has_key(i):
                sT[i] += 1
            else:
                sT[i] = 1
        for k, v in sT.items():
            if (v > self.exist[k]):
                return False
        return True


s = Solution()
print s.combinationSum2(
    [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29, 24, 17,
     27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12], 27)
