class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l = len(prices)
        for i in range(l):
            for j in range(i+1, l):
                profit = prices[j] - prices[i]
                maxprofit = max(maxprofit, profit)
        return maxprofit
        