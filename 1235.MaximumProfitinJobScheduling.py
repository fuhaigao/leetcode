class Solution:
    # Transition function:
    # 1. dp[i-1] don't pick current job
    # 2. dp[index]+p[i] pick current job and last job that not conflict with current job
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # important: sort by endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        dp = [0] * n
        dp[0] = jobs[0][2]
        
        for i in range(1, len(jobs)):
            s, e, p = jobs[i][0], jobs[i][1], jobs[i][2]
            
            # index is the last job whose endTime < currJob's startTime
            index = self.findLastJob(jobs, i)
            if index == -1:
                dp[i] = max(dp[i-1], p)
            else:
                dp[i] = max(dp[i-1], dp[index]+p)
        return dp[-1]
            
    # This func can be optimized with binary search
    def findLastJob(self, jobs, currJob):
        for i in range(currJob-1, -1, -1):
            if jobs[i][1] <= jobs[currJob][0]:
                return i
        return -1