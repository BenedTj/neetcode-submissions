class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = list(filter(lambda c: c.isalnum(), s.lower()))
        amount_to_check, lim = math.floor(len(filtered) >> 1), len(filtered) - 1

        for idx in range(amount_to_check):
            if filtered[idx] != filtered[lim - idx]:
                return False
        
        return True