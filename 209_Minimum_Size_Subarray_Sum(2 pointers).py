class Solution(object):
    def minSubArrayLen(self, s, nums):
        fast, slow, sum, n, r = 0, 0, 0, len(nums), float('inf')
        while 1:
            while fast < n and sum < s:
                sum += nums[fast]
                fast += 1

            if fast >= n and sum < s:
                break

            while slow < fast and sum >= s:
                r = min(r, fast - slow)
                sum -= nums[slow]
                slow += 1

        return 0 if r == float('inf') else r