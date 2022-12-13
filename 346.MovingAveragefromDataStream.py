class MovingAverage:

    def __init__(self, size: int):
        self.nums = [0]*size
        self.insert = 0
        self.sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        if self.count < len(self.nums):
            self.count += 1
        self.sum -= self.nums[self.insert]
        self.sum += val
        self.nums[self.insert] = val
        self.insert = (self.insert+1) % len(self.nums)

        return self.sum / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
