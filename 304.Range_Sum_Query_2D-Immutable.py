class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix is None or not matrix:
              return
        n, m = len(matrix)+1, len(matrix[0])+1
        self.sums = [[0]*m for i in range(n)]
        # self.sums = [ [0 for j i /n range(m)] for i in range(n) ]
        for i in range(1, n):
            for j in range(1, m):
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)