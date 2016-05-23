class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lenD = len(digits)
        flag = True
        idx = lenD - 1
        if not digits:
            return []
        ca = True
        while ca and idx >= 0:
            if ca:
                digits[idx] += 1
                ca = False
            if digits[idx] == 10:
                ca = True
                digits[idx] = 0
                idx -= 1

        if idx == -1:
            digits[0] = 0
            digits = [1] + digits
        return digits


print Solution().plusOne([2,9, 9, 9])
