
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c
        return new_s == new_s[::-1]