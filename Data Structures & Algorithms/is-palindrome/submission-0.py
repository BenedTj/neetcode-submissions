class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(list(filter(lambda c: c.isalnum(), [c for c in s.lower()])))
        leng = len(filtered)
        idxs_to_check, last = math.floor(leng), leng - 1

        for idx in range(idxs_to_check):
            if filtered[idx] != filtered[last - idx]:
                return False
        
        return True