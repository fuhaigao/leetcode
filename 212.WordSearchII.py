# Simple DFS on each word: TLE, so we need to use Trie structure to improve performance
# class Solution:
#     def __init__(self):
#         self.result = []
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         for word in words:
#             for i in range(len(board)):
#                 for j in range(len(board[0])):
#                     self.dfs(board, i, j, word, 0)
#         return self.result
                
#     def dfs(self, board, i, j, word, index):
#         if len(word) == index:
#             if word not in self.result:
#                 self.result.append(word)
#             return
#         if i<0 or j<0 or i>=len(board) or j >= len(board[0]):
#             return
#         if board[i][j] == word[index]:
#             board[i][j] = '.'
#             self.dfs(board, i-1, j, word, index+1) 
#             self.dfs(board, i+1, j, word, index+1) 
#             self.dfs(board, i, j-1, word, index+1)
#             self.dfs(board, i, j+1, word, index+1)
#             board[i][j] = word[index]
#             return 

# Use Trie Node to imporve performance
class Solution:
    def __init__(self):
        self.result = []
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # init Trie
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.next:
                    node.next[c] = TrieNode()
                node = node.next[c]
            node.isWord = word
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, root, i, j)
        return self.result
        
    def dfs(self, board, root, i, j):
        key = board[i][j]
        node = root.next.get(key)
        if node:
            if node.isWord != "" and node.isWord not in self.result:
                self.result.append(node.isWord)
        
            board[i][j] = '.'
            if i>0: 
                self.dfs(board, node, i-1, j)
            if i<len(board)-1: 
                self.dfs(board, node, i+1, j)
            if j>0: 
                self.dfs(board, node, i, j-1)
            if j<len(board[0])-1:   
                self.dfs(board, node, i, j+1)
            board[i][j] = key
                

class TrieNode:
    def __init__(self):
        self.next = dict()
        self.isWord = ""
