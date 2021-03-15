class Solution:
    def jump(self, nums: List[int]) -> int:
        end = len(nums)-1
        steps = 0
        while end > 0:
            for i in range(end):
                if nums[i] >= (end-i):
                    end = i
                    steps += 1
                    break
        return steps