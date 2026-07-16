class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        def getLeft(num: int) -> int:
            nonlocal numset
            
            if num in numset:
                numset.remove(num)
                return getLeft(num - 1) + 1
            else:
                return 0
        
        def getRight(num: int) -> int:
            nonlocal numset

            if num in numset:
                numset.remove(num)
                return getRight(num + 1) + 1
            else:
                return 0

        for num in nums:
            if num in numset:
                res = max(res, getLeft(num - 1) + getRight(num + 1) + 1)

        return res