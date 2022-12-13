class Solution:
    # item in min_heap: tuple (sum, num1, num2, index_of_nums2)
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for i in range(len(nums2)):
            if i == k:
                break
            heapq.heappush(minHeap, (nums1[0]+nums2[i], nums1[0], nums2[i], 0))
        
        while k>0 and minHeap:
            sum, n1, n2, idx = heapq.heappop(minHeap)
            res.append([n1, n2])
            k -= 1
            if idx == len(nums1)-1:
                continue
            n1 = nums1[idx+1]
            heapq.heappush(minHeap, (n1+n2, n1, n2, idx+1))
            
        return res