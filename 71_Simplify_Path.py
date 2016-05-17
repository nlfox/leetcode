class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = path.split("/")
        print s
        s_real = []
        while s != []:
            if s[0] == '.':
                pass
            elif s[0]=='':
                pass
            elif s[0] == "..":
                if len(s_real) > 0:
                    s_real.pop()
            else:
                s_real.append(s[0])
            s.pop(0)
        return '/' + '/'.join(s_real)


print Solution().simplifyPath("///")
