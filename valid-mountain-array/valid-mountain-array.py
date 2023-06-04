# For every element we check the condition that the next element is greater than the current one
#  On O1

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # print(arr) # [0, 3, 2, 1]

        l, r = 0, len(arr)-1

        # left pointer를 이용해 peak를 찾는다.
        while l < len(arr) - 1 and arr[l] < arr[l+1]:
            l += 1
        # print(l) # 1

        # right pointer를 이용해 peak를 찾는다.
        while r > 0 and arr[r-1] > arr[r]:
            r -= 1
        # print(r) # 1

        if l == 0 or l == len(arr)-1:
            return False

        # # Edge: peak가 가장자리인 경우(오르막길, 내리막길)
        return l == r