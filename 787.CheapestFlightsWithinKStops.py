class Solution:
    '''
    Dijkstra 变种
    '''
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         flightMap = collections.defaultdict(list)
#         for flight in flights:
#             flightMap[flight[0]].append(flight[1:])
            
#         pq = [(0, src, k)]
#         steps = collections.defaultdict(int)
#         while pq:
#             cost, curr, stepRemains = heapq.heappop(pq)
#             if curr == dst:
#                 return cost
#             if steps[curr] > stepRemains:
#                 continue
#             steps[curr] = stepRemains
#             for neighbour, dw in flightMap[curr]:
#                 heapq.heappush(pq, (cost+dw, neighbour, stepRemains-1))

#         return -1
        
        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightMap = collections.defaultdict(list)
        for flight in flights:
            flightMap[flight[0]].append(flight[1:])
        pq = [(0, src, 0)] #(cost, city, stepsTaken)
        visited = collections.defaultdict(int)
        
        while pq:
            cost, curr, stepsTaken = heapq.heappop(pq)
            if curr == dst:
                return cost
            if stepsTaken == k+1:
                continue
            if visited[(curr, stepsTaken)] == 1:
                continue
            visited[(curr, stepsTaken)] = 1
            
            for neighbour, dw in flightMap[curr]:
                if visited[(neighbour, stepsTaken+1)] == 0:
                    heapq.heappush(pq, (cost+dw, neighbour, stepsTaken+1))
        return -1
    
    # BFS, TLE
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         flightMap = collections.defaultdict(list)
#         for flight in flights:
#             flightMap[flight[0]].append(flight[1:])
        
#         level = 0
#         queue = collections.deque([(src,0)])
#         res = float('inf')
#         while queue:
#             for _ in range(len(queue)):
#                 curr, currCost = queue.popleft()
#                 if curr == dst:
#                     res = min(res, currCost)
#                 for neighbour, cost in flightMap[curr]:
#                     queue.append((neighbour, cost+currCost))
#             level += 1
#             if level > k+1:
#                 break
#         return res if res != float('inf') else -1