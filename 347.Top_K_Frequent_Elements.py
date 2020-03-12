class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        heap_max = []
        res = []
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for key,value in dict.items():
            heapq.heappush(heap_max, (-1*value, key))
        for i in range(k):
            curr_tuple = heapq.heappop(heap_max)
            res.append(curr_tuple[1])
        return res