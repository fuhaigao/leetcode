class Solution:
    # Binary operation
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [False]*len(nums)
        b = 0
        for i, num in enumerate(nums):
            b = b << 1 | num
            res[i] = not b%5
        return res