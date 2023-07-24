# 정수로 이루어진 배열 nums를 받았을 때, 짝수자리수인 item은 몇 개일까
# Input: nums = [12,345,2,6,7896] Output: 2
# How to compute the number of digits of a number ? Divide the number by 10 again and again to get the number of digits.
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # len(str(num)) % 2 == 0 => 문자열의 길이가 짝수이면 값 1(True에 해당)을 반환
        return sum(len(str(num)) % 2 == 0 for num in nums)
    
    # ```python
    # def findNumbers(self, nums: List[int]) -> int:
    #     return sum(len(str(n)) % 2 == 0 for n in nums) 
    
    # class Solution:
    # def findNumbers(self, nums: List[int]) -> int:
    #     return len([x for x in nums if len(str(x)) % 2 == 0])
    
#     class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         totalEven = 0
        
#         for num in nums:
#             digitCount = 0
#             while num >= 1:
#                 num /= 10
#                 digitCount += 1
            
#             if digitCount % 2 == 0:
#                 totalEven += 1
                
#         return totalEven