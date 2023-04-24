# #방법1: for i in range(len(arr)) 69%, 96%
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # ascending order로 정렬된 arr(nums)
#         # nums 중에서 target을 찾고, 그것의 index를 반환하라
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#         return -1

# 방법2: binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 전제: 오름차순 정렬된 arr nums
        # left와 right는 arr의 양 끝 인덱스
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1
        
#         while left<=right:
#             mid = (left+right)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]>target:
#                 right = mid-1
#             else:
#                 left = mid+1
        
#         return -1