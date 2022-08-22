class Solution:
    '''
    Iterate all letters occured Need performance improvement
    '''
    # def characterReplacement(self, s: str, k: int) -> int:
    #     counter = collections.Counter(s)
    #     res = 0
    #     for letter in counter:
    #         start, alternates = 0, 0
    #         for i in range(len(s)):
    #             if s[i] != letter:
    #                 alternates += 1
    #             while alternates > k:
    #                 if s[start] != letter:
    #                     alternates -= 1
    #                 start += 1
    #             res = max(res, i-start+1)
    #     return res
    
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        maxLength, maxCount = 0, 0
        start = 0
        for end in range(len(s)):
            count[s[end]] += 1
            maxCount = max(maxCount, count[s[end]])
            while end-start+1-maxCount > k:
                count[s[start]] -= 1
                start += 1
            maxLength = max(maxLength, end-start+1)
        return maxLength