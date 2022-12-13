class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.values = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        if idKey != self.ptr:
            self.values[idKey] = value
            return []
        stream = [value]
        self.ptr += 1
        while self.ptr in self.values:
            stream += [self.values[self.ptr]]
            self.ptr += 1
        return stream


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
