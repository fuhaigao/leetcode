class Solution:
    # heap solution O(logn)
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heap = []
    #     for num in nums:
    #         heapq.heappush(heap, num)
    #     for i in range(len(nums)-k):
    #         heapq.heappop(heap)
    #     return heapq.heappop(heap)

    # quick sort partition O(N) for this question since: T(n) = T(n/2)+O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high: 
            index = self.partition(low, high, nums)
            if index == k-1:
                return nums[index]
            elif index > k-1:
                high = index-1
            else:
                low = index+1
        return -1
            
    def partition(self, low, high, nums):
        index = low
        pivot = high
        for i in range(low, high):
            if nums[i] >= nums[pivot]:
                nums[i], nums[index]= nums[index], nums[i]
                index += 1
        nums[index], nums[pivot] = nums[pivot], nums[index]
        return index


        
        
    