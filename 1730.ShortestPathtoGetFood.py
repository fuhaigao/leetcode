class Solution:
    '''
    BFS, cannot use DFS
    '''
    def getFood(self, grid: List[List[str]]) -> int:
        shortestPath = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = collections.deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    visited[i][j] = 1
        move = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for i, j in [[1,0], [-1,0], [0,1], [0,-1]]:
                    x1, y1 = x+i, y+j
                    if x1<0 or x1>=len(grid) or y1<0 or y1>=len(grid[0]) or visited[x1][y1] or grid[x1][y1] == 'X':
                        continue
                    if grid[x1][y1] == '#':
                        return move+1
                    visited[x1][y1] = 1
                    queue.append((x1,y1))
            move += 1
        return -1
                