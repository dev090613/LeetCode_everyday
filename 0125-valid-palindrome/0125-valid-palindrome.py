# 방법1
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = [char.lower() for char in s if char.isalnum()]
#         print(strs)
        
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():# check!
#                 return False
            
#         return True


# # 방법2: isalnum() 이 아닌 re.sub 사용
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub('[^a-z0-9]', '', s) # important\U0001f339
        
#         return s == s[::-1]

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s_lower = s.lowwer()
#         left, right = s_lower[0], s_lower[-1]
#         while left<len(s_lower)/2:
#             if left != right:
#                 return False
#             left += 1
#             right += 1
#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [char.lower() for char in s if char.isalnum()]
        while len(s_list) > 1:
            if s_list.pop(0) != s_list.pop():
                return False
        return True

