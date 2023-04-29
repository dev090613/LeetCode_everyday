# 문제: 0 또는 1로 이루어진 array가 있다. 1이 최대 몇 개 연속적으로 이어졌는가
# Input: nums = [1,1,0,1,1,1] Output: 3
# Input: nums = [1,0,1,1,0,1] Output: 2
# Input: nums = [] Output: 0
# Follow up: You can also try something fancy one liner solution as shared by Stefan Pochmann.
# 해결방법: One pointer
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)
