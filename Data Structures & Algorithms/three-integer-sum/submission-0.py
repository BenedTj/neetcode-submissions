class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        lim = len(nums) - 1
        res = []
        prev = set({})

        for idx, val in enumerate(nums_sorted):
            target = -val
            left, right = 0, lim

            while left < right:
                if left == idx:
                    left += 1
                    continue
                if right == idx:
                    right -= 1
                    continue
                
                tmp = nums_sorted[left] + nums_sorted[right]
                if tmp < target:
                    left += 1
                elif tmp > target:
                    right -= 1
                else:
                    toadd = [nums_sorted[left], nums_sorted[right], val]
                    tupl = tuple(sorted(toadd))
                    
                    if tupl not in prev:
                        res.append(toadd)
                        prev.add(tupl)
                    
                    left += 1
                    right -= 1
        
        return res