class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'(': ')', '{': '}', '[': ']'}
        leng = 0
        st = []

        for c in s:
            if c in closing:
                st.append(c)
                leng += 1
            else:
                if leng > 0 and c == closing.get(st[leng - 1], 'X'):
                    st.pop()
                    leng -= 1
                else:
                    return False
        
        return st == []