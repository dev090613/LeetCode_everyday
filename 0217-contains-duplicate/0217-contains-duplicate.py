class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 방법1: set()과 list()의 크기 차이를 이용
        if len(nums) != len(set(nums)):
            return True
        return False