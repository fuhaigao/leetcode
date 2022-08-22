class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([(interval[0], idx) for idx, interval in enumerate(intervals)])
        res = [-1]*len(intervals)
        for i, interval in enumerate(intervals):
            # can be replaced as: (use bisect_left)
            # rightIntervalIdx = bisect.bisect_left(starts, (interval[1],))
            # if rightIntervalIdx == len(starts):
            #     rightIntervalIdx = -1
            # else:
            #     rightIntervalIdx = starts[rightIntervalIdx][1]
            rightIntervalIdx = self.getRightInterval(starts, interval[1])
            res[i] = rightIntervalIdx
        return res
    
    def getRightInterval(self, starts, target):
        l, r = 0, len(starts)-1
        while (l < r):
            mid = (l+r)//2
            curr = starts[mid][0]
            if curr < target:
                l = mid+1
            elif curr > target:
                r = mid
            else:
                return starts[mid][1]
        return starts[l][1] if starts[l][0] >= target else -1