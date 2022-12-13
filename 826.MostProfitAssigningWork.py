class Solution:
    '''
    细节很多
    1. why sort ability by difficulty
    2. why sort worker
    3. why init i and maxProfit outside two loops
    '''

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ability = sorted(zip(difficulty, profit))
        i, res = 0, 0
        maxProfit = 0
        for w in sorted(worker):
            while i < len(ability) and ability[i][0] <= w:
                maxProfit = max(maxProfit, ability[i][1])
                i += 1
            res += maxProfit
        return res
