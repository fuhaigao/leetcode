class Solution:
    def __init__(self):
        self.graph = dict()
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = collections.defaultdict(list)
        for i in range(len(equations)):
            self.graph[equations[i][0]].append((equations[i][1], values[i]))
            self.graph[equations[i][1]].append((equations[i][0], 1/values[i]))
        
        res = [-1]*len(queries)
        for i,query in enumerate(queries):
            if query[0] not in self.graph:
                continue
            elif query[0] == query[1]:
                res[i] = 1
            else:
                for neighbour, scalar in self.graph[query[0]]:
                    result = self.dfs(query[0], neighbour, query[1], scalar, set())
                    if result != -1:
                        res[i] = result
        return res
            
    def dfs(self, top, bot, target, val, visited):
        if bot == target:
            return val
        for neighbour, scalar in self.graph[bot]:
            if neighbour not in visited:
                visited.add(neighbour)
                result = self.dfs(bot, neighbour, target, scalar*val, visited)
                visited.remove(neighbour)
                if result != -1:
                    return result
        return -1