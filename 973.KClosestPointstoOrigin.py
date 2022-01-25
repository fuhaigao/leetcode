'''
仔细读题完，想到heap很简单，但要注意每次直接heappush, len(pq) > k的时候 再 heappop 可以精炼很多逻辑。 要充分利用 heappush and heappop
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        kthMinDist = float('inf')
        for point in points:
            dist = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(pq, (-dist, point))
            if len(pq) > k:
                heapq.heappop(pq)
                
        return [p[1] for p in pq]