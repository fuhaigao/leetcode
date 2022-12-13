'''
1. queue O(n)
2. binary search O(log n)
'''
# 1.queue
# class RecentCounter:

#     def __init__(self):
#         self.queue = collections.deque()

#     def ping(self, t: int) -> int:
#         self.queue.append(t)
#         while self.queue[0] < t-3000:
#             self.queue.popleft()
#         return len(self.queue)

# 2.binary search


class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        idx = self.findIndex(t-3000)
        return len(self.counter) - idx

    def findIndex(self, val):
        left, right = 0, len(self.counter)-1
        while left < right:
            mid = (left+right) // 2
            if self.counter[mid] == val:
                return mid
            elif val < self.counter[mid]:
                right = mid
            else:
                left = mid + 1
        return left


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
