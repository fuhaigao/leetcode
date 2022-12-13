class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [-1] * len(intervals)
        starts = sorted([(interval[0], idx)
                        for idx, interval in enumerate(intervals)])
        for i, interval in enumerate(intervals):
            res[i] = self.getRightInterval(starts, interval[1])
        return res

    def getRightInterval(self, starts, target):
        left, right = 0, len(starts)-1
        while left < right:
            mid = (left+right) // 2
            if target == starts[mid][0]:
                return starts[mid][1]
            elif target > starts[mid][0]:
                left = mid+1
            else:
                right = mid
        return starts[left][1] if starts[left][0] >= target else -1
