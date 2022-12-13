class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = collections.deque([])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        
        while queue:
            x,y = queue.popleft()
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                xn, yn = x+dx, y+dy
                if xn < 0 or xn >= len(mat) or yn < 0 or yn >= len(mat[0]) or mat[xn][yn] != -1:
                    continue
                mat[xn][yn] = mat[x][y] + 1
                queue.append((xn,yn))
        return mat
                    