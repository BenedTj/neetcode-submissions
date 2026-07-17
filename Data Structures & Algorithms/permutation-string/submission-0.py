from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        aldict1 = dict({})

        for s in s1:
            if s in aldict1:
                aldict1[s] += 1
            else:
                aldict1[s] = 1
        
        left, right = 0, len(s2) - 1

        while s2[left] not in aldict1 and left < len(s2) - 1:
            left += 1
        while s2[right] not in aldict1 and right > 0:
            right -= 1

        searchable = s2[left:right+1]
        for i in range(len(searchable) - len(s1) + 1):
            aldict2 = aldict1.copy()

            for c in searchable[i:i+len(s1)]:
                if c in aldict2:
                    aldict2[c] -= 1
                    if aldict2[c] == 0:
                        aldict2.pop(c)
                    if aldict2 == dict({}):
                        return True
                else:
                    break

        return False 