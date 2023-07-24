# idea: frequency를 index로 삼는 array를 만든다. bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # bucket 만들기. 하나의 숫자만 있는 경우, 한 개도 없는 경우도 고려
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # print(count)
        for n, c in count.items():
            freq[c].append(n)
        # print(freq)
        res = []
        for i in range(len(freq)-1, 0-1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
# input: [1,1,1,2,2,3], 2
# count: {1: 3, 2: 2, 3: 1} O(n)
# index, value: [[None], [3], [2], [1], [None], [None], [None]] O(n)
# output: [1, 2]
        