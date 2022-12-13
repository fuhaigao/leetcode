class Solution:
    # prefix sum
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        presums = collections.defaultdict(int)
        currSum, count = 0, 0
        for i in range(len(nums)):
            currSum = (currSum+nums[i]) % k
            if currSum == 0:
                count += 1
            count += presums[currSum]
            presums[currSum] += 1
        return count