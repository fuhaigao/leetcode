class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-2):
            currTarget = target - nums[i]
            j, k = i+1, n-1
            while j < k:
                if nums[j] + nums[k] < currTarget:
                    res += k-j
                    j += 1
                else:
                    k -= 1
        return res
