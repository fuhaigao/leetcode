class Solution:
    # Sliding Window
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = maxLength = 0
        for i in range(len(s)):
            maxCost -= abs(ord(s[i]) - ord(t[i]))
            while maxCost < 0:
                maxCost += abs(ord(s[start]) - ord(t[start]))
                start += 1
            maxLength = max(maxLength, i-start+1)
        return maxLength