# 중복되는 값이 있는 경우 True
# [1,2,3,1]
# True
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # # 방법1: set()과 list()의 크기 차이를 이용/ 61% 77%
#         # if len(nums) != len(set(nums)):
#         #     return True
#         # return False