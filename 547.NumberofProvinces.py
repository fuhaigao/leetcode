class Solution:
    '''
    union find, can be donw with DFS, but I think union find is more intuitive
    '''
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        roots = [x for x in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    a, b = self.find(roots, i), self.find(roots, j)
                    if a != b:
                        roots[b] = a
                        count += 1
        return len(isConnected)-count
    
    def find(self, roots, node):
        primaryNode = node
        while roots[node] != node:
            node = roots[node]
        roots[primaryNode] = node
        return node