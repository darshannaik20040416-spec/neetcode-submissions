class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprofit = prices[0]
        maxprofit = 0
        for price in prices:
            minprofit = min(minprofit, price)
            profit = price  - minprofit
            maxprofit = max(maxprofit, profit)
        return maxprofit
            

        