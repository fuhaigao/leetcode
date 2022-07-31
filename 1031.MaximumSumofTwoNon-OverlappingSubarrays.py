class Solution:
    '''
    Sliding Window + Prefix sum
    
    Divide into two conditions:
    1. first subarray is on the left of second subarry
    2. first subarray is on the right of second subarry

    Traverse prefix sum arrary to update the maximum sum
    '''
    
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # define prefix sum array
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        maxSum = nums[firstLen + secondLen -1]
        # Condition 1: 1st subarray on the left of 2nd subarray
        # window  | --- 1st --- | --- 2nd --- |
        lMax = nums[firstLen-1] 
        for i in range(firstLen+secondLen, len(nums)):
            lMax = max(lMax, nums[i-secondLen]-nums[i-secondLen-firstLen])
            maxSum = max(maxSum, lMax+nums[i]-nums[i-secondLen])
            
        # Condition 2: 1st subarray on the right of 2nd subarray
        # window  | --- 2nd --- | --- 1st --- |
        rMax = nums[secondLen-1]
        for i in range(firstLen+secondLen, len(nums)):
            rMax = max(rMax, nums[i-firstLen]-nums[i-firstLen-secondLen])
            maxSum = max(maxSum, rMax+nums[i]-nums[i-firstLen])
            
        return maxSum