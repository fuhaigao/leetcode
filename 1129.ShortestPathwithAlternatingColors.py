RED, BLUE = 0, 1
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [collections.defaultdict(list), collections.defaultdict(list)]
        for edge in redEdges:
            graph[0][edge[0]].append(edge[1])
        for edge in blueEdges:
            graph[1][edge[0]].append(edge[1])
        
        res = [math.inf for _ in range(n)]
        visited = [collections.defaultdict(int), collections.defaultdict(int)]
        queue = collections.deque([[0,RED], [0,BLUE]])
        level = 0
        while queue:
            queueSize = len(queue)
            for _ in range(queueSize):
                node, color = queue.popleft()
                res[node] = min(res[node], level)
                visited[color][node] = 1
                color ^= 1
                for neighbour in graph[color][node]:
                    if visited[color][neighbour] == 0:
                        queue.append([neighbour, color])
            level += 1
        return [-1 if item == math.inf else item for item in res]