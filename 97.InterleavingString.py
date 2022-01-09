class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DFS
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        stack = [(0,0)]
        visited = set((0,0))
        while stack:
            x, y = stack.pop()
            if x+y == l3:
                return True
            if x+1 <= l1 and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y))
                visited.add((x+1, y))
            if y+1 <= l2 and s2[y] == s3[x+y] and (x,y+1) not in visited:
                stack.append((x, y+1))
                visited.add((x, y+1))
        return False