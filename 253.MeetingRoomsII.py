class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        pq = []
        for interval in intervals:
            if pq and pq[0] <= interval[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, interval[1])
        return len(pq)
