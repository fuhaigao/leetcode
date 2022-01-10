class Solution:
    # Greedy
    def jump(self, nums: List[int]) -> int:
        end, farthestReach, count = 0, 0, 0
        curr = 0
        while end < len(nums)-1:
            count += 1
            while curr <= end and curr < len(nums):
                farthestReach = max(farthestReach, curr+nums[curr])
                curr += 1
            if end == farthestReach:
                return -1
            end = farthestReach
        return count