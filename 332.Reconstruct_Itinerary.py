class Solution:
    # Use heapq to keep lexical order 
    # Use DFS to guarentee the correct path
    #https://www.youtube.com/watch?v=LKSdX31pXjY
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        paths = {}
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            if origin not in paths:
                paths[origin] = []
            heapq.heappush(paths[origin], dest)
        res = []
        self.dfs(res, "JFK", paths)
        return res
    
    def dfs(self, res, start, paths):
        destinations = paths.get(start)
        # example for why using while:
        # [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        while destinations:
            self.dfs(res, heapq.heappop(destinations), paths)
        res.insert(0, start)
        return

# Use stack to implement DFS
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = dict()
#         for ticket in tickets:
#             origin, dest = ticket[0], ticket[1]
#             if origin not in graph:
#                 graph[origin] = []
#             heapq.heappush(graph[origin], dest)
#         stack = ["JFK"]
#         res = []
#         while stack:
#             start = stack.pop()
#             while graph.get(start):
#                 dest = heapq.heappop(graph[start])
#                 stack.append(start)
#                 start = dest
#             res.insert(0, start)
#         return res
                