class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        start, end = newInterval[0], newInterval[1]
        result = []
        index = 0
        while index < len(intervals) and intervals[index][1] < start:
            result.append(intervals[index])
            index += 1
        while index < len(intervals) and intervals[index][0] <= end:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index += 1
        result.append([start, end])
        for i in range(index, len(intervals)):
            result.append(intervals[i])
        return result