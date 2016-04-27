class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #todo: Btree
        numsLen = len(nums)
        minLen = 9223372036854775807
        tNum = numsLen
        flag = True
        levels = [nums]
        level = -1
        locs = []
        while (flag):
            level += 1
            if tNum % 2 == 0:
                tNum = tNum / 2
                levels.append([])
                for i in xrange(tNum):
                    curNum = sum(levels[level][(2 * i):(2 * i) + 2])
                    levels[level + 1].append(curNum)
                    if (curNum >= s):
                        locs.append(i)
                        flag = False
                        pass
            else:
                tNum = tNum / 2
                levels.append([])
                for i in xrange(tNum):
                    curNum = sum(levels[level][(2 * i):(2 * i) + 2])
                    levels[level + 1].append(curNum)
                    if (curNum >= s):
                        locs.append(i)
                        flag = False
                levels[level + 1].append(levels[level][-1])
                tNum+=1
        print level+1,locs


s = Solution()
print s.minSubArrayLen(5, [2, 3, 1, 2, 4, 3])
