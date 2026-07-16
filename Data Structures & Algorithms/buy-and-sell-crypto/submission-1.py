class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, res = 101, 0

        for price in prices:
            res = max(res, price - mini)

            mini = min(mini, price)

        return res