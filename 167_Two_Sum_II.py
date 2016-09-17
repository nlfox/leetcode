class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {v:(i+1) for i,v in enumerate(numbers)}
        for n in numbers:
            if m.has_key(target-n):
                if target == 2*n:
                    return [m[n]-1,m[n]]
                return [m[n],m[target-n]]