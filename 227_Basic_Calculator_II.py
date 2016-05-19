class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        s_last = "+"
        s_num = []
        opers = ['+', '-', '*', '/']
        num = 0
        for i in xrange(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in opers:
                if s_last == "+":
                    s_num.append(num)
                elif s_last == "-":
                    s_num.append(-num)
                elif s_last == "*":
                    s_num[-1] = num * s_num[-1]
                elif s_last == "/":
                    if s_num[-1] // num < 0 and s_num[-1]%num != 0:
                        s_num[-1] = s_num[-1] // (num) + 1
                    else:
                        s_num[-1] = s_num[-1] // (num)
                s_last = s[i]
                num = 0
        if s_last == "+":
            s_num.append(num)
        elif s_last == "-":
            s_num.append(-num)
        elif s_last == "*":
            s_num[-1] = s_num[-1] * num
        elif s_last == "/":
            if s_num[-1] // num < 0 and s_num[-1] % num != 0:
                s_num[-1] = s_num[-1] // (num) + 1
            else:
                s_num[-1] = s_num[-1] // (num)

        return sum(s_num)


print Solution().calculate("10000-1000/10+100*1")
