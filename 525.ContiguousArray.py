class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        presums = collections.defaultdict(int)
        curr, maxLength = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1
            if curr == 0:
                maxLength = max(maxLength, i+1)
                continue
            if curr in presums:
                maxLength = max(maxLength, i-presums[curr])
            else:
                presums[curr] = i
        return maxLength