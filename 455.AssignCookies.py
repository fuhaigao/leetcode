class Solution:
    # Greedy
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j, res = 0, 0, 0
        g.sort()
        s.sort()
        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1
        return res