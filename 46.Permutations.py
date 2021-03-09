class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res)
        return res
    
    def helper(self, nums, curr, res):
        if len(curr) == len(nums):
            res.append(curr)
            return
        for num in nums:
            if num in curr:
                continue
            else:
                self.helper(nums, curr+[num], res)
        return