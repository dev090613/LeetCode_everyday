# idea: prefix, postfix를 설정한다.
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 곱셈을 할 것이므로 기본값을 1로 설정한다
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # print(res)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix # prefix와 달리 곱으로 시작함
            postfix *= nums[i]
        # print(res)
        return res