
# 방법2: index 26
# counter도 사용할 수 있지 않을까..?
# # 방법1: sorted()/ 64%, 10%
# comment: sorting is last resort when coding an algorithm.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

#방법2: index26, string.count()
# count() method returns an integer that denotes number of times a substring occurs in a given string. 
# https://www.geeksforgeeks.org/python-string-count-method/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in "abcdefghijklmnopqrstuvwxyz":
            if s.count(char) != t.count(char):
                return False
        return True

        
# Follow up

# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# Answer

# Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.