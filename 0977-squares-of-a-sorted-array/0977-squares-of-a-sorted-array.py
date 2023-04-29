# 오름차순의 배열을 입력 받는다. 그것의 각 아이템에 대한 제곱의 배열을 오름차순으로 반환한다.
# Input: nums = [-4,-1,0,3,10] Output: [0,1,9,16,100]
# Input: nums = [-7,-3,2,3,11] Output: [4,9,9,49,121]
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num*num for num in nums)
        