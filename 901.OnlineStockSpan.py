class StockSpanner:
    '''
    单调栈
    Important: consecutive days starting from today
    '''
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            _, num = self.stack.pop()
            count += num
        self.stack.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)