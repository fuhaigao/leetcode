# DP solution, 难点是 traversal 顺序
class Solution:
    '''
    dp[i][j]: is s[i:j] a palindromic substring or not
    transform function:
        dp[i][j] = dp[i+1][j-1] if j-i >= 1 and s[i]==s[j]
    traversal:
        since dp[i][j] depends on i+1, j-1, start from bottom left to top right
    '''
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        result = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True
                        result += 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                        if dp[i][j] == True:
                            result += 1
        return result

# Brute Force
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         if not s or len(s) == 0:
#             return 0
#         count = 0
#         for i in range(len(s)):
#             # odd length: ex. 333
#             count += self.check_palindrome(s, i, i)
#             # even length: ex. 22
#             count += self.check_palindrome(s, i, i+1)
#         return count
    
#     def check_palindrome(self, s, start, end):
#         count = 0
#         while start >= 0 and end < len(s) and s[start] == s[end]:
#             start -= 1
#             end += 1
#             count += 1
#         return count