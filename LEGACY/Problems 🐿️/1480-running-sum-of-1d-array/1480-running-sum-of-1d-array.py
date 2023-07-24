# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for num in nums[1::]:
            result.append(result[-1] + num)
        return result