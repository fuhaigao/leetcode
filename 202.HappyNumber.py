class Solution:
    def isHappy(self, n: int) -> bool:
        hs = set()
        while n > 1:
            sum = 0
            while n > 0:
                digit = n%10
                n //= 10
                sum += digit*digit
            if sum in hs:
                return False
            hs.add(sum)
            n = sum
        return True
        