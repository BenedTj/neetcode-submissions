class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for idx, s in enumerate(strs):
            res += "#"
            for idx2, c in enumerate(s):
                if idx2 != 0:
                    res += "|"
                res += str(ord(c))
        
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []

        if s == "":
            return res

        strs = s.split("#")
        for st in strs[1:]:
            tmp = ""
            chs = st.split("|")

            for c in chs:
                if c != "":
                    tmp += chr(int(c))
            
            res.append(tmp)

        return res