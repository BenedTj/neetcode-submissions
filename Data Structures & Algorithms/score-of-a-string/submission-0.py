class Solution:
    def scoreOfString(self, s: str) -> int:
        prev, res = ord(s[0]), 0

        for val in s[1:]:
            ord_val = ord(val)
            res += abs(ord_val - prev)
            prev = ord_val
        
        return res