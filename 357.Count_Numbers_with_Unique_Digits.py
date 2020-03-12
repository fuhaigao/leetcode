class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        res = 10 # init 10 numbers
        unique_digits = 9
        curr_amount = 9
        while n > 1 and unique_digits > 0:
            curr_amount *= unique_digits
            unique_digits -= 1
            res += curr_amount
            n -= 1
        return res