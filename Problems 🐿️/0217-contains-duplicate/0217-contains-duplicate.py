# 동일한 값이 두 번 반복되는 경우 True 반환
# brute forst O(n^2)
# hash map O(n)
# len(set)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False