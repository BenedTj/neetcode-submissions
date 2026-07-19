class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minarr, res = math.inf, -math.inf
        cur = 0

        for num in nums:
            cur += num

            res = max(res, cur - minarr, cur)

            minarr = min(minarr, cur)

        return res