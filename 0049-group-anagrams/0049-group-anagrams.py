# The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

# In python, list can't be key in dictionary. 
# list can be converted to tuple. 
# 따라서, list는 튜플로 변환 후 dict의 key로 사용할 수 있다.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # KeyError 대신 empty list 반환
        res = defaultdict(list)
        
        # 동일한 counter를 가진 str들끼리 묶을 것이다.
        # { [counter1] : [str1, str2], 
        #   [counter2] : [str3] }
        for str in strs:
            counter = [0] * 26 # a-z의 반복횟수 저장될 것
            for char in str:
                counter[ord(char) - ord('a')] += 1
            res[tuple(counter)].append(str) # counter 같은 str끼리 모일 것
        return res.values()
        