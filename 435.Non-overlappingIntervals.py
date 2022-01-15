class Solution:
    '''
    https://programmercarl.com/0435.%E6%97%A0%E9%87%8D%E5%8F%A0%E5%8C%BA%E9%97%B4.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
    2 methods:
    1. sort by interval[0] When there's an overlapping (interval[i][0] < end), update the end to the minimum value
    2. sort by interval[1] Count non-overlapping intervals and keep updating end
    '''
    
    # Method 1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], x[1]))
        print(intervals)
        end, count = float('-inf'), 0
        for interval in intervals:
            if interval[0] < end:
                count += 1
                end = min(end, interval[1])
            else:
                end = interval[1]
        return count
    
    #Mehod 2
    # class Solution:
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     if len(intervals) == 0: return 0
    #     intervals.sort(key=lambda x: x[1])
    #     count = 1 # 记录非交叉区间的个数
    #     end = intervals[0][1] # 记录区间分割点
    #     for i in range(1, len(intervals)):
    #         if end <= intervals[i][0]:
    #             count += 1
    #             end = intervals[i][1]
    #     return len(intervals) - count