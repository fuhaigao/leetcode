class Solution:
    
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         n = len(cardPoints)
#         leftSums, rightSums = [0]*(n+1), [0]*(n+1)
#         for i in range(1, n+1):
#             leftSums[i] = leftSums[i-1] + cardPoints[i-1]
#         for i in range(n-1, -1, -1):
#             rightSums[i] = rightSums[i+1] + cardPoints[i]
        
#         curr = leftSums[k]
#         maxValue = curr
#         for i in range(1, k+1):
#             curr = leftSums[k-i] + rightSums[n-i]
#             maxValue = max(maxValue, curr)
#         return maxValue

# Optimized: O(1) memory
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        leftSums = 0
        for i in range(k):
            leftSums += cardPoints[i]
        maxVal = leftSums
        rightSums = 0
        for i in range(k):
            leftSums -= cardPoints[k-1-i]
            rightSums += cardPoints[n-1-i]
            maxVal = max(maxVal, leftSums+rightSums)
        return maxVal