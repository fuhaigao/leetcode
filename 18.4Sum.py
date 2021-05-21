class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums)<4:
            return res      
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                start = j+1
                end = len(nums)-1
                while start < end:
                    sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum < target:
                        start += 1
                    elif sum > target:
                        end -= 1
                    else:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start+1]:
                            start += 1
                        while start < end and nums[end] == nums[end-1]:
                            end -= 1
                        start += 1
                        end -= 1
        return res