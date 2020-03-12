class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # stores the length of chosen nums at index i 
        if len(nums) == 0:
            return 0
        positive = [0] * len(nums)
        negative = [0] * len(nums)
        positive[0] = 1
        negative[0] = 1
        for i in range(1, len(nums)):
            # difference > 0 condition: 
            if nums[i] > nums[i-1]:
                positive[i] = negative[i-1] + 1
                negative[i] = negative[i-1]
            # difference < 0 condition: 
            elif nums[i] < nums[i-1]:
                negative[i] = positive[i-1] + 1
                positive[i] = positive[i-1]
            #difference == 0 condition:
            else:
                negative[i] = negative[i-1]
                positive[i] = positive[i-1]
        return max(positive[-1], negative[-1])