class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = dict({})

        for st in s:
            if st in alpha:
                alpha[st] += 1
            else:
                alpha[st] = 1
        
        for st in t:
            if st not in alpha:
                return False
            else:
                if alpha[st] == 1:
                    alpha.pop(st)
                else:
                    alpha[st] -= 1

        return len(alpha) == 0