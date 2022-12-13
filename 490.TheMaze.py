class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = collections.deque([(start[0], start[1])])
        maze[start[0]][start[1]] = 2
        while queue:
            x, y = queue.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                xn, yn = x+dx, y+dy
                while xn >= 0 and xn < len(maze) and yn >=0 and yn < len(maze[0]) and maze[xn][yn] != 1:
                    xn += dx
                    yn += dy
                if maze[xn-dx][yn-dy] == 0:
                    queue.append((xn-dx, yn-dy))
                    maze[xn-dx][yn-dy] = 2
        return False
                