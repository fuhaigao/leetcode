class Solution:
    # Binary search on enveplopes width is similar to lc 300 (LIS)
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0 or len(envelopes[0]) == 0:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        left, right, size = 0, 0, 0
        tails = [0]*len(envelopes)
        for env in envelopes:
            left, right = 0, size
            while left < right:
                mid = (left+right)//2
                if tails[mid] < env[1]:
                    left = mid+1
                else:
                    right = mid
            tails[left] = env[1]
            size = max(size, left+1)
        return size
