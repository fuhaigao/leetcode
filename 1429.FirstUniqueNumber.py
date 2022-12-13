'''
queue + dictionary
lazy pop numbers that are not unique
'''


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counter = collections.Counter(nums)
        self.queue = collections.deque()
        for num in nums:
            if self.counter[num] == 1:
                self.queue.append(num)

    def showFirstUnique(self) -> int:
        while self.queue and self.counter[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if len(self.queue) > 0 else -1

    def add(self, value: int) -> None:
        self.counter[value] += 1
        if self.counter[value] == 1:
            self.queue.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
