class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num_s = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                num_s.append(i)
            elif i == "/":
                r, l = int(num_s.pop()), int(num_s.pop())
                if l * r < 0 and l % r != 0:
                    num_s.append(l / r + 1)
                else:
                    num_s.append(l / r)
            else:
                res = eval(str(num_s[-2]) + i + str(num_s[-1]))
                num_s.pop()
                num_s.pop()
                num_s.append(res)
        return int(num_s[0])


print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
