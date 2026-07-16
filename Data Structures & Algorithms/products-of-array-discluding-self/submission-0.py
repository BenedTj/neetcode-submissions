class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_back = []
        leng = len(nums)
        res = []

        acc = 1
        for idx in range(len(nums) - 1, -1, -1):
            acc *= nums[idx]
            from_back.append(acc)

        acc = 1
        for idx, val in enumerate(nums):
            if idx == 0:
                res.append(from_back[leng - 2])
            elif idx == leng - 1:
                res.append(acc)
            else:
                res.append(acc * from_back[leng - idx - 2])
            
            acc *= val
        
        return res