class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        letters = collections.defaultdict(int)
        start = 0
        res = 0
        for i, c in enumerate(s):
            letters[c] += 1
            while len(letters) > k:
                letters[s[start]] -= 1
                if letters[s[start]] == 0:
                    del letters[s[start]]
                start += 1
            res = max(res, i-start+1)
        return res