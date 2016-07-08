class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in list(set(nums1) & set(nums2)):
            res += [i] * min(nums1.count(i), nums2.count(i))
        return res
