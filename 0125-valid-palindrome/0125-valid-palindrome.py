# string.isalnum()
# The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

# re.sub('찾을 패턴', '변경할 내용', '원본')
# [^a-z]: 선두에 위치할 경우 해당 문자 패턴(알파벳)이 아닌 것 매칭

# 방법1
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = [char.lower() for char in s if char.isalnum()]
#         print(strs)
        
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():# check!
#                 return False
            
#         return True


# 방법2: isalnum() 이 아닌 re.sub 사용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s) # important\U0001f339
        
        return s == s[::-1]