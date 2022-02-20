class Solution:
    '''
    Sliding Window with AtMostK as helper function
    '''
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal > 0:
            return self.atMostK(nums, goal) - self.atMostK(nums, goal-1)
        else:
            return self.atMostK(nums, goal)
        
    def atMostK(self, nums, goal):
        start, result = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                goal -= 1
            while goal < 0:
                if nums[start] == 1:
                    goal += 1
                start += 1
            result += i-start+1
        return result