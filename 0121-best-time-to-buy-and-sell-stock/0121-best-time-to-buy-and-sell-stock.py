# [7,1,5,3,6,4] => 5
# idea: Two pointer
# Time O(n) Space O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, (prices[sell] - prices[buy]))
            else:
                buy = sell
            sell += 1
        return max_profit