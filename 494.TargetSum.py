class Solution:
    '''
    DP 01背包：要想到数字可以被分为两组，此时找正数组可以得到的最多可能性
    https://programmercarl.com/0494.%E7%9B%AE%E6%A0%87%E5%92%8C.html#%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92
    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numSum = sum(nums)
        if numSum < abs(target):
            return 0
        if (target+numSum)%2 == 1:
            return 0
        # x - (sum-x) = target -> x = (target+sum)/2
        n = (target+numSum)//2
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(0, len(nums)):
            currNum = nums[i]
            for j in range(n, currNum-1, -1):
                dp[j] += dp[j-currNum]
        return dp[n]