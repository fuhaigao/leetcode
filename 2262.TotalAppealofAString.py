class Solution:
    '''
    Compare to 828:
    828 遇到duplicate letters时，两个都不算；2262 则要算一个
    这导致 828 需要record 上一个出现的位置和下一个出现的位置，从而算出 left, right; 相乘
    2262 只需啊哟record 上一个出现的位置，right 永远都是 当前位置到最后，这样substrings只会被算一次
    '''
    def appealSum(self, s: str) -> int:
        prev = dict()
        res = 0
        for i, c in enumerate(s):
            left = i - prev.get(c, -1)
            right = len(s) - i
            res += right * left
            prev[c] = i
        return res