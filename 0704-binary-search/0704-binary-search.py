class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ascending order로 정렬된 arr(nums)
        # nums 중에서 target을 찾고, 그것의 index를 반환하라
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1