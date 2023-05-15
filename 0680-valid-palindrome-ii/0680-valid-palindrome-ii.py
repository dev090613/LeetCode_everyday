# 문제: Palindrome인지 판단, 하나의 char까지는 지울 수 있다.
# "aba" => True
# "abca" => True
# "abc" => False

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while(l < r):
            if s[l] != s[r]:
                return self.isPalindrome(s, l+1, r) or self.isPalindrome(s, l, r-1)
            l+=1
            r-=1
        return True
    
    def isPalindrome(self, s, l, r):
        # l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
