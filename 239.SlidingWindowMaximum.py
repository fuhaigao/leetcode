class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        queue = []
        for i in range(len(nums)):
            # pop the leftmost number if it is out of range k
            if len(queue)>0 and queue[0] < i-k+1:
                queue.pop(0)
            # Remove useless number when new number is added to queue
            # Useless: Any number in the queue that is smaller than new added number, because it will never be the maximum amongst the range 
            # Important: Scan from right to left
            while len(queue)>0 and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                results.append(nums[queue[0]])
        return results