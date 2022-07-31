class Solution:
    # BFS
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        queue, borders, components = [[row, col]], set(), set((row, col))
        while queue:
            r, c = queue.pop(0)
            for x, y in [[-1,0], [1,0], [0,-1], [0,1]]:
                currRow, currCol = r+x, c+y
                if 0 <= currRow < len(grid) and 0 <= currCol < len(grid[0]) and grid[currRow][currCol] == grid[row][col]:
                    if (currRow, currCol) not in components:
                        components.add((currRow, currCol))
                        queue.append([currRow, currCol])
                else:
                    borders.add((r,c))
        for r, c in borders:
            grid[r][c] = color
        return grid
        