class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_point, t_leng = 0, len(t)

        for c in s:
            if c == t[t_point]:
                t_point += 1
                if t_point == t_leng:
                    return 0

        return t_leng - t_point