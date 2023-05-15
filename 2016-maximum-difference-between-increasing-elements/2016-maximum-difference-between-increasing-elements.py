# 주식으로 수익내기와 매우 비슷한 문제 같다.
# idea: Slid window
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l = 0
        # [3,5,2,10] 
        res = 0
        for r in range(1, len(nums)):
            if nums[l] > nums[r]:
                l = r
            res = max(res, nums[r] - nums[l])
        if res > 0:
            return res
        return -1
        return res
            