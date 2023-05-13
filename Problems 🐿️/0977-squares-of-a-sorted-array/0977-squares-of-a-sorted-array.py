# 오름차순의 배열을 입력 받는다. 그것의 각 아이템에 대한 제곱의 배열을 오름차순으로 반환한다.
# Input: nums = [-4,-1,0,3,10] Output: [0,1,9,16,100]
# Input: nums = [-7,-3,2,3,11] Output: [4,9,9,49,121]
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 방법1: sorted()/ 80% 12%/ O(NlogN) O(N)
        # return sorted(num*num for num in nums)
        # 방법2: Two pointer/ O(N) O(N)
        # Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
        n = len(nums)
        empty_list = [0] * n # or list(range(n)), empty list 생성
        left, right = 0, n-1 # two pointer
        for i in range(n-1, 0-1, -1):# exclusive, 큰 수를 우측에 배치
            # 양 포인터의 절대값을 비교
            if abs(nums[left]) < abs(nums[right]): # 우 포인터가 더 큰 경우
                # 우 포인터 인덱스의 값을 제곱한 것이 빈 리스트로
                value = nums[right]
                right -= 1
            else: # 좌 포인터가 큰 경우
                value = nums[left]
                left += 1
            empty_list[i] = value * value
        return empty_list
    # 문자열처리를 하여서 음수를 양수로 바꾼 다음에 솔팅하는 방법은?