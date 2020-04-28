class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        count = 0
        for i in range(len(s)):
            # odd length: ex. 333
            count += self.check_palindrome(s, i, i)
            # even length: ex. 22
            count += self.check_palindrome(s, i, i+1)
        return count
    
    def check_palindrome(self, s, start, end):
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            count += 1
        return count