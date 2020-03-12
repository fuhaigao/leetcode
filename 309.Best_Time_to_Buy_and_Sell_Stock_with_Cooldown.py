class Solution:
    # https://www.youtube.com/watch?v=Ggzbo9eVrLU
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        hold = [0]*len(prices)
        unhold = [0]*len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            if i == 1:
                hold[i] = max(hold[0], -prices[1])
            hold[i] = max(hold[i-1], unhold[i-2]-prices[i])
            unhold[i] = max(unhold[i-1], hold[i-1]+prices[i])
        return unhold[len(prices)-1]