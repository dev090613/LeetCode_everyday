# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
class Solution:
    """
    Set Two pointer
    Compare
        if abs(nums[l]) < abs(nums[r]):
            Append
            Move pointer    
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res = [0] * len(nums)
        # print(l, r, res) # 0 4 [0, 0, 0, 0, 0]
        i = 1
        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                value = nums[r]
                r -= 1
            else:
                value = nums[l]
                l += 1
            res[-i] = value ** 2
            i += 1
        return res