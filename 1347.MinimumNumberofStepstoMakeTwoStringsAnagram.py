class Solution:
    def minSteps(self, s: str, t: str) -> int:
        alphabet = [0]*26
        for i in range(max(len(s), len(t))):
            if i < len(s):
                alphabet[ord(s[i]) - ord('a')] += 1
            if i < len(t):
                alphabet[ord(t[i]) - ord('a')] -= 1
        # Acutually no need to consider negatives, since the question is asking steps to convert s to t
        pos, neg = 0, 0
        for val in alphabet:
            if val > 0:
                pos += val
            if val < 0:
                neg -= val
        return max(pos, neg)
    