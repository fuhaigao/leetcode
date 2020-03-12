class Solution:
    # item in min_heap: tuple (sum, num1, num2, index_of_nums2)
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        res = []
        if len(nums1) == 0 or len(nums2) == 0:
             return res
        for i in range(len(nums1)):
            if i >= k: break
            sum = nums1[i] + nums2[0]
            heapq.heappush(min_heap, (sum, nums1[i], nums2[0], 0))
        while min_heap and k > 0:
            curr_entry = heapq.heappop(min_heap)
            k -= 1
            res.append([curr_entry[1], curr_entry[2]])
            prev_index = curr_entry[3]
            if prev_index == len(nums2)-1: 
                continue
            num1, num2 = curr_entry[1], nums2[prev_index+1]
            heapq.heappush(min_heap, (num1 + num2, num1, num2, prev_index+1))
        return res