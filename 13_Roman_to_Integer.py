class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D":500, "M": 1000}
        sol = 0
        prev = 0
        # iterate backwards
        for i in range(len(s) -1, -1, -1):
            ch = s[i]
            inc = val[ch]
            if inc < prev:
                sol -= inc
            else:
                sol += inc
            prev = inc
        return sol