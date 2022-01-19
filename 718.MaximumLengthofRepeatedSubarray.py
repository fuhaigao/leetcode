class Solution:
    '''
    DP
    '''
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0]*(n2+1) for i in range(n1+1)]
        result = 0
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
                    result = max(result, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0
        return result