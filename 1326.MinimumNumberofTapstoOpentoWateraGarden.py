class Solution:
    # greedy
    def minTaps(self, n: int, ranges: List[int]) -> int:
        tapRanges = []
        for i in range(len(ranges)):
            start = i - ranges[i]
            end = i + ranges[i]
            tapRanges.append((start, end))
        tapRanges = sorted(tapRanges, key=lambda x:x[0])
        count, end, curr, farthestMove = 0, 0, 0, 0
        while end < len(ranges)-1:
            count += 1
            while curr < len(ranges) and tapRanges[curr][0] <= end:
                farthestMove = max(farthestMove, tapRanges[curr][1])
                curr += 1
            if farthestMove == end:
                return -1
            end = farthestMove
        return count