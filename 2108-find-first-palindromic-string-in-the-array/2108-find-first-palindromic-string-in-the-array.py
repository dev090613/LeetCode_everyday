# 2108. Find First Palindromic String in the Array
# idea: Two pointer
# Time: O(n)
# 다른 풀이: reverse
# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         for word in words:
#             l, r = 0, len(word)-1
#             while(l < r):
#                 if word[l] == word[r]:
#                     l += 1
#                     r -= 1
#                 else:
#                     break
#             if not(l<r):
#                 return word
#         return ""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""