class Solution:
    # (x0 - y0) / (x1 -y1)  != (x0 - z0) / (x1 - z1)
    def isBoomerang(self, p: List[List[int]]) -> bool:
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])