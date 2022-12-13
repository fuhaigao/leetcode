class Solution:
    # prefix sum
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # n can be replaced by 1000 due to constrains
        n = max([trip[2] for trip in trips])
        stops = [0]*(n+1)
        for trip in trips:
            if trip[0] > capacity:
                return False
            stops[trip[1]] += trip[0]
            stops[trip[2]] -= trip[0]
        
        for i in range(n):
            capacity -= stops[i]
            if capacity < 0:
                return False
        return True
        