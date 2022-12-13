'''
We can solve it by walking along the path reversely.

1. Find nodes with out degree 0, they are terminal nodes, we remove them from graph and they are added to result
2. For nodes who are connected terminal nodes, since terminal nodes are removed, we decrease in-nodes' out degree by 1 and if its out degree equals to 0, it become new terminal nodes
3. Repeat 2 until no terminal nodes can be found.
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        neighbours = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for i in range(len(graph)):
            degree[i] = 0
        for i, nodes in enumerate(graph):
            for node in nodes:
                neighbours[node].append(i)
                degree[i] += 1
        
        queue = collections.deque()
        for node in degree:
            if degree[node] == 0:
                queue.append(node)
        
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbour in neighbours[node]:
                degree[neighbour] -= 1
                if degree[neighbour] == 0:
                    queue.append(neighbour)
        return sorted(res)