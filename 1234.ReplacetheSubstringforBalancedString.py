class Solution:
    '''
    Sliding Window
    '''
    def balancedString(self, s: str) -> int:
        n = len(s)
        counter = collections.Counter(s)
        result, start = float('inf'),0
        for i in range(n):
            counter[s[i]] -= 1
            while start < n and counter['Q'] <= n/4 and counter['W'] <= n/4 and counter['E'] <= n/4 and counter['R'] <= n/4:
                result = min(result, i-start+1)
                counter[s[start]] += 1
                start += 1
        return result