class Solution:
    '''
    Sliding Window
    very similar to 992
    '''
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMostKOdds(nums, k) - self.atMostKOdds(nums, k-1)
    
    def atMostKOdds(self, nums, k):
        start = 0
        result = 0
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                k -= 1
            while k < 0:
                if nums[start]%2 == 1:
                    k += 1
                start += 1
            result += i-start+1
        return result