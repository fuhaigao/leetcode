class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit

    # can buy multiple and sell multiple
    def maxProfitAlter(self, prices: List[int]) -> int:
        res = 0
        currMax = 0
        for i in range(1, len(prices)):
            currMax = max(0, currMax + prices[i]-prices[i-1])
            res = max(res, currMax)
        return res
