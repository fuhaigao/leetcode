# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = low + (high-low)//2
            if guess(mid) == 1:
                low = mid + 1
            elif guess(mid) == -1:
                high = mid
            else:
                return mid
        return low