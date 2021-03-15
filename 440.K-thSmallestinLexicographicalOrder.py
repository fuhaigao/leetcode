class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        a = 1
        k -= 1
        while k > 0:
            gap = self.findGap(a, a+1, n)
            if gap <= k:
                k -= gap
                a += 1
            else:
                a *= 10
                k-=1
        return a

    def findGap(self, a, b, n):
        gap = 0
        while a <= n:
            if b < n+1:
                gap = gap + (b-a)
            else:
                gap = gap + (n-a+1)
            a *= 10
            b *= 10
        return gap