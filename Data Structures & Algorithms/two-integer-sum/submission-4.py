class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = dict({})
        first = True

        for idx, num in enumerate(nums):
            if idx == 0:
                prev[num] = idx
                continue
            elif target - num in prev.keys():
                return [prev[target - num], idx]

            prev[num] = idx