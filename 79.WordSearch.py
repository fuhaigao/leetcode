class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.bfs(i, j, board, word) == True:
                    return True
        return False

    def bfs(self, i, j, board, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        board[i][j] = '.'
        flag = self.bfs(i+1, j, board, word[1:]) or self.bfs(i-1, j, board, word[1:]) or self.bfs(
            i, j+1, board, word[1:]) or self.bfs(i, j-1, board, word[1:])
        board[i][j] = word[0]
        return flag
