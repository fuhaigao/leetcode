class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    visited.add((i,j))
        
        perimeter = 0
        while queue:
            x, y = queue.popleft()
            neighbours = 0
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                xn, yn = x+dx, y+dy
                if xn < 0 or xn >= len(grid) or yn < 0 or yn >=len(grid[0]) or grid[xn][yn] == 0:
                    continue
                neighbours += 1
                if not (xn, yn) in visited:
                    queue.append((xn,yn))
                    visited.add((xn,yn))
            perimeter += 4-neighbours
        return perimeter
    
# An alternative way (in Java):
# class Solution {
#     public int islandPerimeter(int[][] grid) {
#       int m = grid.length, n = grid[0].length;
#       int count = 0;
#       int[][] dir = {{0,1},{1,0},{-1,0},{0,-1}};
#       for(int i = 0; i < m; i++){
#         for(int j = 0; j < n; j++){
#           if(grid[i][j] == 1){
#             for(int[] d:  dir){
#               int x = i + d[0], y = j + d[1];
#               if(x < 0 || y < 0 || x == m || y == n || grid[x][y] == 0){
#                 count++;
#               }
#             } 
#           }
#         }
#       }
#       return count;  
#     }
# }