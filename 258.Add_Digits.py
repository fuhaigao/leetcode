class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while num // 10 >=1:
            digit_sum = 0
            while num > 0:
                digit_sum += num%10
                num //= 10
            num = digit_sum
        return num       