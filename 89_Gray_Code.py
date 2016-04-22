class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = [False for i in xrange(n)]
        self.resList = []
        self.exist = {0:True}
        self.max = 2**n
        self.dfs(arr, 1)
        self.resList.insert(0,0)
        print self.resList

    def dfs(self, arr, depth):
        if depth == self.max:
            return True
        for index in range(len(arr))[::-1]:
            arr[index] = not arr[index]
            binInt = int(''.join([str(int(i)) for i in arr]), 2)
            if self.exist.has_key(binInt):
                arr[index] = not arr[index]
                continue
            else:
                self.exist[binInt] = True
                if self.dfs(arr, depth + 1):
                    self.resList.insert(0, binInt)
                    return True
                else:
                    self.exist[binInt] = False
        return False


s = Solution()
print s.grayCode(2)
