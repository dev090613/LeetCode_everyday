# 방법1: Brute Force, O(n^2): 이중 for문, O(1): 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop: list의 size만큼
        for i in range(len(nums)):
            # loop2: i+1 부터 마지막 인덱스까지
            for j in range(i+1, len(nums)-1 + 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
            
            
# 방법2: Two-pass Hash Table