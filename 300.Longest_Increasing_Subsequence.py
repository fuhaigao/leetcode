class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0]*len(nums)
        size = 0
        for num in nums:
            low, high = 0, size
            while low < high:
                mid = (low+high)//2
                if tails[mid] < num:
                    low = mid+1
                else:
                    high = mid
            tails[low] = num
            size = max(low+1, size)
        return size