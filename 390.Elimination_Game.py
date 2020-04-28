class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        head = 1
        step = 1
        remaining = n
        while remaining > 1:
            if left:
                head += step
            else:
                if remaining % 2 == 1:
                    head += step
            remaining //= 2
            left = not left
            step *= 2
        return head