# # 방법2: isalnum() 이 아닌 re.sub 사용
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub('[^a-z0-9]', '', s)
        
#         return s == s[::-1]
#----------------------------------------------------------

# 학습용 솔루션: Space O(1)로 풀어보기, isalnum 사용하지 않기 
# 조건: after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters
# input: "A man, a plan, a canal: Panama", output: True
# idea: Two pointer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while (not self.alphaNum(s[left])) and (left < right):
                left += 1
                print("left is ", s[left])
            while (not self.alphaNum(s[right])) and (left < right):
                right -= 1
                print("right is ", s[right])
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
            print("left and right is ", left, right)
        return True
    
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))