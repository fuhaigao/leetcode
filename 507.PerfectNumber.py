class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum = 1
        i = 2
        while i*i < num:
            if num%i == 0:
                sum += i
                sum += num/i
            i += 1
        return sum == num