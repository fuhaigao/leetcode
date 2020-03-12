class Solution:
    def integerBreak(self, n: int) -> int:
        product = 1
        if n == 2: return 1
        if n == 3: return 2
        # n > 4 sine 2*2 > 3*1, if it ends up with 4, always use 2*2 which is 4
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        return product