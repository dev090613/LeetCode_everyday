class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Reverse, 변수 하나를 더 할당
        """

        curMax = -1
        for i in range(len(arr)-1, 0-1, -1):
            newMax = max(arr[i], curMax)
            arr[i] = curMax
            curMax = newMax
        
        return arr