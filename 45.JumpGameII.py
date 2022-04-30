class Solution:
    # Greedy
    def jump(self, nums: List[int]) -> int:
        currMove, currEnd = 0, 0
        steps = 0
        farthestReach = 0
        while currEnd < len(nums)-1:
            steps += 1
            while currMove <= currEnd and currMove < len(nums):
                farthestReach = max(farthestReach, currMove + nums[currMove])
                currMove += 1
            if currEnd == farthestReach:
                return -1
            currEnd = farthestReach
        return steps
