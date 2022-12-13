class Solution:
    # prefix sum
    def longestWPI(self, hours: List[int]) -> int:
        prefixsum = collections.defaultdict(int)
        curr, maxLength = 0, 0
        for i in range(len(hours)):
            curr += 1 if hours[i] > 8 else -1
            if curr > 0:
                maxLength = max(maxLength, i+1)
            # if there exists a prefixsum x, such that curr - x = 1, then hours[x_idx:curr_idx] is well performing, derive from curr - x = 1, curr - 1 = x. Therefore check if curr-1 (x) exisits in prefixsum
            if curr-1 in prefixsum:
                maxLength = max(maxLength, i-prefixsum[curr-1])
            if curr not in prefixsum:
                prefixsum[curr] = i
        return maxLength