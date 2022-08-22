DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]
class Solution:
    def __init__(self):
        self.boundries = list()
    def shortestBridge(self, grid: List[List[int]]) -> int:
        xStart, yStart = self.findFirst(grid)
        self.dfs(grid, xStart, yStart)
                        
        queue = collections.deque(self.boundries)
        level = 0 
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for i, j in DIRECTIONS:
                    x1, y1 = x+i, y+j
                    if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
                        if grid[x1][y1] == 1:
                            return level
                        elif grid[x1][y1] == 0:
                            grid[x1][y1] = -1
                            queue.append((x1,y1))
            level += 1
        return -1

    def findFirst(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (i,j)
        
    def dfs(self, grid, x, y):
        grid[x][y] = -1
        isBorder = True
        for i, j in DIRECTIONS:
            x1, y1 = x+i, y+j
            if 0<=x1<len(grid) and 0<=y1<len(grid[0]):
                if grid[x1][y1] == 1:
                    self.dfs(grid, x1, y1)
                else:
                    self.boundries.append((x,y))
            