class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxdist, last = 0, len(nums) - 1

        for idx, num in enumerate(nums):
            if idx > maxdist:
                return False

            maxdist = max(maxdist, idx + num)

        return True