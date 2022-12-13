class Solution:
    # union find
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        roots = [i for i in range(n)]
        for edge in edges:
            root1 = self.find(roots, edge[0])
            root2 = self.find(roots, edge[1])
            if root1 == root2:
                return False
            roots[root1] = roots[root2]
            n -= 1
                
        return n == 1
            
    
    def find(self, roots, node):
        primaryNode = node
        # path compression
        while roots[node] != node:
            node = roots[node]
        roots[primaryNode] = node
        return node