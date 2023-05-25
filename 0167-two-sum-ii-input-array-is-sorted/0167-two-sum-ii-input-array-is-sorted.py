class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Input is non-decreasing order,
        exactly one solution,
        Return the indices of the two numbers added by one
        ---
           [2,7,11,15], 9
        l:  ^
        r:      ^
        
        cusSum = 2 + 11 = 9 > target => r-1
        
        Time: O(n), Space: O(1)
        """
        l, r = 0, len(numbers) - 1 # Set two pointer 
        
        while l < r: # Scaning with Two pointer
            cus_sum = numbers[l] + numbers[r]
            # print("cus_sum is {cus_sum}")
            
            if cus_sum > target:
                r -= 1
            elif cus_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        return
            