class Solution:
    '''
    sum + m*n = (minNum+m)*n
    sum - minNum * n = m
    Explain: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/93817/It-is-a-math-question
    '''
    def minMoves(self, nums: List[int]) -> int:
        numSum = sum(nums)
        minNum = min(nums)
        return numSum - minNum * len(nums)