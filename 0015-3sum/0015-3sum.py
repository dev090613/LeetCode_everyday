# Notice that the solution set must not contain duplicate triplets.
# Two sum2와 유사하다 
# Time: O(nlogn + n^2) => O(n^2)
# Space: O(n), sorting이 메모리를 차지함
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if (i > 0) and a == nums[i-1]: # 정렬된 list의 값에서 중복되는 경우는 건너뛴다.
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res