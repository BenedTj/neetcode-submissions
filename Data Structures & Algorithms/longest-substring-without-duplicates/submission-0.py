class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        window = set({})
        left, right = 0, -1
        lim = len(s) - 1
        res = 0

        while right < lim:
            if s[right + 1] not in window:
                right += 1
                window.add(s[right])
            else:
                res = max(res, right - left + 1)

                tmp = s[right + 1]
                while s[left] != tmp:
                    window.remove(s[left])
                    left += 1
                
                window.remove(s[left])
                left += 1
        
        res = max(res, right - left + 1)
        return res