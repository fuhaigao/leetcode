class Solution:
    def __init__(self):
        self.result = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range(n)]
        self.backtracking(0, n, board)
        return self.result
    def backtracking(self, row, n, board):
        if row == n:
            tmp = []
            for row in board:
                s = ''.join(row)
                tmp.append(s)
            self.result.append(tmp)
            return
        for i in range(n):
            if self.isValid(row, i, board):
                board[row][i] = 'Q'
                self.backtracking(row+1, n, board)
                board[row][i] = '.'
                
    def isValid(self, row, col, board):
        # check if current col has queen
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        
        # check 45 degree
        i, j = row-1, col-1
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i, j = i-1, j-1
        
        # check 135 degree
        i, j = row-1, col+1
        while i >=0 and j <len(board):
            if board[i][j] == 'Q':
                return False
            i, j = i-1, j+1
        
        return True