class Solution:
    # Recursion too slow
#     def validPalindrome(self, s: str) -> bool:
#         return self.isPalindrome(s, 0, len(s)-1, False)
    
#     def isPalindrome(self, s, left, right, isDeleted):
#         if left >= right:
#             return True
#         if s[left] == s[right]:
#             return self.isPalindrome(s, left+1, right-1, isDeleted)
#         if not isDeleted:
#             return self.isPalindrome(s, left+1, right, True) or self.isPalindrome(s, left, right-1, True)

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True