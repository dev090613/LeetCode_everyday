
# 방법2: index 26
# counter도 사용할 수 있지 않을까..?

# # 방법1: sorted()/ 64%, 10%
# comment: sorting is last resort when coding an algorithm.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# #방법2: index26, string.count()/ 99%, 58%
# # count() method returns an integer that denotes number of times a substring occurs in a given string. 
# # https://www.geeksforgeeks.org/python-string-count-method/
# # It's practically O(1), however, we're using the built in str.count() method, which theoretically is O(n), and since we call it 26 times this solution is O(26*(n+m)). But, python built-in library methods are efficiently coded for speed ups and can generally be used for efficient solutions.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         for char in "abcdefghijklmnopqrstuvwxyz":
#             if s.count(char) != t.count(char):
#                 return False
#         return True

# 방법3: set(), count()/ 93%, 32%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True
        
# 방법4: hash-map, dict.items()
class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False
        hash_dict = dict() # it means, {}
        for char in s:
            if char in hash_dict:
                hash_dict[char] += 1
            else:
                hash_dict[char] = 1
        for char in t:
            if char in hash_dict:
                hash_dict[char] -= 1
            else:
                return False
        for k,v in hash_dict.items():
            if v != 0: # is not None과는 다르다. 이유는?
                return False
        return True
                

# # 방법5: collections.defaultdict()
# 추후 공부 필요
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         tracker = collections.defaultdict(int)
#         for x in s: tracker[x] += 1
#         for x in t: tracker[x] -= 1
#         return all(x == 0 for x in tracker.values())

            # Follow up

# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# Answer

# Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.