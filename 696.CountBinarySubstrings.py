class Solution:
    '''
    when there exists consecutive numbers with 1 and 0 like, the minimum number of 0 and 1 is the number of substrings generated from these numbers. 
    e.g. '00111' => '01', '0011'
    '''
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = 0, 1
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                result += min(curr, prev)
                prev = curr
                curr = 1
        result += min(curr, prev)
        return result