class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in sorted(products):
            trie.addWord(word)
        res = []
        curr = trie.root
        for letter in searchWord:
            curr = curr.children[letter]
            res.append(curr.suggestions)
        return res
        
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestions = list()
    
    def addSuggestion(self, word):
        if len(self.suggestions) < 3:
            self.suggestions.append(word)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for letter in word:
            curr = curr.children[letter]
            curr.addSuggestion(word)