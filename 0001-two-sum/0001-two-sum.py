# # 방법1: Brute Force(2중 loop)/ O(n^2), O(1) / 21% 100%
# # Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # loop: list의 size만큼
#         for i in range(len(nums)):
#             # loop2: i+1 부터 마지막 인덱스까지
#             for j in range(i+1, len(nums)-1 + 1):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
            
            
# 방법2: Two-pass Hash Table/ O(N), O(N)/ 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # In the first iteration, List의 element's의 key와 value를 hash map에 저장
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        #  in the second iteration, complement의 존재를 찾습니다.
        # nums[i] + complement = target
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
