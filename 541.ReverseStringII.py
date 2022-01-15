class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sl = list(s)
        left = 0
        while left < len(s):
            right = min(len(s)-1, left+k-1)
            sl = self.swap(sl, left, right)
            left += 2*k
        return "".join(sl)

    def swap(self, sl, l, r):
        while l < r:
            sl[l], sl[r] = sl[r], sl[l]
            l += 1; r -= 1
        return sl