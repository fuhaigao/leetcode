class Node:
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        node = Node(key, value)
        self.dict[key] = node
        self.add(node)
        if len(self.dict) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dict[n.key]

            
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)