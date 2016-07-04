class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = version1.split(".")
        l2 = version2.split(".")
        ll1, ll2 = len(l1), len(l2)

        if ll1 > ll2:
            l2 += ["0"] * (ll1 - ll2)
        elif ll1 < ll2:
            l1 += ["0"] * (ll2 - ll1)
        for i, v in enumerate(l1):
            if int(l2[i]) < int(v):
                return 1
            elif int(l2[i]) > int(v):
                return -1
            else:
                continue
        return 0
