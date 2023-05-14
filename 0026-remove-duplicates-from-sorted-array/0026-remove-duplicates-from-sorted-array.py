# input [0,0,1,1,1,2,2,3,3,4]
# output [1, 1, 2]
# Space: O(n)으로 풀기
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)-1+1, 1):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l