[5월 9일 화요일] First Unique Character in a String

~~~python
# 387. First Unique Character in a String
# input: "leetcode" "aabb" /// output: 0 -1
# Time O(n) // string of length n two times, 
# Space O(1) // 영문자는 최대 26자
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            # count에 c를 저장할 것입니다. 그리고 그것의 숫자를 하나씩 올립니다.
            count[c] = count.get(c, 0) + 1
        for i, k in enumerate(count):
            if count[k] == 1:
                return s.index(k)
        return -1
~~~

