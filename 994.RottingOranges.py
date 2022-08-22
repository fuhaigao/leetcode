class Solution:
    '''
    Simple BFS
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque([])
        minutes, count = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                x0, y0 = queue.popleft()
                for i, j in [[1,0],[-1,0],[0,1],[0,-1]]:
                    x, y = x0+i, y0+j
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        queue.append((x,y))
                        grid[x][y] = 2
                        count -= 1
            if count == 0:
                return minutes
        return -1