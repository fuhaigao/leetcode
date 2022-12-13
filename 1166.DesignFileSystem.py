class FileSystem:
    # Trie

    def __init__(self):
        self.root = Node(0)

    def createPath(self, path: str, value: int) -> bool:
        path = path.split("/")
        parentNode = self.findPath(path[1:-1])
        if not parentNode:
            return False
        if path[-1] in parentNode.children:
            return False
        parentNode.children[path[-1]] = Node(value)
        return True

    def get(self, path: str) -> int:
        node = self.findPath(path.split("/")[1:])
        if not node:
            return -1
        return node.val

    def findPath(self, path):
        curr = self.root
        for p in path:
            if p not in curr.children:
                return None
            curr = curr.children[p]
        return curr


class Node:

    def __init__(self, val):
        self.children = dict()
        self.val = val

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
