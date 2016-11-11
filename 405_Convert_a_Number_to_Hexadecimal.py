class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        c = num
        if c == 0:
            return "0"
        if c < 0:
            c = 4294967295 + c + 1

        r = []
        while c != 0:
            r += [c % 16]
            c = c // 16
        return ''.join([m[i] for i in r][::-1])

