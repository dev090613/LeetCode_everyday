# idea: 오름차순이므로, Target과 비교하며 Two pointer 이동
# Input: numbers = [2,3,4], target = 6 
# Output: [1,3]
# Time: O(n), Space O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l<r:
            cur_sum = numbers[l] + numbers[r]
            
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        return
                