class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.keyValue = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self.keyValue[key]
        self.keyValue[key] = val
        curr = self.root
        for c in key:
            curr = curr.children[c]
            curr.val += diff
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            curr = curr.children[c]
        return curr.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = collections.defaultdict(TrieNode)