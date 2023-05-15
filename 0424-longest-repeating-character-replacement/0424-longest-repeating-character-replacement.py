# idea: k >= (windowLength - count[mostFreq]). windowLength가 최대값으로 갱신되려면 포인터의 갱신은 count[mostFreq]가 증가하는 방향이어야 효율적이다.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        "AABABBA", k = 1 => 4
           l
              r
         count = {'A':1, 'B':3}
         res = 4// mostFreq + k > res ==> l 이동
        '''
        count = {}
        res = 0
        # Sliding window
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            
            while (r - l + 1) - max(count.values()) > k: # 이 부분이 핵심 \U0001f338
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)    
        return res