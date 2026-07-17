class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st, res = [], []
        leng = 0

        for _ in range(len(temperatures)):
            res.append(None)
        
        for idx, temp in enumerate(temperatures):
            while leng > 0 and st[leng - 1][0] < temp:
                _, i = st.pop()
                leng -= 1

                res[i] = idx - i
            st.append((temp, idx))
            leng += 1
        
        for temp, idx in st:
            res[idx] = 0

        return res