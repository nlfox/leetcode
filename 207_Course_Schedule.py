class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        IN = 0
        OUT = 1
        t = {}
        for i in prerequisites:
            if t.has_key(i[1]):
                t[i[1]][IN] += 1
            else:
                t[i[1]] = [1, 0]
            if t.has_key(i[0]):
                t[i[0]][OUT] += 1
            else:
                t[i[0]] = [0, 1]
        while 1:
            idx = -1
            for i, v in t.iteritems():
                if v[IN] == 0:
                    idx = i
                    t.pop(i)
                    break
            if idx == -1 and t != {}:
                return False
            elif idx == -1 and t == {}:
                return True
            flag = 0
            for i, edge in enumerate(prerequisites):
                if edge[0] == idx:
                    t[edge[1]][IN] -= 1
                    flag = 1
                    prerequisites[i] = "toremove"
            if flag:
                prerequisites.remove("toremove")


print Solution().canFinish(3, [[2, 0], [2, 1]])
