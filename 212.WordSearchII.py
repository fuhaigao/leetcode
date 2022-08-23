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
        self.res = list()
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for letter in word:
                curr = curr.children[letter]
            curr.word = word
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(root, board, i, j)
        return self.res
    
    # prefer this dfs, since it is more intuitive, but a bit slower (will get TLE but nothing wrong with structure)
    # add the following trie.num_of_words = len(words), and decrement this by 1 every time you add a word to solution and at the beginning of the dfs return if num_of_words == 0 
    def dfs(self, node, board, i, j):
        if node.word != "" and node.word not in self.res:
            self.res.append(node.word)
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        val = board[i][j]
        node = node.children.get(val)
        if node:
            for direction in [[1,0], [-1,0], [0,1], [0,-1]]:
                board[i][j] = "."
                self.dfs(node, board, i+direction[0], j+direction[1])
                board[i][j] = val
    
#     def dfs(self, root, board, i, j):
#         key = board[i][j]
#         node = root.children.get(key)
#         if node:
#             if node.word != "" and node.word not in self.res:
#                 self.res.append(node.word)
        
#             board[i][j] = '.'
#             if i>0: 
#                 self.dfs(node, board, i-1, j)
#             if i<len(board)-1: 
#                 self.dfs(node, board, i+1, j)
#             if j>0: 
#                 self.dfs(node, board, i, j-1)
#             if j<len(board[0])-1:   
#                 self.dfs(node, board, i, j+1)
#             board[i][j] = key
            
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = ""