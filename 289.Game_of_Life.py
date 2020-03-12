class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                count = self.helper(board, row, col, i, j)
                if board[i][j] == 1 and count >= 2 and count <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2
        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1
        return
    
    def helper(self, board, row, col, i, j):
        count = 0
        for m in range(max(i-1, 0), min(i+2,row)):
            for n in range(max(j-1, 0), min(j+2,col)):
                count += board[m][n]&1
        count -= board[i][j]&1
        return count