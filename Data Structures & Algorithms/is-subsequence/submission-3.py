class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        s_point = 0
        s_leng = len(s)

        for c in t:
            if c == s[s_point]:
                s_point += 1
                if s_point == s_leng:
                    return True
        
        return False