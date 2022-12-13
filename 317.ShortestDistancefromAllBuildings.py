class Solution:
    # BFS, keep track number of reachable building
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dist = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        reach = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def bfs(i, j, cnt):
            queue = collections.deque([(i, j, 0)])
            while queue:
                x, y, step = queue.popleft()
                step += 1
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    xn, yn = x+dx, y+dy
                    if 0 <= xn < len(grid) and 0 <= yn < len(grid[0]) and grid[xn][yn] == 0 and reach[xn][yn] == cnt:
                        queue.append((xn, yn, step))
                        dist[xn][yn] += step
                        reach[xn][yn] += 1

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bfs(i, j, cnt)
                    cnt += 1

        res = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and reach[i][j] == cnt:
                    res = min(res, dist[i][j])

        return res if res != float('inf') else -1
