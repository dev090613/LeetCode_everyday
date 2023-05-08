



---

~~~python
# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## 주어진 List[int]에서 동일한 수가 두 번 반복되는지
        ## 방법0: length. Time: O(n), Space: O(n)
        # return len(set(nums)) < len(nums)
        ## 방법1: naive solution O(n^2) O(1) - 각 요소당 루프를 돌며 일치하는 것을 찾아낸다
        ## 방법2: sorting O(nlogn) O(1) - 정렬 후 인접한 두 개의 포인터를 이용하여 서치한다.
        ## 방법3: hashset O(n) O(n) - 약간의 메모리를 더 사용하는 대신 정렬 없이 동일한 value 찾아냄
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
~~~

~~~python
# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 문자열 s와 문자열 t가 Anagram인지
        
        ## 방법1: hashset Time: O(s+t) Space: O(s+t)// s+t는 n에 근사한다
        # 두 문자열의 길이가 다르다면 이미 anagram이 아니다
        if len(s) != len(t):
            return False
        
        # s와 t의 hashmap을 만든다.
        count_s, count_t = {}, {}
        
        # 문자열의 인덱스를 따라 진행하여 'a': 1 , 이런 식으로 개수를 셀 것임
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        for k in count_s:
        #     # if count_s[k] != count_t[k]: 의 문제점?
        #     # keyError가 발생할 수 있다. 아래의 코드가 더욱 개선된 방식이다
        #     # 에러를 반환하지 않고 기본값 0을 반환하여 비교한다.
            if count_s[k] != count_t.get(k, 0):
                return False
        return True
    
        # 방법2: pythonic, Counter(): 방법 2의 기능이 파이썬에 built-in되어 있다. 속도는 더 빠르다.
        # return Counter(s) == Counter(t)
        
        # Follow up: Space: O(1)으로 해결해보기
        ## 방법3: sorted, Time: O(nlogn) Space: O(1)
        # return sorted(s) == sorted(t)        
~~~

~~~python
# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 방법1: Brute force O(n^2) O(1)
        # 방법2: Hashmap{val: index} O(n) O(n)
        #######################################
        # List를 순회
        # target - value가 hashmap에 없다면
        # hashmap에 val: index 추가
        # 있다면 그 인덱스와 현재 인덱스 반환
        # // 반환할 값이 인덱스이니까 val: index로 설정하는 것 같다
        #######################################
        hashmap = {} # value:inex # 탐색할 것(if in)은 key에 배치, 반환(return)할 것은 value에 배치
        
        # index와 value가 필요한 경우 enumerate를 사용한다. 시작값 바꿀 수 있음
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        # return # 항상 하나의 sol이 존재하므로 반환값 필요 없음 위에서 다 반환될 것
~~~

~~~python
# 49. Group Anagrams

~~~

