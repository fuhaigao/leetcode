class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        '''
        Greedy
        sort by abs value
        '''
        nums = sorted(nums, key=lambda x:-abs(x))
        for i in range(len(nums)):
            if k>0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        if k>0:
            nums[-1] *= (-1)**k
        return sum(nums)