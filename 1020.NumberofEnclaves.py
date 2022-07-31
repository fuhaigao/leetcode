class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(x, y):
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y]:
                grid[x][y] = 0
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)

        for i in range(0, len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0])-1)
        for i in range(0, len(grid[0])):
            dfs(0, i)
            dfs(len(grid)-1, i)
        
        return sum(sum(row) for row in grid) 
    
    
        
        