class Solution:
    '''
    Slding Window
    '''
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, result = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            result = max(result, i-start+1)
        return result