class Solution:
    # https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/820072/EASY-soultion-with-DRY-RUN-JAVA
    def getMaxLen(self, nums: List[int]) -> int:
        res, positive, negative = 0, 0, 0
        for num in nums:
            if num == 0:
                positive, negative = 0, 0
            elif num > 0:
                positive = positive + 1
                if negative != 0:
                    negative += 1
            else:
                tmp = positive
                positive = 0 if negative == 0 else negative+1
                negative = tmp + 1
            res = max(res, positive)
        return res