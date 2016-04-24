class Solution(object):
    def combinationSum(self, candidates, target):
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
                if not self.exist.has_key(num):
                    self.exist[num] = True

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
                sT[i] = True
            else:
                sT[i] = False
        for k, v in sT.items():
            if not self.exist[k]:
                return False
        return True

