class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def findPath(self, path):
        if len(path) == 1:
            return self.root
        curr = self.root
        for word in path.split("/")[1:]:
            curr = curr.children[word]
        return curr
    
    def ls(self, path: str) -> List[str]:
        curr = self.findPath(path)
        if curr.content != "":
            return [path.split('/')[-1]]
        return sorted(curr.children.keys())
        
    def mkdir(self, path: str) -> None:
        self.findPath(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.findPath(filePath)
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.findPath(filePath)
        return curr.content

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.content = ""

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)