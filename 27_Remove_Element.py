class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lens = len(nums)
        pointer = 0
        count = 0
        if lens==0:
            return 0
        while pointer != lens:
            while nums[pointer] == val :
                if pointer == lens - 1:
                    return count
                pointer += 1
            nums[count] = nums[pointer]
            pointer += 1
            count += 1
        return count

s = Solution()
print s.removeElement([3,2], 2)
