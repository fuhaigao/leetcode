class Solution:
    # Greedy, can be solved with dp as well
    def maxProfit(self, prices: List[int], fee: int) -> int:
        minPrice = prices[0]
        result = 0
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = prices[i] - minPrice - fee
            if profit > 0:
                print(i, prices[i], minPrice)
                result += profit
                minPrice = prices[i] - fee  #Important: 可以选择在之后更合适的机会进行transaction，那样的话minPrice提前减去手续费
        return result