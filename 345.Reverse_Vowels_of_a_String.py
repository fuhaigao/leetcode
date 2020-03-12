class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s)-1
        vowels = tuple('aeiouAEIOU')
        while start < end:
            while s[start] not in vowels and start<end: start += 1
            while s[end] not in vowels and start<end: end -= 1
            if start >= end:
                break
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
        s = ''.join(s)
        return s