# 두 문자열이 Anagram인지 판단하라
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        # print(count_s, count_t)
        for k in count_s:
            if count_s[k] != count_t.get(k, 0):
                return False
        return True