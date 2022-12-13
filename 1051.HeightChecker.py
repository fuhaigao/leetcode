class Solution:
    # Similar to counting sort
    def heightChecker(self, heights: List[int]) -> int:
        counter = collections.Counter(heights)
        i = 0
        diff = 0
        for height in heights:
            while counter[i] == 0:
                i += 1
            if height != i:
                diff += 1
            counter[i] -= 1
        return diff
