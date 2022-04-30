class Solution:
    '''
    1. Inital Idea: Use one heap sort by profits decreasingly. For each round, heappop until the maximum profit with captial <= w, and then heappush back all poped values except the selected one. However, this method TLE
    2. So use gready appoach with two heap:
        - heapCap stores (capital, profit) sort by captical increasingly
        - heapPro stores current affordable projects sort by profit decreasingly
    '''

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heapPro = []
        heapCap = []
        n = len(profits)
        for i in range(n):
            heapq.heappush(heapCap, (capital[i], profits[i]))
        for i in range(k):
            while heapCap and heapCap[0][0] <= w:
                c, p = heapq.heappop(heapCap)
                heapq.heappush(heapPro, (-p, c))
            if not heapPro:
                break
            p, c = heapq.heappop(heapPro)
            w = w - p
        return w
