'''
https://leetcode.com/problems/matrix-block-sum/discuss/477041/Java-Prefix-sum-with-Picture-explain-Clean-code-O(m*n)
'''
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat[0]), len(mat)
        # use n+1 and m+1, so we don't need to deal with i=0 and j=0
        presums = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                presums[i][j] = presums[i-1][j] + presums[i][j-1] - presums[i-1][j-1] + mat[i-1][j-1]
        
        
        
        res = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                c1, c2 = max(0, c-k), min(n-1, c+k)
                r1, r2 = max(0, r-k), min(m-1, r+k)
                c1, c2, r1, r2 = c1+1, c2+1, r1+1, r2+1
                res[r][c] = presums[r2][c2] - presums[r1-1][c2] - presums[r2][c1-1] + presums[r1-1][c1-1]
        return res