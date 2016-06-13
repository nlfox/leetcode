class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def add(n1, n2):
            flow = 0
            if len(n1) > len(n2):
                nl, ns = n1[::-1], n2[::-1]
            else:
                nl, ns = n2[::-1], n1[::-1]
            res = []
            for i, v in enumerate(ns):
                s = int(v) + int(nl[i]) + flow
                if s >= 10:
                    flow = 1
                    s = s - 10
                else:
                    flow = 0
                res.append(str(s))

            for i in xrange(len(ns), len(nl)):
                s = int(nl[i]) + flow
                if s >= 10:
                    flow = 1
                    s -= 10
                else:
                    flow = 0
                i += 1
                res.append(str(s))
            res.append(str(flow) if flow > 0 else "")
            return ''.join(res[::-1])

        def mulSingle(n1, n):
            flow = 0
            n = int(n)
            res = []
            for i, v in enumerate(n1[::-1]):
                s = int(v) * n + flow
                if s > 10:
                    flow = s / 10
                    s = s % 10
                else:
                    flow = 0
                res.append(str(s))
            res.append(str(flow) if flow > 0 else "")
            return ''.join(res[::-1])

        if len(num1) > len(num2):
            nl, ns = num1[::-1], num2[::-1]
        else:
            nl, ns = num2[::-1], num1[::-1]
        res = "0"
        for i, v in enumerate(ns):
            res = add(mulSingle(nl[::-1], v) + "0" * i, res)
        for i in xrange(len(res)):
            if res[i] != '0':
                return res[i:]
        return "0"


print Solution().multiply("9133", "0")
