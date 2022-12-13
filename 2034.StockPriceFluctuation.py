class StockPrice:

    def __init__(self):
        self.stocks = {}
        self.latestTimestamp = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))
        self.stocks[timestamp] = price
        self.latestTimestamp = max(self.latestTimestamp, timestamp)

    def current(self) -> int:
        return self.stocks[self.latestTimestamp]

    def maximum(self) -> int:
        # While loop clean old data
        while -self.maxHeap[0][0] != self.stocks[self.maxHeap[0][1]]:
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        # While loop clean old data
        while self.minHeap[0][0] != self.stocks[self.minHeap[0][1]]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
