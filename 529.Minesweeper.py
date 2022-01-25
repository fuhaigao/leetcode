class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        moves = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
        self.dfs(board, click[0], click[1], moves)
        return board
    
    def dfs(self, board, i, j, moves):
        if board[i][j] == 'M':
            board[i][j] = 'X'
        if board[i][j] == 'E':
            count = 0
            for rMove, colMove in moves:
                if i+rMove >= 0 and i+rMove <= len(board)-1 and j+colMove >= 0 and j+colMove <= len(board[0])-1:
                    if board[i+rMove][j+colMove] == 'M':
                        count += 1
            if count > 0:
                board[i][j] = str(count)
            else:
                board[i][j] = 'B'
                for rMove, colMove in moves:
                    if i+rMove >= 0 and i+rMove <= len(board)-1 and j+colMove >= 0 and j+colMove <= len(board[0])-1:
                        self.dfs(board, i+rMove, j+colMove, moves)