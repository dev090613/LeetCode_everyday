# 문제: index에 따른 높이가 값으로 주어진 list가 있다. 최대 넓이를 구하라
# idea: 높이가 낮은 쪽의 포인터를 이동한다.
# Time: O(n): Single pass
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # [1,8,6,2,5,4,8,3,7]
        res = 0
        l, r = 0, len(height)-1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res