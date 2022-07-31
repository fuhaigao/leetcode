class Solution:
    # Only need to check from n ~ n/2, since  for every i < N/2, the binary string of 2*i will contain binary string of i.
    # e.g. 16 = b01111, 8 = b01000, no need to check 0~7, since they are covered by 8~16
    def queryString(self, s: str, n: int) -> bool:
        for i in range(n, n//2, -1):
            if bin(i)[2:] not in s:
                return False
        return True