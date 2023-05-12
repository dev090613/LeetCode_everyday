
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         new_s = ""
#         for c in s:
#             if c.isalnum():
#                 new_s += c
#         return new_s == new_s[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if not self.alphaNum(s[left]):
                left += 1
                continue
            if not self.alphaNum(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
        return True
    
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))