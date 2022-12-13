class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSums = collections.defaultdict(int)
        currSum = 0
        for i in range(len(nums)):
            currSum = (currSum + nums[i])%k
            if currSum == 0 and i > 0:
                return True
            if currSum in preSums and preSums[currSum]<i-1:
                return True
            if currSum not in preSums:
                preSums[currSum] = i
        return False