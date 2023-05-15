# idea: Sliding window를 위해 Two pointer 사용
# "pwwkew" => 3 // "pwke" is a subsequence and not a substring.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcabcbb"
        #    l r
        # {c, a, b}
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:  # 이 부분이 핵심 \U0001f433
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(r-l+1, res)
        return res
