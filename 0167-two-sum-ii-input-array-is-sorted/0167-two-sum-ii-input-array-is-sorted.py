# non-decreasing order
# Input: numbers = [2,3,4], target = 6 
# Output: [1,3]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pre_map  = {} # n : index
        
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in pre_map:
                return [pre_map[diff]+1, i+1]
            pre_map[n] = i
        return
                