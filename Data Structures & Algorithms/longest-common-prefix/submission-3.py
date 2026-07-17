class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res, leng = strs[0], len(strs[0])

        for s in strs[1:]:
            count, opp_leng = 0, len(s)

            if opp_leng == 0:
                return ""

            if leng > opp_leng:
                res = res[:opp_leng]
                leng = opp_leng

            while count < leng and count < opp_leng:
                if res[count] == s[count]:
                    count += 1
                else:
                    res = res[:count]
                    leng = count
                    break
        
        return res