# Does in-place mean constant space complexity?
# two-pointer approach

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         # two-pointer를 이용한 방식 \U0001f338추천
#         left, right = 0, len(s)-1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
        
        
#         # slicing을 이용한 방식
#         # s[:] = s[::-1]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # slicing은 문자열과 list를 처리하기 아주 좋은 방법이지만(성능도 좋다)
        # return [s::-1] 은 오답으로 처리된다. 그 이유는
        # 공간복잡도를 O(1)으로 제한하기 때문이다.
        # 다만 s[:] = s[::-1] 으로 제출하면 해결이 된다.
        # The [:] makes a shallow copy of the array, hence allowing you to modify your copy without damaging the original.
        s[:] = s[::-1]
        return s[:]
