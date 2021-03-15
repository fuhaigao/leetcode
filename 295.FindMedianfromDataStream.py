class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.small, -num)
            largest_from_small = -heapq.heappop(self.small)
            heapq.heappush(self.large, largest_from_small)
            # 优化
            # heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.large, num)
            smallest_from_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_from_large)
            #优化
            # heapq.heappush(self.small, -heapq.heappushpop(self.large, num))


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return float(self.large[0])



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()