class StreamChecker:

    '''
    Use Trie to store words and check stream
    Important: reversed order of check can avoid many useless check
    e.g. stream = a,b,c,d. To check d, we need to check if any of abcd, bcd, cd, d is stored in trie. 
    we can check all conditions with 1 traversal using reversed order, but 4 traversals using in order
    '''
    
    def __init__(self, words: List[str]):
        self.letters = list()
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        curr = self.trie.root
        for i in range(len(self.letters)-1, -1, -1):
            letter = self.letters[i]
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
            if curr.isEnd:
                return True
        return False
        
        
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)