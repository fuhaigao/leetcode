class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.maxLength = 0
        self.neighbours = collections.defaultdict(list)
        for start, end in edges:
            self.neighbours[start].append(end)
            self.neighbours[end].append(start)
        visited = set([0])
        self.dfs(0, visited)
        return self.maxLength
    
    def dfs(self, node, visited):
        d1, d2 = 0, 0
        for neighbour in self.neighbours[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                depth = self.dfs(neighbour, visited)
                if depth > d1:
                    d2 = d1
                    d1 = depth
                elif depth > d2:
                    d2 = depth
        self.maxLength = max(self.maxLength, d1+d2)
        return d1+1
        