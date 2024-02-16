![image-20240214030744233](/Users/isntsoo/Library/Application Support/typora-user-images/image-20240214030744233.png)



~~~python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if nums[r] < target or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

~~~

위 코드는 어디가 잘못됐을까?

