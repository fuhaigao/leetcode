class Solution:
    # BFS
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         graph = collections.defaultdict(list)
#         for edge in edges:
#             graph[edge[0]].append(edge[1])
#             graph[edge[1]].append(edge[0])
        
#         queue = collections.deque()
#         nodes = set([x for x in range(n)])
#         count = 0
#         for i in range(n):
#             if i in nodes:
#                 count += 1
#                 queue.append(i)
#             while queue:
#                 node = queue.popleft()
#                 for neighbour in graph[node]:
#                     if neighbour in nodes:
#                         queue.append(neighbour)
#                         nodes.remove(neighbour)
#         return count
    
    # Union Find
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [x for x in range(n)]
        for edge in edges:
            root0 = self.find(roots, edge[0])
            root1 = self.find(roots, edge[1])
            if root0 != root1:
                roots[root0] = root1
                n -= 1
        return n
    
    def find(self, roots, node):
        primaryNode = node
        while roots[node] != node:
            node = roots[node]
        roots[primaryNode] = node
        return node