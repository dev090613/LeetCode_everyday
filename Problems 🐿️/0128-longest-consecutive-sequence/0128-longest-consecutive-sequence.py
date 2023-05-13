
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # 이유: To allow O(1) lookups
        # 반환할 값인 가장 긴 길이
        longest = 0
        
        # nums에서 가장 긴 단편을 찾을 것이다.
        for num in nums: # O(n)
            # 단편의 시작점을 찾는다.
            if (num - 1) not in num_set:
                length = 0 # 1로 두어도 무방
                while (num + length) in num_set:
                    length += 1
                longest = max(length, longest) # scope 주의하기
        return longest
                    