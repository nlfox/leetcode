class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        m = {'{': '}', '[': ']', '(': ')'}
        for i in xrange(len(s)):
            if m.has_key(s[i]):
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                if m[stack.pop()] == s[i]:
                    continue
                else:
                    return False
        if stack != []:
            return False
        return True
print Solution().isValid("")