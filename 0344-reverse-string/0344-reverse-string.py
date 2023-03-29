# Does in-place mean constant space complexity?
# two-pointer approach

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two-pointer를 이용한 방식 \U0001f338추천
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        # # pythonic한 방식, \U0001f338추천
        # s.reverse()
        
        # slicing을 이용한 방식
        # s[:] = s[::-1]