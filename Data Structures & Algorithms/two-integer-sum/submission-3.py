class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = []

        for idx, num in enumerate(nums):
            nums_index.append((num, idx))

        sorted_nums = sorted(nums_index)

        f, s = 0, len(sorted_nums) - 1

        while f < s:
            sm = sorted_nums[f][0] + sorted_nums[s][0]

            if sm == target:
                fir, sec = sorted_nums[f][1], sorted_nums[s][1]
                return [min(fir, sec), max(fir, sec)]
            elif sm > target:
                s -= 1
            else:
                f += 1